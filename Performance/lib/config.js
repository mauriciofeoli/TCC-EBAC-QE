import { htmlReport } from 'https://raw.githubusercontent.com/benc-uk/k6-reporter/2.4.0/dist/bundle.js';
import { textSummary } from 'https://jslib.k6.io/k6-summary/0.0.2/index.js';

export const BASE_URL = __ENV.BASE_URL || 'http://lojaebac.ebaconline.art.br';

// Configuração exigida no TCC: 20 VUs, 2 minutos de execução, ramp-up de 20 segundos
export const options = {
  stages: [
    { duration: '20s', target: 20 },
    { duration: '1m30s', target: 20 },
    { duration: '10s', target: 0 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.05'],
    http_req_duration: ['p(95)<3000'],
    checks: ['rate>0.95'],
  },
};

export const gerarRelatorio = (nome) => (data) => ({
  [`reports/${nome}.html`]: htmlReport(data, { title: `k6 - ${nome}` }),
  [`reports/${nome}.json`]: JSON.stringify(data, null, 2),
  stdout: textSummary(data, { indent: ' ', enableColors: true }),
});
