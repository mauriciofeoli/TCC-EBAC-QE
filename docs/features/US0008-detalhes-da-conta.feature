# language: pt
Funcionalidade: [US-0008] Detalhes da Conta
  Como cliente autenticado da EBAC-SHOP
  Quero alterar meus dados pessoais e minha senha
  Para manter minha conta atualizada e segura

  # Regras de negócio:
  # - Nome, sobrenome, nome de exibição e e-mail são obrigatórios
  # - Para alterar a senha é necessário informar a senha atual
  # - Nova senha e confirmação devem ser iguais

  Contexto:
    Dado que eu esteja autenticado
    E acesse "Detalhes da conta"

  Cenário: Alterar dados pessoais com sucesso
    Quando eu alterar o nome de exibição para "Mauricio QA"
    E clicar em "Salvar alterações"
    Então deve ser exibida a mensagem "Detalhes da conta modificados com sucesso"

  Cenário: Alterar senha informando a senha atual correta
    Quando eu informar a senha atual, a nova senha e a confirmação iguais
    E clicar em "Salvar alterações"
    Então a senha deve ser alterada com sucesso

  Cenário: Não alterar senha com confirmação diferente
    Quando eu informar a nova senha "Nova@123" e a confirmação "Nova@321"
    Então deve ser exibida a mensagem "As novas senhas não coincidem"

  Cenário: Não salvar com e-mail inválido
    Quando eu informar o e-mail "email-invalido"
    Então deve ser exibida a mensagem "Informe um endereço de e-mail válido"
