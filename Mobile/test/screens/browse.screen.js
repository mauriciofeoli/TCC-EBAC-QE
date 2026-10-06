class BrowseScreen {
  get titulo() {
    return $(`-ios predicate string:label == 'Browse'`);
  }

  get campoBusca() {
    return $('-ios class chain:**/XCUIElementTypeTextField');
  }

  get ordenar() {
    return $(`-ios predicate string:label CONTAINS 'Sort By'`);
  }

  get categoria() {
    return $(`-ios predicate string:label CONTAINS 'Category'`);
  }

  get precos() {
    return $$(`-ios predicate string:label CONTAINS 'R$'`);
  }

  get mensagemSemResultado() {
    return $(`-ios predicate string:label == 'No products found'`);
  }

  produtosComNome(nome) {
    return $$(`-ios predicate string:label BEGINSWITH '${nome}'`);
  }

  async aguardarProdutos() {
    await browser.waitUntil(async () => (await this.precos.length) > 0, {
      timeout: 60000,
      timeoutMsg: 'A lista de produtos não foi carregada.',
    });
  }

  async focarBusca() {
    if (await this.campoBusca.isExisting()) return;
    const { width, height } = await driver.getWindowSize();
    await driver.execute('mobile: tap', { x: Math.round(width * 0.5), y: Math.round(height * 0.171) });
    await this.campoBusca.waitForExist({ timeout: 30000 });
  }

  async buscar(termo) {
    await this.focarBusca();
    await this.campoBusca.clearValue();
    await this.campoBusca.setValue(termo);
  }
}

module.exports = new BrowseScreen();
