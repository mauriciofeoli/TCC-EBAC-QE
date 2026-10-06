import loginPage from '../page-objects/login.page';

// Login reaproveitado entre specs com cache de sessão
Cypress.Commands.add('login', (usuario, senha) => {
  cy.session([usuario, senha], () => {
    loginPage.visitar();
    loginPage.autenticar(usuario, senha);
    loginPage.saudacao().should('be.visible');
  });
});
