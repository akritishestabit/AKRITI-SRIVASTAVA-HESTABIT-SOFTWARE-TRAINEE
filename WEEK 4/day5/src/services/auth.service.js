const Account = require("../models/Account");
const bcrypt = require("bcrypt");
const { generateToken } = require("../utils/jwt");

class AuthService {
  async register(data) {
    const user = new Account(data);
    await user.save();

    const token = generateToken({ id: user._id });
    return { user, token };
  }

  async login(email, password) {
    const user = await Account.findOne({ email });

    if (!user) {
      throw new Error("User not found");
    }

    const isMatch = await bcrypt.compare(password, user.password);

    if (!isMatch) {
      throw new Error("Invalid credentials");
    }

    const token = generateToken({ id: user._id });

    return { user, token };
  }
}

module.exports = new AuthService();