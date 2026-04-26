const morgan = require("morgan");
const logger = require("../utils/logger");


const stream = {
  write: (message) => {
    logger.info(message.trim());
  },
};


const requestLogger = morgan(
  (tokens, req, res) => {
    return [
      `[${req.requestId}]`,
      tokens.method(req, res),
      tokens.url(req, res),
      tokens.status(req, res),
      tokens["response-time"](req, res),
      "ms",
      "-",
      tokens.res(req, res, "content-length"),
    ].join(" ");
  },
  { stream }
);

module.exports = requestLogger;