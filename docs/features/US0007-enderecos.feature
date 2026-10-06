# language: pt
Funcionalidade: [US-0007] Endereços
  Como cliente autenticado da EBAC-SHOP
  Quero cadastrar e editar meus endereços de faturamento e entrega
  Para agilizar a finalização das compras

  # Regras de negócio:
  # - Campos obrigatórios: nome, sobrenome, país, endereço, cidade, estado, CEP, telefone e e-mail (faturamento)
  # - CEP deve ter 8 dígitos numéricos
  # - Após salvar, deve ser exibida mensagem de sucesso

  Contexto:
    Dado que eu esteja autenticado
    E acesse "Endereços"

  Cenário: Cadastrar endereço de faturamento válido
    Quando eu preencher todos os campos obrigatórios com dados válidos
    E clicar em "Salvar endereço"
    Então deve ser exibida a mensagem "Endereço alterado com sucesso"

  Esquema do Cenário: Validar campos obrigatórios
    Quando eu deixar o campo <campo> vazio
    E clicar em "Salvar endereço"
    Então deve ser exibida a mensagem "<campo> é um campo obrigatório"

    Exemplos:
      | campo    |
      | Nome     |
      | CEP      |
      | Telefone |

  Esquema do Cenário: Validar formato do CEP
    Quando eu informar o CEP <cep>
    Então o endereço deve ser <resultado>

    Exemplos:
      | cep        | resultado |
      | 01310-100  | salvo     |
      | 0131010    | rejeitado |
      | ABCDE-FGH  | rejeitado |

  Cenário: Editar endereço de entrega
    Dado que eu possua endereço de entrega cadastrado
    Quando eu alterar a cidade para "Campinas" e salvar
    Então o endereço de entrega deve exibir a cidade "Campinas"
