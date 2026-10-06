class CarrinhoPage {
  visitar() {
    cy.visit('/carrinho/');
  }

  linhasProduto() {
    return cy.get('.woocommerce-cart-form__cart-item, tr.cart_item');
  }

  quantidade() {
    return cy.get('.woocommerce-cart-form input.qty').first();
  }

  totalCarrinho() {
    return cy.get('.cart_totals .order-total .amount');
  }

  carrinhoVazio() {
    return cy.get('.cart-empty');
  }
}

export default new CarrinhoPage();
