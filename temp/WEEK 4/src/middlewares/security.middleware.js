const express = require("express");
const helmet = require("helmet");
const rateLimit = require("express-rate-limit");
const mongoSanitize = require("express-mongo-sanitize");
const hpp = require("hpp");
const xss = require("xss-clean");

const applySecurityMiddlewares = (app) => {
  app.use(express.json({ limit: "10kb" }));
 
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

  app.use(xss());

  app.use(hpp());


  
};

module.exports = applySecurityMiddlewares;