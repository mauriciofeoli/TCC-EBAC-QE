import 'cypress-mochawesome-reporter/register';
import './commands';

Cypress.on('uncaught:exception', () => false);
