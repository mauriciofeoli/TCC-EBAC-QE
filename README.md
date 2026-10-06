# TCC-EBAC-QE – Engenheiro de Qualidade de Software

Trabalho de Conclusão de Curso da formação **Profissão: Engenheiro de Qualidade de Software (EBAC)**.
Autor: **Mauricio Ferreira de Oliveira** – São Paulo, 2026.

Estratégia de testes, critérios de aceitação, casos de teste e automação (UI, API, Mobile e Performance) do e-commerce **EBAC Shop** (`http://lojaebac.ebaconline.art.br`).

📄 Documento do TCC: [`docs/TCC-EBAC-QE.docx`](docs/TCC-EBAC-QE.docx)
🧠 Mapa mental da estratégia: [`docs/estrategia-mapa-mental.png`](docs/estrategia-mapa-mental.png)
🥒 Critérios de aceitação (Gherkin): [`docs/features`](docs/features)

## Estrutura

| Pasta | Conteúdo | Ferramentas | Testing Pattern | Relatório |
|---|---|---|---|---|
| `UI/` | US-0001 Carrinho e US-0002 Login | Cypress 13 (JavaScript) | Page Objects + App Actions + Custom Commands | Mochawesome (`UI/cypress/reports/ui-report.html`) |
| `API/` | US-0003 API de Cupons | Supertest + Mocha + Chai + Joi | Service Object + Data Factory + validação de contrato | Mochawesome (`API/reports/api-report.html`) |
| `Mobile/` | Catálogo de Produtos (app iOS EBAC Store) | WebdriverIO 9 + Appium (XCUITest) no Sauce Labs | Screen Objects (Page Objects) | Allure (`Mobile/allure-report`) |
| `Performance/` | Login e Catálogo | k6 | Configuração compartilhada + massa em `SharedArray` | k6-reporter (`Performance/reports/*.html`) |
| `.github/workflows/` | CI | GitHub Actions + GitHub Pages | – | Pages + artefatos |

## Pré-requisitos

- Node.js 20+
- Docker (opcional – para rodar o k6 sem instalá-lo ou subir a loja localmente)
- Conta no Sauce Labs (Mobile)

## Como executar

```bash
# API
cd API && npm install && npm test

# UI
cd UI && npm install && npm test          # headless
cd UI && npm run cy:open                   # modo interativo

# Performance (k6 instalado)
cd Performance && k6 run login.test.js && k6 run catalogo.test.js
# ou via Docker
docker run --rm -u root -v "$PWD/Performance:/scripts" -w /scripts grafana/k6 run login.test.js

# Mobile (Sauce Labs) – copie Mobile/.env.example para Mobile/.env e preencha
cd Mobile && npm install && npm test && npm run report
```

Todos os projetos aceitam a variável `BASE_URL` (padrão: `http://lojaebac.ebaconline.art.br`).

### Ambiente local com Docker (alternativo)

```bash
docker network create --attachable ebac-network
docker run -d --name wp_db -p 3306:3306 --network ebac-network ernestosbarbosa/lojaebacdb:latest
docker run -d --name wp -p 80:80 --network ebac-network ernestosbarbosa/lojaebac:latest
BASE_URL=http://localhost npm test
```

## Integração contínua

- **`ci.yml`** – a cada push/PR na `main` executa API, UI e Performance em paralelo, publica os relatórios como artefatos e no **GitHub Pages**.
- **`mobile.yml`** – executa os testes mobile no Sauce Labs (push em `Mobile/**` ou manual).

Configuração necessária no repositório:
1. *Settings → Pages → Source*: **GitHub Actions**.
2. *Settings → Secrets and variables → Actions*: `SAUCE_USERNAME`, `SAUCE_ACCESS_KEY`, `SAUCE_APP`.

## Casos de teste automatizados

| ID | Caso | Tipo | Projeto |
|---|---|---|---|
| CT-LOGIN-01 | Login com credenciais válidas | Feliz | UI |
| CT-LOGIN-02 | Senha inválida exibe erro | Alternativo | UI |
| CT-LOGIN-03 | Usuário inexistente exibe erro | Negativo | UI |
| CT-LOGIN-04 | Campos vazios exibem erro | Negativo | UI |
| CT-CARR-01 | Adicionar produto com variações | Feliz | UI |
| CT-CARR-02 | Total = preço × quantidade | Feliz | UI |
| CT-CARR-03 | Comprar sem selecionar variações | Alternativo | UI |
| CT-CARR-04 | Variação sem estoque | Negativo | UI |
| CT-CARR-05 | Carrinho vazio | Alternativo | UI |
| CT-API-01..04 | GET cupons (lista, por ID, 404, 401) + contrato | Feliz/Alternativo/Negativo | API |
| CT-API-05..08 | POST cupons (criar, duplicado, sem code, tipo inválido) + contrato | Feliz/Alternativo/Negativo | API |
| CT-MOB-01..04 | Catálogo: listar, categorias, busca, sem resultado | Feliz/Alternativo | Mobile |
| CT-PERF-01 | Login com 20 VUs / 2 min / ramp-up 20 s | Carga | Performance |
| CT-PERF-02 | Navegação no catálogo com 20 VUs / 2 min / ramp-up 20 s | Carga | Performance |
