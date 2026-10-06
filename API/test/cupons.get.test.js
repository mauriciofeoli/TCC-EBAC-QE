const { expect } = require('chai');
const { cuponsService } = require('../support/api');
const { novoCupom } = require('../support/factory');
const { cupomSchema, listaCuponsSchema, erroSchema } = require('../contracts/cupom.contract');

describe('US-0003 | API de Cupons - GET /wc/v3/coupons', () => {
  let cupomId;

  before(async () => {
    const { body } = await cuponsService.cadastrar(novoCupom());
    cupomId = body.id;
  });

  after(async () => {
    if (cupomId) await cuponsService.excluir(cupomId);
  });

  it('CT-API-01 - deve listar todos os cupons cadastrados (caminho feliz + contrato)', async () => {
    const res = await cuponsService.listar({ per_page: 10 });

    expect(res.status).to.equal(200);
    expect(res.body).to.be.an('array').that.is.not.empty;
    const { error } = listaCuponsSchema.validate(res.body);
    expect(error, error && error.message).to.be.undefined;
  });

  it('CT-API-02 - deve buscar um cupom pelo ID (caminho feliz + contrato)', async () => {
    const res = await cuponsService.buscarPorId(cupomId);

    expect(res.status).to.equal(200);
    expect(res.body.id).to.equal(cupomId);
    const { error } = cupomSchema.validate(res.body);
    expect(error, error && error.message).to.be.undefined;
  });

  it('CT-API-03 - deve retornar 404 ao buscar cupom com ID inexistente (alternativo)', async () => {
    const res = await cuponsService.buscarPorId(999999999);

    expect(res.status).to.equal(404);
    expect(res.body.code).to.equal('woocommerce_rest_shop_coupon_invalid_id');
    expect(erroSchema.validate(res.body).error).to.be.undefined;
  });

  it('CT-API-04 - deve retornar 401 ao listar cupons sem autenticação (negativo)', async () => {
    const res = await cuponsService.listarSemAutenticacao();

    expect(res.status).to.equal(401);
    expect(res.body.code).to.equal('woocommerce_rest_cannot_view');
    expect(erroSchema.validate(res.body).error).to.be.undefined;
  });
});
