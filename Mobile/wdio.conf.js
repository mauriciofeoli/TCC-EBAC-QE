require('dotenv').config();
const fs = require('fs');

const obrigatorias = ['SAUCE_USERNAME', 'SAUCE_ACCESS_KEY', 'SAUCE_APP'];
const ausentes = obrigatorias.filter((nome) => !process.env[nome]);
if (ausentes.length) {
  throw new Error(`Variáveis de ambiente ausentes: ${ausentes.join(', ')} (veja Mobile/.env.example)`);
}

exports.config = {
  runner: 'local',
  user: process.env.SAUCE_USERNAME,
  key: process.env.SAUCE_ACCESS_KEY,
  region: process.env.SAUCE_REGION || 'us',
  services: ['sauce'],

  specs: ['./test/specs/**/*.spec.js'],
  maxInstances: 1,

  capabilities: [
    {
      platformName: 'iOS',
      'appium:deviceName': process.env.SAUCE_DEVICE_NAME || 'iPhone Simulator',
      'appium:platformVersion': process.env.SAUCE_PLATFORM_VERSION || '17.0',
      'appium:automationName': 'XCUITest',
      'appium:app': process.env.SAUCE_APP,
      'appium:newCommandTimeout': 240,
      'appium:waitForIdleTimeout': 0,
      'appium:reduceMotion': true,
      'appium:settings[customSnapshotTimeout]': 15,
      'appium:settings[animationCoolOffTimeout]': 0,
      'sauce:options': {
        build: process.env.SAUCE_BUILD || `TCC-EBAC-QE mobile - ${process.env.GITHUB_RUN_NUMBER || 'local'}`,
        name: 'Catálogo de Produtos - iOS',
      },
    },
  ],

  logLevel: 'warn',
  waitforTimeout: 20000,
  connectionRetryTimeout: 180000,
  connectionRetryCount: 2,

  framework: 'mocha',
  mochaOpts: { ui: 'bdd', timeout: 300000 },

  reporters: [
    'spec',
    ['allure', { outputDir: 'allure-results', disableWebdriverStepsReporting: true }],
  ],

  onPrepare: () => fs.mkdirSync('reports', { recursive: true }),

  afterTest: async function (test, context, { passed }) {
    if (!passed) await browser.takeScreenshot();
  },
};
