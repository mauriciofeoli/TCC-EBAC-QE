const { expect } = require('chai');
const { cuponsService } = require('../support/api');
const { novoCupom } = require('../support/factory');
const { cupomSchema, erroSchema } = require('../contracts/cupom.contract');

describe('US-0003 | API de Cupons - POST /wc/v3/coupons', () => {
  const criados = [];

  after(async () => {
    await Promise.all(criados.filter(Boolean).map((id) => cuponsService.excluir(id)));
  });

  it('CT-API-05 - deve cadastrar cupom com os campos obrigatórios (caminho feliz + contrato)', async () => {
    const cupom = novoCupom();
    const res = await cuponsService.cadastrar(cupom);
    criados.push(res.body.id);

    expect(res.status).to.equal(201);
    expect(res.body.code).to.equal(cupom.code.toLowerCase());
    expect(res.body.amount).to.equal('10.00');
    expect(res.body.discount_type).to.equal('fixed_product');
    expect(res.body.description).to.equal('Cupom de teste');
    const { error } = cupomSchema.validate(res.body);
    expect(error, error && error.message).to.be.undefined;
  });

  it('CT-API-06 - não deve permitir cadastrar cupom com código repetido (alternativo)', async () => {
    const cupom = novoCupom();
    const primeiro = await cuponsService.cadastrar(cupom);
    criados.push(primeiro.body.id);

    const res = await cuponsService.cadastrar(cupom);

    expect(res.status).to.equal(400);
    expect(res.body.code).to.equal('woocommerce_rest_coupon_code_already_exists');
    expect(erroSchema.validate(res.body).error).to.be.undefined;
  });

  it('CT-API-07 - não deve cadastrar cupom sem o código (negativo)', async () => {
    const { code, ...semCodigo } = novoCupom();
    const res = await cuponsService.cadastrar(semCodigo);

    expect(res.status).to.equal(400);
    expect(res.body.code).to.equal('rest_missing_callback_param');
    expect(res.body.data.params).to.include('code');
  });

  it('CT-API-08 - não deve cadastrar cupom com tipo de desconto inválido (negativo)', async () => {
    const res = await cuponsService.cadastrar(novoCupom({ discount_type: 'desconto_invalido' }));

    expect(res.status).to.equal(400);
    expect(res.body.code).to.equal('rest_invalid_param');
    expect(res.body.data.params).to.have.property('discount_type');
  });
});
