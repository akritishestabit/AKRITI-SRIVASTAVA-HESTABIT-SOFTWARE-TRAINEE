// const productRepository = require("../repositories/product.repository");

// class ProductService {
//   async createProduct(data) {
//     return await productRepository.create(data);
//   }

//   async getProductById(id) {
//     const product = await productRepository.findById(id);
//     if (!product) {
//       const error = new Error("Product not found");
//       error.code = "PRODUCT_NOT_FOUND";
//       error.status = 404;
//       throw error;
//     }
//     return product;
//   }

//   async getProducts(filters) {
//     return await productRepository.findWithFilters(filters);
//   }

//   async updateProduct(id, data) {
//     return await productRepository.update(id, data);
//   }

//   async deleteProduct(id) {
//     return await productRepository.softDelete(id);
//   }
// }

// module.exports = new ProductService();

const productRepository = require("../repositories/product.repository");

class ProductService {
  async createProduct(data) {
    return await productRepository.create(data);
  }

  async getProductById(id) {
    const product = await productRepository.findById(id);

    if (!product) {
      const error = new Error("Product not found");
      error.code = "PRODUCT_NOT_FOUND";
      error.status = 404;
      throw error;
    }

    return product;
  }

  async getProducts(query) {
    return await productRepository.findWithFilters(query);
  }

  async updateProduct(id, data) {
    const updated = await productRepository.update(id, data);

    if (!updated) {
      const error = new Error("Product not found");
      error.code = "PRODUCT_NOT_FOUND";
      error.status = 404;
      throw error;
    }

    return updated;
  }

  async deleteProduct(id) {
    const deleted = await productRepository.softDelete(id);

    if (!deleted) {
      const error = new Error("Product not found");
      error.code = "PRODUCT_NOT_FOUND";
      error.status = 404;
      throw error;
    }

    return deleted;
  }
}

module.exports = new ProductService();