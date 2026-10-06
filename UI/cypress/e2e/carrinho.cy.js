import produtoPage from '../page-objects/produto.page';
import carrinhoPage from '../page-objects/carrinho.page';
import { adicionarProdutoAoCarrinho, precoEmNumero } from '../app-actions/carrinho.actions';

describe('US-0001 | Adicionar item ao carrinho', () => {
  let produto;
  let produtoSemEstoque;

  before(() => {
    cy.fixture('produtos').then((dados) => {
      produto = dados.hoodie;
      produtoSemEstoque = dados.hoodieSemEstoque;
    });
  });

  it('CT-CARR-01 - deve adicionar produto com tamanho, cor e quantidade ao carrinho (caminho feliz)', () => {
    adicionarProdutoAoCarrinho(produto, 2);

    produtoPage.mensagemSucesso()
      .should('be.visible')
      .and('contain', produto.nome)
      .and('contain', 'adicionados no seu carrinho');

    carrinhoPage.visitar();
    carrinhoPage.linhasProduto().should('have.length', 1).and('contain', produto.nome);
    carrinhoPage.quantidade().should('have.value', '2');
  });

  it('CT-CARR-02 - deve calcular o total do carrinho conforme preço x quantidade (caminho feliz)', () => {
    adicionarProdutoAoCarrinho(produto, 3);
    carrinhoPage.visitar();

    cy.get('.cart_item .product-price .amount').first().invoke('text').then((precoTexto) => {
      const esperado = precoEmNumero(precoTexto) * 3;
      cy.get('.cart_item .product-subtotal .amount').first().invoke('text')
        .then((subtotal) => expect(precoEmNumero(subtotal)).to.be.closeTo(esperado, 0.01));
    });
  });

  it('CT-CARR-03 - não deve permitir comprar sem selecionar as variações do produto (alternativo)', () => {
    produtoPage.visitar(produto.slug);

    produtoPage.botaoComprar().should('have.class', 'disabled');
    produtoPage.adicionarAoCarrinho();
    produtoPage.mensagemSucesso().should('not.exist');
  });

  it('CT-CARR-04 - não deve adicionar combinação de variação sem estoque (negativo)', () => {
    const alerta = cy.stub().as('alerta');
    cy.on('window:alert', alerta);

    adicionarProdutoAoCarrinho(produtoSemEstoque, 1);

    cy.get('@alerta').should('have.been.calledWithMatch', /não está disponível/);
    produtoPage.mensagemSucesso().should('not.exist');
  });

  it('CT-CARR-05 - deve manter o carrinho vazio quando nenhum produto foi adicionado (alternativo)', () => {
    carrinhoPage.visitar();

    carrinhoPage.carrinhoVazio().should('be.visible');
  });
});
