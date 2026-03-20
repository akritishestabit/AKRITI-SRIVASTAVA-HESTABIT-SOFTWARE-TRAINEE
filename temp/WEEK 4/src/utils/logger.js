const winston = require("winston");
const path = require("path");
const fs = require("fs");
const { getRequestId } = require("./context");

const logDir = path.join(__dirname, "../logs");

if (!fs.existsSync(logDir)) {
  fs.mkdirSync(logDir);
}

const { combine, timestamp, errors, json, printf, colorize } =
  winston.format;

const isProduction = process.env.NODE_ENV === "prod";

const consoleFormat = printf(({ level, message, timestamp }) => {
  return `${timestamp} [${level}] : ${message}`;
});

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || "info",
  format: combine(
  timestamp(),
  errors({ stack: true }),
  winston.format((info) => {
    const requestId = getRequestId();
    if (requestId) {
      info.requestId = requestId;
    }
    return info;
  })(),
  json()
),
  transports: [
   
    new winston.transports.File({
      filename: path.join(logDir, "error.log"),
      level: "error",
    }),


    new winston.transports.File({
      filename: path.join(logDir, "combined.log"),
    }),
  ],
});


if (!isProduction) {
  logger.add(
    new winston.transports.Console({
      format: combine(
        colorize(),
        timestamp(),
        consoleFormat
      ),
    })
  );
}

module.exports = logger;