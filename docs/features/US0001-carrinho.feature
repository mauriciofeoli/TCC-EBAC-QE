# language: pt
Funcionalidade: [US-0001] Adicionar item ao carrinho
  Como cliente da EBAC-SHOP
  Quero adicionar produtos no carrinho
  Para realizar a compra dos itens

  Contexto:
    Dado que eu acesse a página de um produto da EBAC-SHOP

  Cenário: Adicionar produto com variações válidas ao carrinho
    Quando eu selecionar tamanho "XS", cor "Red" e quantidade 2
    E clicar em "Comprar"
    Então deve ser exibida a mensagem de produto adicionado ao carrinho
    E o carrinho deve exibir o produto com quantidade 2 e o total calculado

  Esquema do Cenário: Validar o limite de 10 unidades do mesmo produto
    Quando eu adicionar <quantidade> unidades do mesmo produto ao carrinho
    Então o sistema deve <resultado>

    Exemplos:
      | quantidade | resultado                                                         |
      | 9          | adicionar os itens ao carrinho                                    |
      | 10         | adicionar os itens ao carrinho                                    |
      | 11         | bloquear a inclusão e exibir "Limite de 10 itens por produto"     |

  Esquema do Cenário: Validar o valor máximo de R$ 990,00 no carrinho
    Quando o total do carrinho for <valor>
    Então o sistema deve <resultado>

    Exemplos:
      | valor      | resultado                                                           |
      | R$ 989,99  | permitir finalizar a compra                                         |
      | R$ 990,00  | permitir finalizar a compra                                         |
      | R$ 990,01  | bloquear e exibir "O valor do carrinho não pode ultrapassar R$ 990" |

  Esquema do Cenário: Aplicar cupom de desconto conforme a faixa de valor
    Quando o total do carrinho for <valor>
    Então o cupom aplicado deve ser <cupom>

    Exemplos:
      | valor      | cupom          |
      | R$ 199,99  | nenhum         |
      | R$ 200,00  | 10% de desconto |
      | R$ 600,00  | 10% de desconto |
      | R$ 600,01  | 15% de desconto |

  Cenário: Tentar comprar sem selecionar as variações obrigatórias
    Quando eu clicar em "Comprar" sem selecionar tamanho e cor
    Então o produto não deve ser adicionado ao carrinho
