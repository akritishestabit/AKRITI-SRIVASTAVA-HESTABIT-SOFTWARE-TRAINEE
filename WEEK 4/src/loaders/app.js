const express = require("express");
const helmet = require("helmet");
const cors = require("cors");
const logger = require("../utils/logger");

const loadApp = () => {
  const app = express();

  // Security middlewares
  app.use(helmet());
  app.use(cors());

  // Body parser
  app.use(express.json());

  logger.info("Middlewares loaded");

  // Health check route
  app.get("/health", (req, res) => {
    res.json({ status: "OK" });
  });

  // Safe route counting (defensive coding)
  let routeCount = 0;

  if (app._router && app._router.stack) {
    routeCount = app._router.stack.filter(
      (layer) => layer.route
    ).length;
  }

  logger.info(`Routes mounted: ${routeCount} endpoints`);

  return app;
};

module.exports = loadApp;
