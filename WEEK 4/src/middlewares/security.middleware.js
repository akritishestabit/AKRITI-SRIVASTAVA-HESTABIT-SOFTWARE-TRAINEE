// const express = require("express");
// const helmet = require("helmet");
// const rateLimit = require("express-rate-limit");
// const mongoSanitize = require("express-mongo-sanitize");
// const hpp = require("hpp");
// const xssClean = require("xss-clean");

// const applySecurityMiddlewares = (app) => {
//   // Secure HTTP headers
//   app.use(helmet());

//   // Rate limiting
//   const limiter = rateLimit({
//     windowMs: 15 * 60 * 1000,
//     max: 100,
//     message: {
//       success: false,
//       message: "Too many requests, please try again later.",
//     },
//   });

//   app.use(limiter);

//   // Prevent NoSQL injection
//   app.use(mongoSanitize());

//   // Prevent HTTP parameter pollution
//   app.use(hpp());

//   // Prevent XSS
//   app.use(xssClean());

//   // Limit request body size
//   app.use(express.json({ limit: "10kb" }));
// };

// module.exports = applySecurityMiddlewares;
const express = require("express");
const helmet = require("helmet");
const rateLimit = require("express-rate-limit");
const mongoSanitize = require("express-mongo-sanitize");
const hpp = require("hpp");

const applySecurityMiddlewares = (app) => {
  // Secure headers
  app.use(helmet());

  // Rate limiting
  const limiter = rateLimit({
    windowMs: 15 * 60 * 1000,
    max: 100,
    message: {
      success: false,
      message: "Too many requests, please try again later.",
    },
  });

  app.use(limiter);

  // Prevent NoSQL injection
  app.use(mongoSanitize());

  // Prevent HTTP parameter pollution
  app.use(hpp());

  // Limit body size
  app.use(express.json({ limit: "10kb" }));
};

module.exports = applySecurityMiddlewares;