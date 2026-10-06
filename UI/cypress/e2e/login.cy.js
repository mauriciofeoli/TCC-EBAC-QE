import loginPage from '../page-objects/login.page';

describe('US-0002 | Login na plataforma', () => {
  let usuarios;

  before(() => {
    cy.fixture('usuarios').then((dados) => {
      usuarios = dados;
    });
  });

  beforeEach(() => {
    loginPage.visitar();
  });

  it('CT-LOGIN-01 - deve autenticar com usuário e senha válidos (caminho feliz)', () => {
    const { usuario, senha, nomeExibido } = usuarios.valido;

    loginPage.autenticar(usuario, senha);

    loginPage.saudacao().should('contain', `Olá, ${nomeExibido}`);
    cy.contains('a', 'Pedidos').should('be.visible');
  });

  it('CT-LOGIN-02 - deve exibir mensagem de erro com senha inválida (alternativo)', () => {
    const { usuario, senha } = usuarios.senhaInvalida;

    loginPage.autenticar(usuario, senha);

    loginPage.mensagemErro()
      .should('be.visible')
      .and('contain', `A senha fornecida para o e-mail ${usuario} está incorreta`);
  });

  it('CT-LOGIN-03 - deve exibir mensagem de erro com usuário inexistente (negativo)', () => {
    const { usuario, senha } = usuarios.inexistente;

    loginPage.autenticar(usuario, senha);

    loginPage.mensagemErro().should('be.visible');
    loginPage.saudacao().should('not.exist');
  });

  it('CT-LOGIN-04 - não deve autenticar com campos obrigatórios vazios (negativo)', () => {
    loginPage.botaoLogin().click();

    loginPage.mensagemErro().should('be.visible').and('contain', 'Erro');
  });
});
