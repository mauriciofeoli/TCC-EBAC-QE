import http from 'k6/http';
import { check, group, sleep } from 'k6';
import { SharedArray } from 'k6/data';
import { BASE_URL, options as baseOptions, gerarRelatorio } from './lib/config.js';

const usuarios = new SharedArray('usuarios', () => JSON.parse(open('./data/usuarios.json')));

export const options = {
  ...baseOptions,
  tags: { cenario: 'login' },
};

// CT-PERF-01: Login na plataforma (US-0002) com massa de dados user1..user5
export default function () {
  const usuario = usuarios[(__VU - 1) % usuarios.length];
  // cookie jar novo a cada iteração: cada login começa sem sessão anterior
  const jar = new http.CookieJar();

  group('Abrir página Minha Conta', () => {
    const res = http.get(`${BASE_URL}/minha-conta/`, { jar, tags: { name: 'GET /minha-conta' } });
    check(res, {
      'minha conta - status 200': (r) => r.status === 200,
      'minha conta - formulário de login exibido': (r) => r.body.includes('woocommerce-login-nonce'),
    });

    const nonce = res.html().find('input[name="woocommerce-login-nonce"]').attr('value');
    // sem o formulário não há como autenticar: evita erro em cascata e registra a falha na métrica acima
    if (!nonce) return;

    group('Autenticar usuário', () => {
      const login = http.post(
        `${BASE_URL}/minha-conta/`,
        {
          username: usuario.username,
          password: usuario.password,
          'woocommerce-login-nonce': nonce,
          _wp_http_referer: '/minha-conta/',
          login: 'Login',
        },
        { jar, tags: { name: 'POST /minha-conta (login)' } },
      );

      check(login, {
        'login - status 200': (r) => r.status === 200,
        'login - usuário autenticado': (r) => r.body.includes(`Olá, <strong>${usuario.username}`),
      });
    });
  });

  sleep(1);
}

export const handleSummary = gerarRelatorio('login');
