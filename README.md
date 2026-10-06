# TCC-EBAC-QE

Trabalho de conclusão do curso Engenheiro de Qualidade de Software da EBAC.

Aluno: Mauricio Ferreira de Oliveira

Projeto de testes da loja EBAC Shop (http://lojaebac.ebaconline.art.br).

## O que tem aqui

- `docs/` - documento do TCC (TCC-EBAC-QE.docx), mapa mental da estratégia, arquivos .feature e prints das execuções
- `UI/` - testes web com Cypress (login e carrinho)
- `API/` - testes da API de cupons com Supertest e validação de contrato com Joi
- `Mobile/` - testes do app iOS (catálogo de produtos) com WebdriverIO + Appium rodando no Sauce Labs
- `Performance/` - testes de carga com k6 (login e catálogo)
- `.github/workflows/` - pipelines do GitHub Actions

## Como rodar

Precisa ter o Node instalado (usei a versão 20).

API:

```
cd API
npm install
npm test
```

UI:

```
cd UI
npm install
npm test
```

Para abrir o Cypress na tela: `npx cypress open`

Performance (com o k6 instalado):

```
cd Performance
k6 run login.test.js
k6 run catalogo.test.js
```

Se não tiver o k6 dá pra rodar pelo Docker:

```
docker run --rm -v "$PWD/Performance:/scripts" -w /scripts grafana/k6 run login.test.js
```

Mobile: copiar o `Mobile/.env.example` para `Mobile/.env` e colocar o usuário e a access key do Sauce Labs. Depois:

```
cd Mobile
npm install
npm test
npm run report
```

Os testes usam o site online por padrão. Para usar a loja local no Docker é só subir os containers e mudar a variável `BASE_URL`:

```
docker network create --attachable ebac-network
docker run -d --name wp_db -p 3306:3306 --network ebac-network ernestosbarbosa/lojaebacdb:latest
docker run -d --name wp -p 80:80 --network ebac-network ernestosbarbosa/lojaebac:latest
```

## Relatórios

- API: `API/reports/api-report.html` (mochawesome)
- UI: `UI/cypress/reports/ui-report.html` (mochawesome)
- Performance: `Performance/reports/login.html` e `catalogo.html`
- Mobile: allure (`npm run report`) e os vídeos ficam no Sauce Labs

No GitHub Actions os relatórios ficam publicados em https://mauriciofeoli.github.io/TCC-EBAC-QE/

## CI

O `ci.yml` roda a cada push na main: primeiro API e UI, depois o k6 (se rodar tudo junto o servidor da loja não aguenta e os outros testes falham). No final publica os relatórios no GitHub Pages.

O job do k6 fica vermelho porque os tempos de resposta passam do limite que defini (p95 < 3s). Isso foi um problema encontrado no teste de performance e está explicado no documento, por isso ele não trava o pipeline.

O `mobile.yml` é rodado manualmente (Actions > Mobile - Sauce Labs > Run workflow) porque minha conta do Sauce é trial. Precisa dos secrets `SAUCE_USERNAME`, `SAUCE_ACCESS_KEY` e `SAUCE_APP`.

## Observações

- No mobile o teste de busca sem resultado (CT-MOB-04) passou. Os testes de listagem e busca (CT-MOB-02 e CT-MOB-03) estão feitos, mas no simulador do Sauce eles estouram o tempo. Expliquei o motivo no documento (seção 4.5).
- Alguns requisitos das histórias não estão funcionando na loja (limite de 10 itens, valor máximo de R$ 990, cupom automático e bloqueio do login depois de 3 tentativas). Deixei como teste manual e registrei como bug no documento.
