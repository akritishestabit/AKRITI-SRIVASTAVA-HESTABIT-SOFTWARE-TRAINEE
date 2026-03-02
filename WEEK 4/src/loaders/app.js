// const express = require("express");
// const helmet = require("helmet");
// const cors = require("cors");
// const logger = require("../utils/logger");
// const productRoutes = require("../routes/product.routes");
// const errorMiddleware = require("../middlewares/error.middleware");



// const loadApp = () => {
//   const app = express();

//   // Security middlewares
//   app.use(helmet());
//   app.use(cors());

//   // Body parser
//   app.use(express.json());

//   logger.info("Middlewares loaded");

//   app.use("/products", productRoutes);

// // error middleware last
// app.use(errorMiddleware);

//   // Health check route
//   app.get("/health", (req, res) => {
//     res.json({ status: "OK" });
//   });

//   // Safe route counting (defensive coding)
//   let routeCount = 0;

//   if (app._router && app._router.stack) {
//     routeCount = app._router.stack.filter(
//       (layer) => layer.route
//     ).length;
//   }

//   logger.info(`Routes mounted: ${routeCount} endpoints`);

//   return app;
// };

// module.exports = loadApp;
const express = require("express");
const cors = require("cors");
const logger = require("../utils/logger");

const applySecurityMiddlewares = require("../middlewares/security.middleware");
const productRoutes = require("../routes/product.routes");
const errorMiddleware = require("../middlewares/error.middleware");

const loadApp = () => {
  const app = express();

  // Apply security first
  applySecurityMiddlewares(app);

  // CORS
  app.use(cors());

  logger.info("Security middlewares loaded");

  // Health route
  app.get("/health", (req, res) => {
    res.json({ status: "OK" });
  });

  // API routes
  app.use("/products", productRoutes);

  // Error middleware (ALWAYS LAST)
  app.use(errorMiddleware);

  logger.info("Routes mounted");

  return app;
};

module.exports = loadApp;