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

  async getProducts(filters) {
    return await productRepository.findWithFilters(filters);
  }

  async updateProduct(id, data) {
    return await productRepository.update(id, data);
  }

  async deleteProduct(id) {
    return await productRepository.softDelete(id);
  }
}

module.exports = new ProductService();
