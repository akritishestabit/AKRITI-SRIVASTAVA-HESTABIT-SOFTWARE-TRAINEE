const mongoose = require("mongoose");
const config = require("../config");
const logger = require("../utils/logger");


require("../models/Account");
require("../models/Order");

const connectDB = async () => {
  try {
    await mongoose.connect(config.mongoUri);
    logger.info("Database connected");
  } catch (error) {
    logger.error("Database connection failed");
    process.exit(1);
  }
};

module.exports = connectDB;
