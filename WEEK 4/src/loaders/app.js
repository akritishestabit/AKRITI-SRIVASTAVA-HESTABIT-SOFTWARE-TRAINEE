const express = require("express");
const cors = require("cors");
const helmet = require("helmet");
const logger = require("../utils/logger");

const app = express();

const loadApp = () => {
 
  app.use(helmet());
  app.use(cors());

  
  app.use(express.json());
  app.use(express.urlencoded({ extended: true }));

  logger.info("Middlewares loaded");

  // Health route
  app.get("/health", (req, res) => {
    res.json({ status: "OK", timestamp: new Date() });
  });

  //just for testing
  app.get("/test-db", async (req, res) => {
  const mongoose = require("mongoose");
  const Test = mongoose.model("Test", new mongoose.Schema({ name: String }));
  await Test.create({ name: "Akriti" });
  res.send("Inserted");
});

  logger.info("Routes mounted");

  return app;
};

module.exports = loadApp;
