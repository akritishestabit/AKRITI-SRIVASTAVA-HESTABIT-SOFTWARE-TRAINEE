const Order = require("../models/Order");

class OrderRepository {
  async create(data) {
    const order = new Order(data);
    return await order.save();
  }

  async findById(id) {
    return await Order.findById(id).populate("accountId");
  }

  async findPaginated({ page = 1, limit = 10, status }) {
    const query = {};

    if (status) {
      query.status = status;
    }

    const skip = (page - 1) * limit;

    const [data, total] = await Promise.all([
      Order.find(query)
        .sort({ createdAt: -1 })
        .skip(skip)
        .limit(limit)
        .populate("accountId"),

      Order.countDocuments(query),
    ]);

    return {
      data,
      total,
      page,
      totalPages: Math.ceil(total / limit),
    };
  }

  async update(id, updateData) {
    return await Order.findByIdAndUpdate(id, updateData, {
      new: true,
      runValidators: true,
    });
  }

  async delete(id) {
    return await Order.findByIdAndDelete(id);
  }
}

module.exports = new OrderRepository();
