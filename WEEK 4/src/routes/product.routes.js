const express = require("express");
const controller = require("../controllers/product.controller");
const validate = require("../middlewares/validate.middleware");
const authMiddleware = require("../middlewares/auth.middleware"); // ⭐ already added

const {
  createProductSchema,
  updateProductSchema,
} = require("../validations/product.validation");

const router = express.Router();


router.get("/", authMiddleware, controller.getAll);

router.get("/:id", authMiddleware, controller.getOne);


router.post(
  "/",
  authMiddleware,
  validate(createProductSchema),
  controller.create
);

router.put(
  "/:id",
  authMiddleware,
  validate(updateProductSchema),
  controller.update
);

router.delete(
  "/:id",
  authMiddleware,
  controller.delete
);

router.post(
  "/send-email",
  authMiddleware,
  controller.sendTestEmail
);

module.exports = router;