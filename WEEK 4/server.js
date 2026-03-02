// const config = require("./src/config");
// const logger = require("./src/utils/logger");
// const connectDB = require("./src/loaders/db");
// const loadApp = require("./src/loaders/app");

// const startServer = async () => {
//   try {
//     logger.info("Starting server...");

//     await connectDB();

//     const app = loadApp();

//     const server = app.listen(config.port, () => {
//       logger.info(`Server started on port ${config.port}`);
//     });

//     process.on("SIGINT", () => {
//       logger.info("Shutting down...");
//       server.close(() => {
//         logger.info("Server closed");
//         process.exit(0);
//       });
//     });

//   } catch (error) {
//     logger.error("Startup failed");
//     process.exit(1);
//   }
// };

// startServer();
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


// 🔥 Graceful Shutdown
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

// Handle termination signals
process.on("SIGINT", () => shutdown("SIGINT"));     // Ctrl+C
process.on("SIGTERM", () => shutdown("SIGTERM"));   // Kill command

// Handle unexpected crashes
process.on("uncaughtException", (error) => {
  logger.error("Uncaught Exception", { error: error.message });
  process.exit(1);
});

process.on("unhandledRejection", (reason) => {
  logger.error("Unhandled Rejection", { reason });
  process.exit(1);
});