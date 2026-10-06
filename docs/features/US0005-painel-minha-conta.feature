# language: pt
Funcionalidade: [US-0005] Painel Minha Conta
  Como cliente autenticado da EBAC-SHOP
  Quero acessar o painel "Minha Conta"
  Para gerenciar meus pedidos, endereços e dados pessoais

  # Regras de negócio:
  # - Somente usuários autenticados acessam o painel
  # - O painel deve exibir saudação com o nome do usuário
  # - O menu deve conter: Painel, Pedidos, Downloads, Endereços, Detalhes da conta e Sair

  Cenário: Exibir painel para usuário autenticado
    Dado que eu esteja autenticado
    Quando eu acessar "Minha Conta"
    Então deve ser exibida a saudação "Olá, <usuário>"
    E o menu com Painel, Pedidos, Downloads, Endereços, Detalhes da conta e Sair

  Cenário: Redirecionar visitante para o login
    Dado que eu não esteja autenticado
    Quando eu acessar "Minha Conta"
    Então deve ser exibido o formulário de login

  Cenário: Navegar pelos links do painel
    Dado que eu esteja autenticado
    Quando eu clicar em "Pedidos"
    Então devo ser direcionado para a página de pedidos

  Cenário: Encerrar a sessão
    Dado que eu esteja autenticado
    Quando eu clicar em "Sair"
    Então a sessão deve ser encerrada
    E deve ser exibido o formulário de login
