const path = require("path");
const dotenv = require("dotenv");

const env = process.env.NODE_ENV || "dev";

const envFiles = {
  local: ".env.local",
  dev: ".env.dev",
  prod: ".env.prod",
};

const selectedEnvFile = envFiles[env];

if (!selectedEnvFile) {
  throw new Error(`Invalid NODE_ENV: ${env}`);
}

dotenv.config({
  path: path.resolve(process.cwd(), selectedEnvFile),
});

const requiredEnvVars = ["PORT", "MONGO_URI"];

requiredEnvVars.forEach((key) => {
  if (!process.env[key]) {
    throw new Error(`Missing environment variable: ${key}`);
  }
});

module.exports = {
  env,
  port: process.env.PORT,
  mongoUri: process.env.MONGO_URI,
  logLevel: process.env.LOG_LEVEL || "info",
};
