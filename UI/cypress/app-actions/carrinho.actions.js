import produtoPage from '../page-objects/produto.page';

// App Actions: atalhos de fluxo reaproveitados pelos specs
export const adicionarProdutoAoCarrinho = ({ slug, tamanho, cor }, quantidade = 1) => {
  produtoPage.visitar(slug);
  produtoPage.selecionarTamanho(tamanho);
  produtoPage.selecionarCor(cor);
  produtoPage.aguardarVariacaoCarregada();
  produtoPage.definirQuantidade(quantidade);
  produtoPage.adicionarAoCarrinho();
};

export const precoEmNumero = (texto) =>
  Number(texto.replace(/[^\d,]/g, '').replace(',', '.'));
