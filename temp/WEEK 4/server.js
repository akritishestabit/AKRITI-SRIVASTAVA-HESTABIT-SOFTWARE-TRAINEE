const config = require("./src/config");
const logger = require("./src/utils/logger");
const connectDB = require("./src/loaders/db");
const loadApp = require("./src/loaders/app");
const mongoose = require("mongoose");

let server;

const startServer = async () => {
  try {
    logger.info("Starting server...");

    await connectDB();

    const app = loadApp();

    server = app.listen(config.port, () => {
      logger.info(`Server started on port ${config.port}`);
    });
  } catch (error) {
    logger.error("Startup failed", { error: error.message });
    process.exit(1);
  }
};

startServer();

const shutdown = async (signal) => {
  logger.info(`${signal} received. Shutting down...`);

  try {
    if (server) {
      await new Promise((resolve) => server.close(resolve));
      logger.info("HTTP server closed");
    }

    await mongoose.connection.close();
    logger.info("Database connection closed");

    process.exit(0);
  } catch (error) {
    logger.error("Error during shutdown", { error: error.message });
    process.exit(1);
  }
};

process.on("SIGINT", () => shutdown("SIGINT"));
process.on("SIGTERM", () => shutdown("SIGTERM"));

process.on("uncaughtException", (error) => {
  logger.error("Uncaught Exception", { error: error.message }); //error outside try and catch
  process.exit(1);
});

process.on("unhandledRejection", (reason) => {
  logger.error("Unhandled Rejection", { reason }); // Promise rejection not handled
  process.exit(1);
});
