class LoginPage {
  visitar() {
    cy.visit('/minha-conta/');
  }

  campoUsuario() {
    return cy.get('#username');
  }

  campoSenha() {
    return cy.get('#password');
  }

  botaoLogin() {
    return cy.get('button[name="login"], input[name="login"]').first();
  }

  autenticar(usuario, senha) {
    this.campoUsuario().clear().type(usuario);
    this.campoSenha().clear().type(senha, { log: false });
    this.botaoLogin().click();
  }

  saudacao() {
    return cy.get('.woocommerce-MyAccount-content');
  }

  mensagemErro() {
    return cy.get('.woocommerce-error');
  }
}

export default new LoginPage();
