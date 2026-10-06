# language: pt
Funcionalidade: [US-0006] Meus Pedidos
  Como cliente autenticado da EBAC-SHOP
  Quero consultar meus pedidos
  Para acompanhar o status das minhas compras

  # Regras de negócio:
  # - A lista deve exibir número, data, status, total e ações de cada pedido
  # - O cliente só visualiza os próprios pedidos
  # - Sem pedidos, deve ser exibida mensagem e link para a loja

  Contexto:
    Dado que eu esteja autenticado

  Cenário: Listar pedidos do cliente
    Dado que eu possua pedidos realizados
    Quando eu acessar "Pedidos"
    Então devem ser exibidos número, data, status, total e o botão "Visualizar"

  Cenário: Visualizar detalhes de um pedido
    Quando eu clicar em "Visualizar" em um pedido
    Então devem ser exibidos os produtos, quantidades, valores e endereços do pedido

  Cenário: Cliente sem pedidos
    Dado que eu não possua pedidos
    Quando eu acessar "Pedidos"
    Então deve ser exibida a mensagem "Nenhum pedido foi feito ainda"

  Cenário: Impedir acesso a pedido de outro cliente
    Quando eu acessar a URL de um pedido que não é meu
    Então o pedido não deve ser exibido
    E deve ser exibida mensagem de pedido inválido
