const homeScreen = require('../screens/home.screen');
const browseScreen = require('../screens/browse.screen');

describe('US-0004 | Catálogo de Produtos (app iOS)', () => {
  before(async () => {
    // o app tem animações contínuas: sem isso o XCUITest espera "ociosidade" a cada comando
    await driver.updateSettings({ waitForIdleTimeout: 0, animationCoolOffTimeout: 0, customSnapshotTimeout: 15 });
  });

  it('CT-MOB-02 - deve listar produtos com nome e preço na aba Browse (caminho feliz)', async () => {
    await homeScreen.irParaBrowse();
    await browseScreen.aguardarProdutos();

    await expect(browseScreen.titulo).toExist();
    await expect(browseScreen.ordenar).toExist();
    await expect(browseScreen.categoria).toExist();
    await expect(browseScreen.produtosComNome('Camiseta EBAC')).toBeElementsArrayOfSize({ gte: 1 });
    expect(await browseScreen.precos.length).toBeGreaterThan(0);
  });

  it('CT-MOB-03 - deve buscar um produto existente pelo nome (caminho feliz)', async () => {
    await homeScreen.irParaBrowse();
    await browseScreen.buscar('Tênis');

    await browser.waitUntil(async () => (await browseScreen.produtosComNome('Camiseta').length) === 0, {
      timeout: 30000,
      timeoutMsg: 'A busca não filtrou a lista de produtos.',
    });
    await expect(browseScreen.produtosComNome('Tênis')).toBeElementsArrayOfSize({ gte: 1 });
  });

  it('CT-MOB-04 - deve informar que nenhum produto foi encontrado (alternativo)', async () => {
    await homeScreen.irParaBrowse();
    await browseScreen.buscar('zzzprodutoinexistente');

    await expect(browseScreen.mensagemSemResultado).toBeDisplayed({ wait: 30000 });
    expect(await browseScreen.precos.length).toBe(0);
    await driver.saveScreenshot('./reports/busca-sem-resultado.png');
  });
});
