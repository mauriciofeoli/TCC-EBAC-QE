class ProdutoPage {
  visitar(slug) {
    cy.visit(`/product/${slug}/`);
  }

  titulo() {
    return cy.get('.product_title');
  }

  selecionarTamanho(tamanho) {
    cy.get('select[name="attribute_size"]').select(tamanho, { force: true });
  }

  selecionarCor(cor) {
    cy.get('select[name="attribute_color"]').select(cor, { force: true });
  }

  definirQuantidade(quantidade) {
    cy.get('input.qty').clear().type(String(quantidade));
  }

  botaoComprar() {
    return cy.get('.single_add_to_cart_button');
  }

  adicionarAoCarrinho() {
    this.botaoComprar().click();
  }

  aguardarVariacaoCarregada() {
    this.botaoComprar().should('not.have.class', 'wc-variation-selection-needed');
  }

  mensagemSucesso() {
    return cy.get('.woocommerce-message');
  }
}

export default new ProdutoPage();
