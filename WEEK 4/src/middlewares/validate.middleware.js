const Joi = require("joi");

const validate = (schema, property = "body") => {
  return (req, res, next) => {
    const { error, value } = schema.validate(req[property], {
      abortEarly: false,
      stripUnknown: true,
    });

    if (error) {
      return next({
        status: 400,
        message: error.details.map((d) => d.message).join(", "),
        code: "VALIDATION_ERROR",
      });
    }

    req[property] = value;
    next();
  };
};

module.exports = validate;