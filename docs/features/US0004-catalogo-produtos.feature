# language: pt
Funcionalidade: [US-0004] Catálogo de Produtos
  Como cliente da EBAC-SHOP
  Quero navegar, buscar e visualizar os produtos do catálogo
  Para escolher o que desejo comprar

  # Regras de negócio:
  # - O catálogo deve exibir nome, imagem e preço de cada produto
  # - A busca deve retornar produtos cujo nome contenha o termo pesquisado
  # - Busca sem resultados deve exibir mensagem informativa
  # - Produtos sem estoque devem ser sinalizados e não podem ser comprados

  Cenário: Listar produtos do catálogo
    Quando eu acessar o catálogo de produtos
    Então devem ser exibidos os produtos com nome, imagem e preço

  Cenário: Buscar produto existente
    Quando eu buscar por "Hoodie"
    Então devem ser exibidos apenas produtos que contenham "Hoodie" no nome

  Cenário: Buscar produto inexistente
    Quando eu buscar por "produto-que-nao-existe"
    Então deve ser exibida a mensagem "Nenhum produto foi encontrado"

  Cenário: Visualizar detalhes de um produto
    Quando eu selecionar o produto "Abominable Hoodie"
    Então devem ser exibidos nome, preço, descrição, variações e o botão "Comprar"

  Cenário: Sinalizar combinação sem estoque
    Quando eu selecionar uma combinação de variações sem estoque
    Então deve ser exibida a mensagem "Desculpe, este produto não está disponível"
