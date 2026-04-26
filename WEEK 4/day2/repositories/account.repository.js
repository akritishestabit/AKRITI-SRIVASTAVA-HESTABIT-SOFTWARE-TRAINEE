const Account = require("../models/Account");

class AccountRepository {
  async create(data) {
    const account = new Account(data);
    return await account.save();
  }

  async findById(id) {
    return await Account.findById(id);
  }

  async findPaginated({ page = 1, limit = 10, status }) {
    const query = {};

    if (status) {
      query.status = status;
    }

    const skip = (page - 1) * limit;

    const [data, total] = await Promise.all([
      Account.find(query)
        .sort({ createdAt: -1 })
        .skip(skip)
        .limit(limit),

      Account.countDocuments(query),
    ]);

    return {
      data,
      total,
      page,
      totalPages: Math.ceil(total / limit),
    };
  }

  async update(id, updateData) {
    return await Account.findByIdAndUpdate(id, updateData, {
      new: true,
      runValidators: true,
    });
  }

  async delete(id) {
    return await Account.findByIdAndDelete(id);
  }
}

module.exports = new AccountRepository();
