const request = require('supertest');

const BASE_URL = process.env.BASE_URL || 'http://lojaebac.ebaconline.art.br';
const API_USER = process.env.API_USER || 'admin_ebac';
const API_PASS = process.env.API_PASS || '@admin!&b@c!2022';

const COUPONS = '/wp-json/wc/v3/coupons';

const api = () => request(BASE_URL);

const cuponsService = {
  listar: (query = {}) => api().get(COUPONS).auth(API_USER, API_PASS).query(query),
  buscarPorId: (id) => api().get(`${COUPONS}/${id}`).auth(API_USER, API_PASS),
  cadastrar: (body) => api().post(COUPONS).auth(API_USER, API_PASS).send(body),
  excluir: (id) => api().delete(`${COUPONS}/${id}`).auth(API_USER, API_PASS).query({ force: true }),
  listarSemAutenticacao: () => api().get(COUPONS),
};

module.exports = { cuponsService };
