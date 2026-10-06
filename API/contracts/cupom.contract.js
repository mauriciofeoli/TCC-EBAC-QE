const Joi = require('joi');

const dataOuNulo = Joi.string().allow(null);

const cupomSchema = Joi.object({
  id: Joi.number().integer().positive().required(),
  code: Joi.string().required(),
  amount: Joi.string().pattern(/^\d+(\.\d+)?$/).required(),
  date_created: Joi.string().required(),
  date_created_gmt: Joi.string().required(),
  date_modified: Joi.string().required(),
  date_modified_gmt: Joi.string().required(),
  discount_type: Joi.string().valid('percent', 'fixed_cart', 'fixed_product').required(),
  description: Joi.string().allow('').required(),
  date_expires: dataOuNulo,
  date_expires_gmt: dataOuNulo,
  usage_count: Joi.number().integer().min(0).required(),
  individual_use: Joi.boolean().required(),
  product_ids: Joi.array().items(Joi.number()).required(),
  excluded_product_ids: Joi.array().items(Joi.number()).required(),
  usage_limit: Joi.number().allow(null),
  usage_limit_per_user: Joi.number().allow(null),
  limit_usage_to_x_items: Joi.number().allow(null),
  free_shipping: Joi.boolean().required(),
  product_categories: Joi.array().required(),
  excluded_product_categories: Joi.array().required(),
  exclude_sale_items: Joi.boolean().required(),
  minimum_amount: Joi.string().required(),
  maximum_amount: Joi.string().required(),
  email_restrictions: Joi.array().required(),
  used_by: Joi.array().required(),
  meta_data: Joi.array().required(),
}).unknown(true);

const listaCuponsSchema = Joi.array().items(cupomSchema);

const erroSchema = Joi.object({
  code: Joi.string().required(),
  message: Joi.string().required(),
  data: Joi.object({ status: Joi.number().required() }).unknown(true).required(),
}).unknown(true);

module.exports = { cupomSchema, listaCuponsSchema, erroSchema };
