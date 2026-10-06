const { faker } = require('@faker-js/faker');

// Data Factory: gera massa de dados única para cada execução
const novoCupom = (overrides = {}) => ({
  code: `TCC-${faker.string.alphanumeric(8).toUpperCase()}`,
  amount: '10.00',
  discount_type: 'fixed_product',
  description: 'Cupom de teste',
  ...overrides,
});

module.exports = { novoCupom };
