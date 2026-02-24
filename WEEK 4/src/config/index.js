const path = require("path");
const dotenv = require("dotenv");

const env = process.env.NODE_ENV || "dev";

// map environment to file
const envFileMap = {
  local: ".env.local",
  dev: ".env.dev",
  prod: ".env.prod",
};

const envFile = envFileMap[env];

if (!envFile) {
  throw new Error(`Invalid NODE_ENV: ${env}`);
}

// Load environment file
dotenv.config({
  path: path.resolve(process.cwd(), envFile),
});

// Required variables validation
const requiredEnvVars = ["PORT", "MONGO_URI"];

requiredEnvVars.forEach((key) => {
  if (!process.env[key]) {
    throw new Error(`Missing required environment variable: ${key}`);
  }
});

const config = {
  env,
  port: process.env.PORT,
  mongoUri: process.env.MONGO_URI,
  logLevel: process.env.LOG_LEVEL || "info",
};

module.exports = config;
