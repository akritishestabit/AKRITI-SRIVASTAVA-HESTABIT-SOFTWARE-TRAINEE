const productService = require("../services/product.service");
const emailQueue = require("../jobs/email.job");

exports.create = async (req, res, next) => {
  try {
    const product = await productService.createProduct(req.body);
    res.status(201).json({ success: true, data: product });
  } catch (error) {
    next(error);
  }
};

exports.getAll = async (req, res, next) => {
  try {
    const result = await productService.getProducts(req.query);
    res.json({ success: true, ...result });
  } catch (error) {
    next(error);
  }
};

exports.getOne = async (req, res, next) => {
  try {
    const product = await productService.getProductById(req.params.id);
    res.json({ success: true, data: product });
  } catch (error) {
    next(error);
  }
};

exports.update = async (req, res, next) => {
  try {
    const product = await productService.updateProduct(
      req.params.id,
      req.body
    );
    res.json({ success: true, data: product });
  } catch (error) {
    next(error);
  }
};

exports.delete = async (req, res, next) => {
  try {
    const product = await productService.deleteProduct(req.params.id);
    res.json({ success: true, data: product });
  } catch (error) {
    next(error);
  }
};

exports.sendTestEmail = async (req, res, next) => {
  try {
    const job = await emailQueue.add(
      "sendEmail",
      {
        to: "test@example.com",
        subject: "Welcome Email",
        body: "This is a background job email.",
      },
      {
        attempts: 3,
        backoff: {
          type: "exponential",
          delay: 2000,
        },
      }
    );

    res.status(202).json({
      success: true,
      message: "Email job added to queue",
      jobId: job.id,
    });
  } catch (error) {
    next(error);
  }
};