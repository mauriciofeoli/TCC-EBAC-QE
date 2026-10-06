# language: pt
Funcionalidade: [US-0002] Login na plataforma
  Como cliente da EBAC-SHOP
  Quero fazer o login (autenticação) na plataforma
  Para visualizar meus pedidos

  Contexto:
    Dado que eu acesse a página "Minha Conta" da EBAC-SHOP

  Cenário: Login com usuário ativo e credenciais válidas
    Quando eu informar o usuário "aluno_ebac@teste.com" e a senha "teste@teste.com"
    E clicar em "Login"
    Então devo ser direcionado ao painel "Minha Conta"
    E deve ser exibida a saudação "Olá, aluno_ebac"

  Esquema do Cenário: Exibir mensagem de erro com credenciais inválidas
    Quando eu informar o usuário <usuario> e a senha <senha>
    E clicar em "Login"
    Então deve ser exibida a mensagem de erro <mensagem>

    Exemplos:
      | usuario                 | senha          | mensagem                              |
      | "aluno_ebac@teste.com"  | "senha_errada" | "A senha fornecida ... está incorreta" |
      | "inexistente@teste.com" | "qualquer123"  | "Endereço de e-mail desconhecido"      |
      | ""                      | ""             | "Nome de usuário é obrigatório"        |

  Cenário: Impedir login de usuário inativo
    Dado que o usuário "inativo@teste.com" esteja com o status inativo
    Quando eu informar suas credenciais válidas
    Então o login não deve ser realizado
    E deve ser exibida a mensagem "Usuário inativo"

  Esquema do Cenário: Bloquear o login após 3 tentativas com senha incorreta
    Quando eu errar a senha <tentativas> vezes consecutivas
    Então o login deve estar <situacao>

    Exemplos:
      | tentativas | situacao                         |
      | 2          | liberado                         |
      | 3          | bloqueado por 15 minutos         |

  Cenário: Liberar o login após o tempo de bloqueio
    Dado que meu login foi bloqueado por 3 tentativas incorretas
    Quando se passarem 15 minutos
    E eu informar as credenciais válidas
    Então devo ser autenticado com sucesso
