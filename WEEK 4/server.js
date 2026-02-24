const config = require("./src/config");
const logger = require("./src/utils/logger");
const connectDB = require("./src/loaders/db");
const loadApp = require("./src/loaders/app");

const startServer = async () => {
  try {
    logger.info("Starting server...");

    await connectDB();

    const app = loadApp();

    const server = app.listen(config.port, () => {
      logger.info(`Server started on port ${config.port}`);
    });

    
    process.on("SIGINT", () => {
      logger.info("Shutting down server...");
      server.close(() => {
        logger.info("Server closed");
        process.exit(0);
      });
    });

  } catch (error) {
    logger.error("Server startup failed", { error });
    process.exit(1);
  }
};

startServer();
