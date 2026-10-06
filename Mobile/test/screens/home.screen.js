// posição horizontal (fração da largura) de cada aba na barra inferior fixa do app
const ABAS = { Home: 0.125, Browse: 0.375, Order: 0.625, Profile: 0.875 };

class HomeScreen {
  get titulo() {
    return $(`-ios predicate string:label == 'EBAC Store'`);
  }

  get categorias() {
    return $$(`-ios predicate string:label == 'Bags'`);
  }

  aba(nome) {
    return $(`~tab-${nome}`);
  }

  // a Home tem uma árvore de acessibilidade grande e às vezes o snapshot do XCUITest não devolve
  // a barra de abas; nesse caso toca na posição fixa da aba
  async tocarAba(nome) {
    try {
      await this.aba(nome).click();
    } catch {
      const { width, height } = await driver.getWindowSize();
      await driver.execute('mobile: tap', { x: Math.round(width * ABAS[nome]), y: Math.round(height * 0.925) });
    }
  }

  async abrir() {
    await this.tocarAba('Home');
    await this.titulo.waitForExist({ timeout: 60000 });
  }

  async irParaBrowse() {
    await this.tocarAba('Browse');
  }
}

module.exports = new HomeScreen();
