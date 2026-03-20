
const express = require("express");
const cors = require("cors");
const logger = require("../utils/logger");

const applySecurityMiddlewares = require("../middlewares/security.middleware");
const productRoutes = require("../routes/product.routes");
const errorMiddleware = require("../middlewares/error.middleware");
const requestLogger = require("../middlewares/requestLogger.middleware");
const tracingMiddleware = require("../utils/tracing");
const { runWithContext } = require("../utils/context");

const loadApp = () => {
  const app = express();


  applySecurityMiddlewares(app);

  
app.use(tracingMiddleware);
app.use(runWithContext);

   app.use(requestLogger);


  app.use(cors());

  logger.info("Security middlewares loaded");

  
  app.get("/health", (req, res) => {
    res.json({ status: "OK" });
  });


  app.use("/products", productRoutes);

 
  app.use(errorMiddleware);

  logger.info("Routes mounted");

 

  return app;
};

module.exports = loadApp;