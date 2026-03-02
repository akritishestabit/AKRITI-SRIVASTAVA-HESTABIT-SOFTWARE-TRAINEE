// const express = require("express");
// const controller = require("../controllers/product.controller");

// const router = express.Router();

// router.post("/", controller.create);
// router.get("/", controller.getAll);
// router.get("/:id", controller.getOne);
// router.put("/:id", controller.update);
// router.delete("/:id", controller.delete);

// module.exports = router;
const express = require("express");
const controller = require("../controllers/product.controller");
const validate = require("../middlewares/validate.middleware");
const {
  createProductSchema,
  updateProductSchema,
} = require("../validations/product.validation");

const router = express.Router();

// Create product with validation
router.post(
  "/",
  validate(createProductSchema),
  controller.create
);

// Get all products
router.get("/", controller.getAll);

// Get single product
router.get("/:id", controller.getOne);

// Update product with validation
router.put(
  "/:id",
  validate(updateProductSchema),
  controller.update
);

// Soft delete
router.delete("/:id", controller.delete);

module.exports = router;