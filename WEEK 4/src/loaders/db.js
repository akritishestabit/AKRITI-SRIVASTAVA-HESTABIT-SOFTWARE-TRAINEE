const mongoose = require("mongoose");
const config = require("../config");
const logger = require("../utils/logger");

const connectDB = async () => {
  try {
    await mongoose.connect(config.mongoUri);

    logger.info("Database connected successfully");
  } catch (error) {
    logger.error("Database connection failed", { error });
    process.exit(1);
  }
};

module.exports = connectDB;
