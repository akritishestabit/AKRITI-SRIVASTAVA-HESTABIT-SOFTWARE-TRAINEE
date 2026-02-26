const mongoose = require("mongoose");

const productSchema = new mongoose.Schema(
  {
    name: {
      type: String,
      required: true,
      trim: true,
    },

    description: {
      type: String,
      trim: true,
    },

    price: {
      type: Number,
      required: true,
      min: 0,
    },

    tags: [
      {
        type: String,
        trim: true,
      },
    ],

    category: {
      type: String,
      trim: true,
    },

    rating: {
      type: Number,
      min: 0,
      max: 5,
      default: 0,
    },

    status: {
      type: String,
      enum: ["active", "inactive"],
      default: "active",
    },

    deletedAt: {
      type: Date,
      default: null,
    },
  },
  {
    timestamps: true,
  }
);

// Compound index for filtering + sorting
productSchema.index({ status: 1, createdAt: -1 });

// Text index for search
productSchema.index({ name: "text", description: "text" });

module.exports = mongoose.model("Product", productSchema);
