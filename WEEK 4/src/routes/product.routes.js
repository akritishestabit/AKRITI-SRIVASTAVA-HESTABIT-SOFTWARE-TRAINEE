
const express = require("express");
const controller = require("../controllers/product.controller");
const validate = require("../middlewares/validate.middleware");
const {
  createProductSchema,
  updateProductSchema,
} = require("../validations/product.validation");

const router = express.Router();

router.post("/send-email", controller.sendTestEmail);


router.post(
  "/",
  validate(createProductSchema),
  controller.create
);


router.get("/", controller.getAll);


router.get("/:id", controller.getOne);

router.put(
  "/:id",
  validate(updateProductSchema),
  controller.update
);


router.delete("/:id", controller.delete);

module.exports = router;