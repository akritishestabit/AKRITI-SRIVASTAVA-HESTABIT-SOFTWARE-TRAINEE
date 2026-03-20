
const Joi = require("joi");

exports.createProductSchema = Joi.object({
  name: Joi.string().min(3).max(100).required(),
  description: Joi.string().min(5).required(),
  price: Joi.number().min(0).required(),
  category: Joi.string().required(),
  stock: Joi.number().min(0).optional(),

 
  tags: Joi.array().items(Joi.string()).optional(),

  
  rating: Joi.number().min(0).max(5).optional(),
});

exports.updateProductSchema = Joi.object({
  name: Joi.string().min(3).max(100).optional(),
  description: Joi.string().min(5).optional(),
  price: Joi.number().min(0).optional(),
  category: Joi.string().optional(),
  stock: Joi.number().min(0).optional(),

  
  tags: Joi.array().items(Joi.string()).optional(),

 
  rating: Joi.number().min(0).max(5).optional(),
});