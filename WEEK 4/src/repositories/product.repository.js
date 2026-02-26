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

    if (!includeDeleted) {
      query.deletedAt = null;
    }

    if (search) {
      query.$text = { $search: search };
    }

    if (minPrice || maxPrice) {
      query.price = {};
      if (minPrice) query.price.$gte = Number(minPrice);
      if (maxPrice) query.price.$lte = Number(maxPrice);
    }

    if (tags) {
      query.tags = { $in: tags.split(",") };
    }

    const [sortField, sortOrder] = sort.split(":");
    const sortObj = {
      [sortField]: sortOrder === "desc" ? -1 : 1,
    };

    const skip = (page - 1) * limit;

    const [data, total] = await Promise.all([
      Product.find(query)
        .sort(sortObj)
        .skip(skip)
        .limit(Number(limit)),

      Product.countDocuments(query),
    ]);

    return {
      data,
      total,
      page: Number(page),
      totalPages: Math.ceil(total / limit),
    };
  }

  async update(id, updateData) {
    return await Product.findByIdAndUpdate(id, updateData, {
      new: true,
      runValidators: true,
    });
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
