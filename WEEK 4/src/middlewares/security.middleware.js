const express = require("express");
const helmet = require("helmet");
const rateLimit = require("express-rate-limit");
const mongoSanitize = require("express-mongo-sanitize");
const hpp = require("hpp");

const applySecurityMiddlewares = (app) => {
 
  app.use(helmet());

  const limiter = rateLimit({
    windowMs: 15 * 60 * 1000,
    max: 100,
    message: {
      success: false,
      message: "Too many requests, please try again later.",
    },
  });

  app.use(limiter);


  app.use(mongoSanitize());

  app.use(hpp());


  app.use(express.json({ limit: "10kb" }));
};

module.exports = applySecurityMiddlewares;