# language: pt
Funcionalidade: [US-0003] API de cupons
  Como admin da EBAC-SHOP
  Quero criar um serviço de cupom
  Para poder listar e cadastrar os cupons

  Contexto:
    Dado que eu esteja autenticado na API com o usuário "admin_ebac" (Basic Auth)

  Cenário: Listar todos os cupons cadastrados
    Quando eu enviar um GET para "/wc/v3/coupons"
    Então o status da resposta deve ser 200
    E a resposta deve ser uma lista de cupons de acordo com o contrato

  Cenário: Buscar cupom pelo ID
    Dado que exista um cupom cadastrado
    Quando eu enviar um GET para "/wc/v3/coupons/{id}"
    Então o status da resposta deve ser 200
    E o cupom retornado deve ter o mesmo ID e seguir o contrato

  Cenário: Cadastrar cupom com os campos obrigatórios
    Quando eu enviar um POST para "/wc/v3/coupons" com:
      | code        | Ganhe10        |
      | amount      | 10.00          |
      | discount_type | fixed_product |
      | description | Cupom de teste |
    Então o status da resposta deve ser 201
    E o cupom criado deve seguir o contrato

  Cenário: Não permitir cadastrar cupom com código repetido
    Dado que já exista o cupom "Ganhe10"
    Quando eu enviar um POST com o código "Ganhe10"
    Então o status da resposta deve ser 400
    E a mensagem deve ser "O código de cupom já existe"

  Esquema do Cenário: Validar campos obrigatórios e inválidos
    Quando eu enviar um POST com <situacao>
    Então o status da resposta deve ser 400
    E o código de erro deve ser <erro>

    Exemplos:
      | situacao                         | erro                          |
      | o campo "code" ausente           | rest_missing_callback_param   |
      | "discount_type" inválido         | rest_invalid_param            |

  Cenário: Não permitir acesso sem autenticação
    Dado que eu não informe credenciais
    Quando eu enviar um GET para "/wc/v3/coupons"
    Então o status da resposta deve ser 401
