import 'cypress-mochawesome-reporter/register';
import './commands';

// Scripts de terceiros da loja (tema/plugins) às vezes lançam erros que não fazem parte do escopo dos testes
Cypress.on('uncaught:exception', () => false);
