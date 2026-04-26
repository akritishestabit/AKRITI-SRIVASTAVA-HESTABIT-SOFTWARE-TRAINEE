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
      query.$or = [
        { name: new RegExp(search, "i") },
        { description: new RegExp(search, "i") },
      ];
    }

   
    
if (minPrice !== undefined || maxPrice !== undefined) {
  const priceFilter = {};

  const parsedMin = Number(minPrice);
  const parsedMax = Number(maxPrice);


  if (!isNaN(parsedMin)) {
    priceFilter.$gte = parsedMin;
  }

  if (!isNaN(parsedMax)) {
    priceFilter.$lte = parsedMax;
  }

  
  if (Object.keys(priceFilter).length > 0) {
    query.price = priceFilter;
  }
}

  
    if (tags) {
      query.tags = { $in: tags.split(",") };
    }

    
    const [sortField, sortOrder] = sort.split(":");
    const sortObj = {
      [sortField]: sortOrder === "desc" ? -1 : 1,
    };

  
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