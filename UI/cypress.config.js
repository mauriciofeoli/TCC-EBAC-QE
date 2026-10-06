const { defineConfig } = require('cypress');

module.exports = defineConfig({
  reporter: 'cypress-mochawesome-reporter',
  reporterOptions: {
    reportDir: 'cypress/reports',
    reportFilename: 'ui-report',
    reportPageTitle: 'UI - EBAC Shop',
    charts: true,
    embeddedScreenshots: true,
    inlineAssets: true,
    saveAllAttempts: false,
  },
  e2e: {
    baseUrl: process.env.BASE_URL || 'http://lojaebac.ebaconline.art.br',
    specPattern: 'cypress/e2e/**/*.cy.js',
    supportFile: 'cypress/support/e2e.js',
    viewportWidth: 1366,
    viewportHeight: 768,
    defaultCommandTimeout: 15000,
    pageLoadTimeout: 90000,
    retries: { runMode: 1, openMode: 0 },
    video: false,
    chromeWebSecurity: false,
    setupNodeEvents(on, config) {
      require('cypress-mochawesome-reporter/plugin')(on);
      return config;
    },
  },
});
