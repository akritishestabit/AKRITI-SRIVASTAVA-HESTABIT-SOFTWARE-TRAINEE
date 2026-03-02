// const Product = require("../models/Product");

// class ProductRepository {
//   async create(data) {
//     const product = new Product(data);
//     return await product.save();
//   }

//   async findById(id) {
//     return await Product.findOne({ _id: id, deletedAt: null });
//   }

//   async findWithFilters(filters) {
//     const {
//       search,
//       minPrice,
//       maxPrice,
//       tags,
//       sort = "createdAt:desc",
//       page = 1,
//       limit = 10,
//       includeDeleted = false,
//     } = filters;

//     const query = {};

//     if (!includeDeleted) {
//       query.deletedAt = null;
//     }

//     if (search) {
//       query.$text = { $search: search };
//     }

//     if (minPrice || maxPrice) {
//       query.price = {};
//       if (minPrice) query.price.$gte = Number(minPrice);
//       if (maxPrice) query.price.$lte = Number(maxPrice);
//     }

//     if (tags) {
//       query.tags = { $in: tags.split(",") };
//     }

//     const [sortField, sortOrder] = sort.split(":");
//     const sortObj = {
//       [sortField]: sortOrder === "desc" ? -1 : 1,
//     };

//     const skip = (page - 1) * limit;

//     const [data, total] = await Promise.all([
//       Product.find(query)
//         .sort(sortObj)
//         .skip(skip)
//         .limit(Number(limit)),

//       Product.countDocuments(query),
//     ]);

//     return {
//       data,
//       total,
//       page: Number(page),
//       totalPages: Math.ceil(total / limit),
//     };
//   }

//   async update(id, updateData) {
//     return await Product.findByIdAndUpdate(id, updateData, {
//       new: true,
//       runValidators: true,
//     });
//   }

//   async softDelete(id) {
//     return await Product.findByIdAndUpdate(
//       id,
//       { deletedAt: new Date() },
//       { new: true }
//     );
//   }
// }

// module.exports = new ProductRepository();
const Product = require("../models/Product");

class ProductRepository {
  async create(data) {
    const product = new Product(data);
    return await product.save();
  }

  async findById(id) {
    return await Product.findOne({ _id: id, deletedAt: null });
  }

  async findWithFilters(filters) {
    const {
      search,
      minPrice,
      maxPrice,
      tags,
      sort = "createdAt:desc",
      page = 1,
      limit = 10,
      includeDeleted = false,
    } = filters;

    const query = {};

    // Soft delete filter
    if (!includeDeleted) {
      query.deletedAt = null;
    }

    // 🔥 RegExp search (FIXED VERSION)
    if (search) {
      query.$or = [
        { name: new RegExp(search, "i") },
        { description: new RegExp(search, "i") },
      ];
    }

    // Price range filter
    if (minPrice || maxPrice) {
      query.price = {};
      if (minPrice) query.price.$gte = Number(minPrice);
      if (maxPrice) query.price.$lte = Number(maxPrice);
    }

    // Tags filter
    if (tags) {
      query.tags = { $in: tags.split(",") };
    }

    // Sorting
    const [sortField, sortOrder] = sort.split(":");
    const sortObj = {
      [sortField]: sortOrder === "desc" ? -1 : 1,
    };

    // Pagination
    const pageNumber = Number(page);
    const limitNumber = Number(limit);
    const skip = (pageNumber - 1) * limitNumber;

    const [data, total] = await Promise.all([
      Product.find(query)
        .sort(sortObj)
        .skip(skip)
        .limit(limitNumber),

      Product.countDocuments(query),
    ]);

    return {
      data,
      total,
      page: pageNumber,
      totalPages: Math.ceil(total / limitNumber),
    };
  }

  async update(id, updateData) {
    return await Product.findOneAndUpdate(
      { _id: id, deletedAt: null },
      updateData,
      {
        new: true,
        runValidators: true,
      }
    );
  }

  async softDelete(id) {
    return await Product.findByIdAndUpdate(
      id,
      { deletedAt: new Date() },
      { new: true }
    );
  }
}

module.exports = new ProductRepository();