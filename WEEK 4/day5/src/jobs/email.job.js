const { Queue, Worker } = require("bullmq");
const IORedis = require("ioredis");
const logger = require("../utils/logger");


const connection = new IORedis({
  host: "127.0.0.1",
  port: 6379,
  maxRetriesPerRequest: null,
});


const emailQueue = new Queue("emailQueue", { connection });

const emailWorker = new Worker(
  "emailQueue",
  async (job) => {
    logger.info(`Processing email job: ${job.id}`);

    const { to, subject, body } = job.data;

    
    await new Promise((resolve) => setTimeout(resolve, 2000));

    logger.info(`Email sent to ${to} with subject: ${subject}`);

    return { success: true };
  },
  { connection }
);


emailWorker.on("completed", (job) => {
  logger.info(`Job ${job.id} completed successfully`);
});

emailWorker.on("failed", (job, err) => {
  logger.error(`Job ${job.id} failed: ${err.message}`);
});

module.exports = emailQueue;