// const mongoose = require("mongoose");
// const config = require("../config");
// const logger = require("../utils/logger");

// const connectDB = async () => {
//   try {
//     await mongoose.connect(config.mongoUri);
//     logger.info("Database connected");
//   } catch (error) {
//     logger.error("Database connection failed");
//     process.exit(1);
//   }
// };

// module.exports = connectDB;
const mongoose = require("mongoose");
const config = require("../config");
const logger = require("../utils/logger");

// Import models to ensure indexes are created
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
