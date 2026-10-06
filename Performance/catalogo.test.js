import http from 'k6/http';
import { check, group, sleep } from 'k6';
import { BASE_URL, options as baseOptions, gerarRelatorio } from './lib/config.js';

export const options = {
  ...baseOptions,
  tags: { cenario: 'catalogo' },
};

const PRODUTOS = ['abominable-hoodie', 'aero-daily-fitness-tee', 'aether-gym-pant'];

export default function () {
  group('Listar produtos', () => {
    const res = http.get(`${BASE_URL}/produtos/`, { tags: { name: 'GET /produtos' } });
    check(res, {
      'catálogo - status 200': (r) => r.status === 200,
      'catálogo - possui produtos': (r) => r.body.includes('/product/'),
    });
  });

  sleep(1);

  group('Buscar produto', () => {
    const res = http.get(`${BASE_URL}/?s=hoodie&post_type=product`, { tags: { name: 'GET /?s=hoodie' } });
    check(res, { 'busca - status 200': (r) => r.status === 200 });
  });

  sleep(1);

  group('Detalhe do produto', () => {
    const slug = PRODUTOS[Math.floor(Math.random() * PRODUTOS.length)];
    const res = http.get(`${BASE_URL}/product/${slug}/`, { tags: { name: 'GET /product/:slug' } });
    check(res, {
      'detalhe - status 200': (r) => r.status === 200,
      'detalhe - botão comprar exibido': (r) => r.body.includes('single_add_to_cart_button'),
    });
  });

  sleep(1);
}

export const handleSummary = gerarRelatorio('catalogo');
