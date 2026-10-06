"""Conteúdo textual do TCC (consumido por gerar_tcc.py)."""

AUTOR = 'Mauricio Ferreira de Oliveira'
CIDADE = 'São Paulo'
ANO = '2026'
REPO = 'https://github.com/mauriciofeoli/TCC-EBAC-QE'

RESUMO = (
    'Este trabalho apresenta o planejamento e a execução da estratégia de qualidade para o e-commerce EBAC Shop, '
    'seguindo o fluxo de trabalho de um Quality Engineer em um time ágil. A partir das histórias de usuário de '
    'carrinho, login e API de cupons, e de cinco novas histórias (Catálogo de Produtos, Painel Minha Conta, Meus '
    'Pedidos, Endereços e Detalhes da Conta), foram definidos uma estratégia de testes em mapa mental, critérios de '
    'aceitação em Gherkin e casos de teste com técnicas de partição de equivalência, valor limite e tabela de decisão. '
    'Os casos priorizados foram automatizados em quatro frentes: interface web com Cypress e Page Objects, API com '
    'Supertest e validação de contratos com Joi, aplicativo mobile com WebdriverIO e Appium no Sauce Labs e '
    'performance com k6 (20 usuários virtuais, 2 minutos e ramp-up de 20 segundos). Todos os testes geram relatórios '
    'e rodam em integração contínua no GitHub Actions, com publicação no GitHub Pages. A execução revelou defeitos '
    'em regras de negócio não implementadas (limite de itens, valor máximo e cupom automático no carrinho e bloqueio '
    'de login após três tentativas) e degradação de desempenho sob carga, evidenciando o valor da combinação entre '
    'testes manuais, automação e análise de resultados.'
)

INTRODUCAO = [
    'A qualidade de software deixou de ser uma etapa isolada no fim do desenvolvimento e passou a acompanhar todo o '
    'ciclo de vida do produto. Em times ágeis, o Engenheiro de Qualidade (Quality Engineer – QE) participa desde o '
    'refinamento das histórias, ajudando a esclarecer regras de negócio e critérios de aceitação, até a entrega, '
    'garantindo que as funcionalidades sejam validadas de forma rápida, repetível e rastreável.',
    'O cenário deste trabalho é a EBAC Shop, uma loja virtual construída em WordPress/WooCommerce, disponível em '
    'ambiente web, com uma API REST para administração de cupons e um aplicativo mobile de catálogo. O objetivo é '
    'aplicar os conhecimentos da formação para definir e executar uma estratégia de testes adequada a esse contexto, '
    'considerando as histórias de usuário já refinadas pelo time: adicionar item ao carrinho (US-0001), login na '
    'plataforma (US-0002) e API de cupons (US-0003), além de novas histórias criadas para as funcionalidades de '
    'catálogo e da área do cliente.',
    'Ao longo do documento são apresentados a estratégia de testes em formato de mapa mental, os critérios de '
    'aceitação escritos em Gherkin, os casos de teste derivados com técnicas de teste, o repositório com o código-fonte, '
    'as automações de UI, API e mobile com seus relatórios, a integração contínua com GitHub Actions e os testes de '
    'performance com k6, com a análise dos resultados obtidos. Espera-se, com isso, demonstrar o fluxo completo de '
    'trabalho de um QE – do planejamento à entrega – e registrar os defeitos e riscos identificados no produto.',
]

PROJETO = [
    'Para este trabalho de conclusão de curso foi elaborada uma estratégia de testes para validar o e-commerce EBAC '
    'Shop (http://lojaebac.ebaconline.art.br), considerando as histórias de usuário como se o autor fizesse parte de '
    'um time ágil. Como base, foi utilizado o Trabalho de Consolidação do Módulo 19 (estratégia de testes com '
    'automação priorizada nas camadas de API e com E2E enxuto para fluxos críticos), além das atividades práticas '
    'desenvolvidas nos módulos anteriores (Cypress, Supertest, WebdriverIO/Appium, k6 e GitHub Actions).',
    'Os ambientes considerados na estratégia foram:',
]

PROJETO_AMBIENTES = [
    ('Ambiente online (principal): ', 'http://lojaebac.ebaconline.art.br – utilizado na execução local e no CI.'),
    ('Ambiente local (alternativo): ', 'imagens Docker ernestosbarbosa/lojaebacdb e ernestosbarbosa/lojaebac, '
     'publicadas em http://localhost:80; todos os projetos aceitam a variável BASE_URL para apontar para esse ambiente.'),
    ('Nuvem mobile: ', 'Sauce Labs (simuladores iOS), dispensando emuladores locais e permitindo a execução no CI.'),
]

ESTRATEGIA_TEXTO = [
    'A estratégia foi construída a partir das diretrizes do Módulo 5 e do Trabalho de Consolidação (Módulo 19). '
    'Seguindo a pirâmide de testes, a maior parte das validações automatizadas fica na camada de API (mais rápida e '
    'estável), enquanto a interface web e o aplicativo recebem testes E2E apenas para os fluxos críticos. Regras de '
    'negócio que exigem observação humana, ou que ainda não estão implementadas, são cobertas por testes manuais e '
    'exploratórios. A Tabela 1 resume a estratégia e a Figura 1 apresenta o mapa mental.',
]

ESTRATEGIA_TABELA = [
    ['Objetivos', 'Validar as histórias US-0001 a US-0008, garantir as regras de negócio, reduzir regressões por meio de automação e dar feedback rápido a cada alteração (CI).'],
    ['Papéis e responsabilidades', 'QE: estratégia, critérios, casos de teste, automação, relatórios e reporte de bugs. Devs: testes unitários e correções. PO: definição e aceite dos critérios. Scrum Master: remoção de impedimentos.'],
    ['Fases e níveis', 'Refinamento (3 Amigos e Gherkin) → testes unitários (dev) → integração/API → sistema/E2E → aceitação com o PO → regressão automatizada no CI.'],
    ['Tipos de teste', 'Funcional, contrato de API, regressão, performance (carga), mobile, exploratório e usabilidade.'],
    ['Técnicas', 'Partição de equivalência, análise de valor limite, tabela de decisão, fluxos feliz, alternativo e negativo.'],
    ['Abordagem', 'Manual para exploratórios e regras ainda não implementadas; automatizada para fluxos críticos e regressão; shift-left com critérios definidos antes do desenvolvimento.'],
    ['Plataformas', 'Web (loja WooCommerce), API REST (/wp-json/wc/v3/coupons) e mobile (aplicativo iOS EBAC Store).'],
    ['Ferramentas / frameworks', 'UI: Cypress 13 (JavaScript). API: Supertest + Mocha + Chai + Joi. Mobile: WebdriverIO 9 + Appium XCUITest. Performance: k6. Relatórios: Mochawesome, Allure e k6-reporter. CI: GitHub Actions + GitHub Pages.'],
    ['Padrões', 'Gherkin em português, casos com ID rastreável à história, Page Objects/Screen Objects, App Actions, Service Object, Data Factory e massa de dados isolada em fixtures.'],
    ['Ambientes', 'Online (lojaebac.ebaconline.art.br), local via Docker e Sauce Labs para mobile.'],
    ['Critérios de saída', '100% dos casos automatizados críticos aprovados, defeitos registrados com evidência e relatórios publicados.'],
]

CRITERIOS_INTRO = (
    'Para cada história foram definidos critérios de aceitação em Gherkin (em português), incluindo esquemas de cenário '
    'com exemplos que já aplicam valores limite. Além das histórias US-0001 a US-0003, foram criadas as histórias '
    'US-0004 a US-0008 para as funcionalidades de Catálogo de Produtos, Painel Minha Conta, Meus Pedidos, Endereços e '
    'Detalhes da Conta. Os arquivos .feature também estão disponíveis em docs/features no repositório.'
)

HISTORIAS = [
    {'titulo': '[US-0001] – Adicionar item ao carrinho', 'feature': 'US0001-carrinho.feature'},
    {'titulo': '[US-0002] – Login na plataforma', 'feature': 'US0002-login.feature'},
    {'titulo': '[US-0003] – API de cupons', 'feature': 'US0003-api-cupons.feature'},
    {'titulo': '[US-0004] – Catálogo de Produtos', 'feature': 'US0004-catalogo-produtos.feature', 'nova': True,
     'como': 'cliente da EBAC-SHOP', 'quero': 'navegar, buscar e visualizar os produtos do catálogo',
     'para': 'escolher o que desejo comprar',
     'regras': ['O catálogo deve exibir nome, imagem e preço de cada produto;',
                'A busca deve retornar produtos cujo nome contenha o termo pesquisado;',
                'Busca sem resultados deve exibir mensagem informativa;',
                'Produtos sem estoque devem ser sinalizados e não podem ser comprados.']},
    {'titulo': '[US-0005] – Painel Minha Conta', 'feature': 'US0005-painel-minha-conta.feature', 'nova': True,
     'como': 'cliente autenticado da EBAC-SHOP', 'quero': 'acessar o painel "Minha Conta"',
     'para': 'gerenciar meus pedidos, endereços e dados pessoais',
     'regras': ['Somente usuários autenticados acessam o painel;',
                'O painel deve exibir saudação com o nome do usuário;',
                'O menu deve conter Painel, Pedidos, Downloads, Endereços, Detalhes da conta e Sair.']},
    {'titulo': '[US-0006] – Meus Pedidos', 'feature': 'US0006-meus-pedidos.feature', 'nova': True,
     'como': 'cliente autenticado da EBAC-SHOP', 'quero': 'consultar meus pedidos',
     'para': 'acompanhar o status das minhas compras',
     'regras': ['A lista deve exibir número, data, status, total e ações de cada pedido;',
                'O cliente só visualiza os próprios pedidos;',
                'Sem pedidos, deve ser exibida mensagem e link para a loja.']},
    {'titulo': '[US-0007] – Endereços', 'feature': 'US0007-enderecos.feature', 'nova': True,
     'como': 'cliente autenticado da EBAC-SHOP', 'quero': 'cadastrar e editar meus endereços de faturamento e entrega',
     'para': 'agilizar a finalização das compras',
     'regras': ['Campos obrigatórios: nome, sobrenome, país, endereço, cidade, estado, CEP, telefone e e-mail (faturamento);',
                'O CEP deve ter 8 dígitos numéricos;',
                'Após salvar, deve ser exibida mensagem de sucesso.']},
    {'titulo': '[US-0008] – Detalhes da Conta', 'feature': 'US0008-detalhes-da-conta.feature', 'nova': True,
     'como': 'cliente autenticado da EBAC-SHOP', 'quero': 'alterar meus dados pessoais e minha senha',
     'para': 'manter minha conta atualizada e segura',
     'regras': ['Nome, sobrenome, nome de exibição e e-mail são obrigatórios;',
                'Para alterar a senha é necessário informar a senha atual;',
                'Nova senha e confirmação devem ser iguais.']},
]

CASOS_INTRO = [
    'Os casos de teste foram derivados dos critérios de aceitação aplicando as técnicas de partição de equivalência '
    '(PE), análise de valor limite (VL) e tabela de decisão (TD), contemplando o fluxo principal (caminho feliz), '
    'fluxos alternativos e negativos. A coluna "Autom." indica os casos automatizados (S) e os executados '
    'manualmente (N). Os IDs são os mesmos usados nos testes automatizados, garantindo rastreabilidade.',
    'Pré-condição comum às histórias da área do cliente: usuário cadastrado e autenticado (aluno_ebac@teste.com).',
]

CASOS = [
    {'us': 'US-0001 – Adicionar item ao carrinho', 'casos': [
        ['CT-CARR-01', 'Acessar Abominable Hoodie, selecionar XS/Red, quantidade 2 e clicar em Comprar', 'PE (classe válida)', 'Mensagem de sucesso; carrinho com o produto e quantidade 2', 'Feliz', 'S'],
        ['CT-CARR-02', 'Adicionar 3 unidades e acessar o carrinho', 'PE', 'Subtotal = preço unitário × 3', 'Feliz', 'S'],
        ['CT-CARR-03', 'Clicar em Comprar sem selecionar tamanho e cor', 'PE (classe inválida)', 'Botão desabilitado; produto não é adicionado', 'Alternativo', 'S'],
        ['CT-CARR-04', 'Selecionar combinação sem estoque (L/Blue) e clicar em Comprar', 'PE (classe inválida)', 'Alerta "este produto não está disponível"; nada é adicionado', 'Negativo', 'S'],
        ['CT-CARR-05', 'Acessar o carrinho sem adicionar produtos', 'PE', 'Mensagem de carrinho vazio', 'Alternativo', 'S'],
        ['CT-CARR-06', 'Adicionar 9, 10 e 11 unidades do mesmo produto', 'VL (10)', '9 e 10 aceitos; 11 bloqueado com mensagem de limite', 'Negativo', 'N'],
        ['CT-CARR-07', 'Montar carrinho com totais R$ 989,99 / R$ 990,00 / R$ 990,01', 'VL (R$ 990)', 'Até R$ 990,00 permitido; R$ 990,01 bloqueado', 'Negativo', 'N'],
        ['CT-CARR-08', 'Totais R$ 199,99 / 200,00 / 600,00 / 600,01', 'VL + TD', 'Sem cupom / 10% / 10% / 15%', 'Feliz', 'N'],
    ]},
    {'us': 'US-0002 – Login na plataforma', 'casos': [
        ['CT-LOGIN-01', 'Informar usuário e senha válidos e clicar em Login', 'PE (válida)', 'Painel Minha Conta com "Olá, aluno_ebac"', 'Feliz', 'S'],
        ['CT-LOGIN-02', 'Informar usuário válido e senha incorreta', 'PE (inválida)', 'Mensagem "A senha fornecida ... está incorreta"', 'Alternativo', 'S'],
        ['CT-LOGIN-03', 'Informar usuário inexistente', 'PE (inválida)', 'Mensagem de erro; usuário não autenticado', 'Negativo', 'S'],
        ['CT-LOGIN-04', 'Clicar em Login com os campos vazios', 'PE (inválida)', 'Mensagem de campo obrigatório', 'Negativo', 'S'],
        ['CT-LOGIN-05', 'Tentar login com usuário inativo', 'TD (ativo × credencial)', 'Login negado com mensagem de usuário inativo', 'Negativo', 'N'],
        ['CT-LOGIN-06', 'Errar a senha 2 e 3 vezes e tentar a senha correta', 'VL (3 tentativas)', '2 erros: login liberado; 3 erros: bloqueio por 15 minutos', 'Negativo', 'N'],
        ['CT-LOGIN-07', 'Após bloqueio, aguardar 15 minutos e logar', 'VL (15 min)', 'Login liberado após o tempo de bloqueio', 'Alternativo', 'N'],
    ]},
    {'us': 'US-0003 – API de cupons', 'casos': [
        ['CT-API-01', 'GET /wc/v3/coupons autenticado', 'PE', 'Status 200 e lista de cupons conforme contrato', 'Feliz', 'S'],
        ['CT-API-02', 'GET /wc/v3/coupons/{id} de cupom existente', 'PE', 'Status 200; mesmo ID; contrato válido', 'Feliz', 'S'],
        ['CT-API-03', 'GET /wc/v3/coupons/999999999', 'PE (inválida)', 'Status 404 woocommerce_rest_shop_coupon_invalid_id', 'Alternativo', 'S'],
        ['CT-API-04', 'GET /wc/v3/coupons sem autenticação', 'PE (inválida)', 'Status 401 woocommerce_rest_cannot_view', 'Negativo', 'S'],
        ['CT-API-05', 'POST com code único, amount 10.00, fixed_product e descrição', 'PE (válida)', 'Status 201 e cupom conforme contrato', 'Feliz', 'S'],
        ['CT-API-06', 'POST repetindo um code já cadastrado', 'PE (inválida)', 'Status 400 "O código de cupom já existe"', 'Alternativo', 'S'],
        ['CT-API-07', 'POST sem o campo code', 'PE (inválida)', 'Status 400 rest_missing_callback_param', 'Negativo', 'S'],
        ['CT-API-08', 'POST com discount_type inválido', 'PE (inválida)', 'Status 400 rest_invalid_param', 'Negativo', 'S'],
    ]},
    {'us': 'US-0004 – Catálogo de Produtos', 'casos': [
        ['CT-MOB-01', 'Abrir o app e visualizar a vitrine (Home)', 'PE', 'Barra de busca, categorias e navegação exibidas', 'Feliz', 'S'],
        ['CT-MOB-02', 'Acessar a aba Browse', 'PE', 'Lista de produtos com nome e preço (R$)', 'Feliz', 'S'],
        ['CT-MOB-03', 'Buscar por termo existente', 'PE (válida)', 'Somente produtos que contenham o termo', 'Feliz', 'S'],
        ['CT-MOB-04', 'Buscar por termo inexistente', 'PE (inválida)', 'Nenhum produto listado / mensagem informativa', 'Alternativo', 'S'],
        ['CT-CAT-05', 'Web: abrir detalhe do produto', 'PE', 'Nome, preço, variações e botão Comprar', 'Feliz', 'N'],
    ]},
    {'us': 'US-0005 – Painel Minha Conta', 'casos': [
        ['CT-CONTA-01', 'Logar e acessar Minha Conta', 'PE', 'Saudação e menu completo', 'Feliz', 'N'],
        ['CT-CONTA-02', 'Acessar Minha Conta sem login', 'PE (inválida)', 'Formulário de login exibido', 'Alternativo', 'N'],
        ['CT-CONTA-03', 'Clicar em cada item do menu', 'PE', 'Cada link abre a página correspondente', 'Feliz', 'N'],
        ['CT-CONTA-04', 'Clicar em Sair', 'PE', 'Sessão encerrada e retorno ao login', 'Alternativo', 'N'],
    ]},
    {'us': 'US-0006 – Meus Pedidos', 'casos': [
        ['CT-PED-01', 'Cliente com pedidos acessa Pedidos', 'PE', 'Lista com número, data, status, total e Visualizar', 'Feliz', 'N'],
        ['CT-PED-02', 'Clicar em Visualizar', 'PE', 'Detalhes do pedido (itens, valores, endereços)', 'Feliz', 'N'],
        ['CT-PED-03', 'Cliente sem pedidos acessa Pedidos', 'PE', 'Mensagem "Nenhum pedido foi feito ainda"', 'Alternativo', 'N'],
        ['CT-PED-04', 'Acessar URL de pedido de outro cliente', 'PE (inválida)', 'Pedido não exibido', 'Negativo', 'N'],
    ]},
    {'us': 'US-0007 – Endereços', 'casos': [
        ['CT-END-01', 'Preencher faturamento com dados válidos e salvar', 'PE (válida)', 'Mensagem de endereço alterado com sucesso', 'Feliz', 'N'],
        ['CT-END-02', 'Salvar com Nome, CEP ou Telefone vazio', 'PE (inválida)', 'Mensagem de campo obrigatório', 'Negativo', 'N'],
        ['CT-END-03', 'CEP com 7, 8 dígitos e com letras', 'VL + PE', 'Somente 8 dígitos numéricos aceito', 'Negativo', 'N'],
        ['CT-END-04', 'Editar cidade do endereço de entrega', 'PE', 'Endereço exibe a nova cidade', 'Alternativo', 'N'],
    ]},
    {'us': 'US-0008 – Detalhes da Conta', 'casos': [
        ['CT-DET-01', 'Alterar nome de exibição e salvar', 'PE (válida)', 'Mensagem de detalhes modificados com sucesso', 'Feliz', 'N'],
        ['CT-DET-02', 'Alterar senha com senha atual correta e confirmação igual', 'TD', 'Senha alterada', 'Feliz', 'N'],
        ['CT-DET-03', 'Nova senha e confirmação diferentes', 'TD', 'Mensagem "As novas senhas não coincidem"', 'Negativo', 'N'],
        ['CT-DET-04', 'Salvar com e-mail inválido', 'PE (inválida)', 'Mensagem de e-mail inválido', 'Negativo', 'N'],
    ]},
]

DEFEITOS_INTRO = (
    'Durante a execução manual (com apoio de requisições HTTP) das regras de negócio das histórias US-0001 e US-0002, '
    'foram identificados os defeitos abaixo. Eles foram mantidos como casos manuais (não automatizados) para não '
    'quebrar o pipeline de regressão e devem ser priorizados com o PO.'
)

DEFEITOS = [
    ['BUG-01', 'Carrinho aceita mais de 10 unidades do mesmo produto (CT-CARR-06).', 'Abominable Hoodie XS/Red com quantidade 11: carrinho exibe 11 unidades, sem mensagem.', 'Média'],
    ['BUG-02', 'Carrinho permite total acima de R$ 990,00 (CT-CARR-07).', '15 unidades de R$ 69,00: total R$ 1.035,00 aceito.', 'Média'],
    ['BUG-03', 'Cupom automático de 10%/15% não é aplicado (CT-CARR-08).', 'Carrinho com R$ 759,00: nenhum desconto aplicado (esperado 15%).', 'Média'],
    ['BUG-04', 'Login não é bloqueado após 3 senhas incorretas (CT-LOGIN-06).', 'user5_ebac: 3 tentativas com senha errada e a 4ª, correta, autentica normalmente.', 'Alta'],
    ['BUG-05', 'Degradação de desempenho sob carga de 20 usuários (CT-PERF-01/02).', 'p95 acima do limite de 3 s e respostas 502 Bad Gateway (ver seção 4.7).', 'Alta'],
]

REPOSITORIO_TEXTO = (
    'Todo o código-fonte das automações, os arquivos Gherkin, o mapa mental, as evidências e este documento estão '
    'versionados no repositório público abaixo. O README descreve a estrutura, os pré-requisitos e os comandos de '
    'execução de cada projeto.'
)
REPOSITORIO_LINK = REPO

REPOSITORIO_ARVORE = [
    'TCC-EBAC-QE/',
    '├── .github/workflows/   ci.yml (API, UI, k6 + GitHub Pages) e mobile.yml (Sauce Labs)',
    '├── API/                 Supertest + Mocha + Joi (contratos)',
    '├── UI/                  Cypress + Page Objects + App Actions',
    '├── Mobile/              WebdriverIO + Appium (iOS no Sauce Labs) + Screen Objects',
    '├── Performance/         k6 (login e catálogo)',
    '├── docs/                TCC-EBAC-QE.docx, mapa mental, features Gherkin e evidências',
    '└── README.md',
]

AUTOMACAO_INTRO = (
    'Foram automatizados os casos marcados com "S" nas tabelas de casos de teste, cobrindo caminhos felizes, '
    'alternativos e negativos. Todos os projetos foram escritos em JavaScript/Node.js, aproveitando um único '
    'ecossistema (npm) para UI, API e mobile, e geram relatórios HTML a cada execução.'
)

UI_TEXTO = [
    'A automação web (pasta UI) cobre as histórias US-0001 (carrinho) e US-0002 (login) com 9 casos de teste. Foram '
    'aplicados os padrões Page Objects (login.page.js, produto.page.js, carrinho.page.js), App Actions '
    '(carrinho.actions.js, que encapsula o fluxo de adicionar produto) e Custom Commands (cy.login com cy.session), '
    'além de massa de dados em fixtures. O relatório é gerado com o cypress-mochawesome-reporter, incluindo '
    'screenshots embutidos em caso de falha.',
    'Para justificar a escolha da ferramenta, foi feito o comparativo a seguir entre três opções de mercado.',
]

COMPARATIVO = [
    ['Linguagem', 'JavaScript/TypeScript', 'TypeScript, JavaScript, Python, Java, .NET', 'Java, C#, Python, JS, Ruby'],
    ['Instalação / setup', 'npm install; tudo incluso (runner, asserções, mocks)', 'npm init playwright; baixa navegadores', 'Requer drivers, runner (JUnit/TestNG) e libs de asserção'],
    ['Esperas', 'Automáticas (retry-ability)', 'Automáticas (auto-wait)', 'Explícitas/implícitas, codificadas pelo QE'],
    ['Navegadores', 'Chrome, Edge, Electron, Firefox', 'Chromium, Firefox, WebKit', 'Todos os principais (W3C WebDriver)'],
    ['Depuração', 'Excelente: time-travel, snapshots no runner', 'Muito boa: trace viewer, codegen', 'Limitada: logs e prints'],
    ['Velocidade / paralelismo', 'Boa; paralelismo via Cypress Cloud ou CI', 'Muito boa; paralelismo nativo', 'Depende do Selenium Grid'],
    ['Múltiplas abas/domínios', 'Restrito (cy.origin)', 'Suporte completo', 'Suporte completo'],
    ['Relatórios', 'Mochawesome, Allure, Cypress Cloud', 'HTML nativo, Allure', 'Allure, Extent, Surefire'],
    ['Curva de aprendizado', 'Baixa', 'Média', 'Alta'],
    ['Experiência prévia do autor', 'Alta (módulos 11 a 24)', 'Baixa', 'Baixa'],
]

UI_JUSTIFICATIVA = [
    'O Cypress foi escolhido por reunir o melhor equilíbrio para o contexto: os fluxos testados ficam em um único '
    'domínio (onde sua limitação de múltiplas abas não pesa), as esperas automáticas reduzem testes instáveis em uma '
    'loja com bastante JavaScript de terceiros, o runner facilita a depuração e o time (no caso, o autor) já possui '
    'experiência com a ferramenta, reduzindo o tempo de entrega. O Playwright seria a alternativa mais forte caso '
    'houvesse necessidade de WebKit ou múltiplas abas, e o Selenium faria sentido em times Java com Grid já existente.',
]

API_TEXTO = [
    'A automação de API (pasta API) valida a US-0003 com Supertest, Mocha e Chai. Os padrões adotados foram Service '
    'Object (support/api.js centraliza os endpoints e a autenticação Basic) e Data Factory (support/factory.js gera '
    'códigos de cupom únicos com Faker, evitando conflito com execuções anteriores). Os contratos são validados com '
    'Joi (contracts/cupom.contract.js) para a resposta de cupom, para a lista de cupons e para o formato de erro. Os '
    'cupons criados durante os testes são excluídos ao final (DELETE ?force=true), mantendo o ambiente limpo.',
    'Foram automatizados 8 casos: listagem e busca por ID (200 + contrato), ID inexistente (404), acesso sem '
    'autenticação (401), cadastro com campos obrigatórios (201 + contrato), código repetido, ausência de code e '
    'discount_type inválido (400). O relatório é gerado com o Mochawesome.',
]

MOBILE_TEXTO = [
    'A automação mobile (pasta Mobile) considera apenas a funcionalidade de Catálogo de Produtos, conforme o enunciado. '
    'Foi escolhida a plataforma iOS, pois o aplicativo iOS disponibilizado pela EBAC (EBAC Store) é o aplicativo de '
    'catálogo voltado ao cliente, enquanto o APK Android corresponde ao aplicativo administrativo do WooCommerce. '
    'Os testes usam WebdriverIO 9 com Appium (XCUITest) executando em simuladores do Sauce Labs, o que dispensa '
    'emuladores locais e permite a execução no GitHub Actions. Foi aplicado o padrão Screen Object (equivalente ao '
    'Page Object para telas mobile) e o relatório é gerado com o Allure.',
]

MOBILE_IMAGENS = [
    ('mobile-home.png', 'Tela inicial do app EBAC Store capturada durante a execução no Sauce Labs.'),
    ('mobile-browse.png', 'Aba Browse com a listagem de produtos.'),
]

CI_TEXTO = [
    'A integração contínua foi implementada com GitHub Actions. A cada push ou pull request na branch main, o '
    'workflow ci.yml executa em paralelo os testes de API, UI e performance; os relatórios são publicados como '
    'artefatos e, ao final, reunidos e publicados no GitHub Pages. O workflow mobile.yml executa os testes do '
    'aplicativo no Sauce Labs, com as credenciais armazenadas em GitHub Secrets.',
]

CI_ITENS = [
    ('api: ', 'Node 20, npm ci e npm test (Supertest), relatório Mochawesome como artefato.'),
    ('ui: ', 'cypress-io/github-action no Chrome headless, relatório Mochawesome como artefato.'),
    ('performance: ', 'grafana/setup-k6-action executa login.test.js e catalogo.test.js; marcado como continue-on-error, '
     'pois o ambiente é compartilhado e os thresholds estourados são achados documentados, e não falhas funcionais.'),
    ('relatorios: ', 'baixa os artefatos e publica um índice com todos os relatórios no GitHub Pages.'),
    ('mobile.yml: ', 'WebdriverIO no Sauce Labs com SAUCE_USERNAME, SAUCE_ACCESS_KEY e SAUCE_APP em Secrets; relatório Allure como artefato.'),
]

PERF_TEXTO = [
    'Os testes de performance foram implementados com k6 para dois casos: CT-PERF-01 – login na plataforma '
    '(abre Minha Conta, extrai o nonce do formulário e autentica) e CT-PERF-02 – navegação no catálogo (listagem, '
    'busca e detalhe do produto). A configuração segue o enunciado: 20 usuários virtuais, 2 minutos de execução e '
    'ramp-up de 20 segundos (stages: 20 s subindo até 20 VUs, 1 min 30 s sustentando e 10 s de ramp-down). A massa '
    'de dados user1_ebac a user5_ebac é carregada com SharedArray e distribuída entre os VUs. Foram definidos os '
    'thresholds: p95 de http_req_duration < 3 s, taxa de falhas < 5% e checks > 95%.',
]

PERF_ANALISE = [
    'Os resultados mostram que o ambiente não sustenta 20 usuários simultâneos dentro do objetivo de tempo de '
    'resposta: o p95 ficou bem acima de 3 segundos nos dois cenários e o tempo médio de resposta ultrapassou 3 '
    'segundos. No login, parte das requisições retornou 502 Bad Gateway e, em alguns momentos, a página Minha Conta '
    'foi entregue incompleta (sem o formulário), o que derrubou a taxa de checks. No catálogo, a taxa de falhas HTTP '
    'ficou dentro do limite, mas a latência também degradou com o aumento de usuários.',
    'Como o ambiente é compartilhado por todos os alunos, recomenda-se repetir os testes no ambiente Docker isolado '
    'para separar o efeito do ambiente do desempenho da aplicação; ainda assim, o resultado foi registrado como '
    'defeito (BUG-05) e indica a necessidade de cache de páginas, ajuste do servidor (PHP-FPM/nginx) e monitoramento.',
]

CONCLUSAO = [
    'Realizar este trabalho foi bastante desafiador e, ao mesmo tempo, a melhor forma de consolidar tudo o que vi na '
    'formação. Precisei juntar em um único projeto assuntos que estudei separadamente ao longo dos módulos: '
    'escrever histórias e critérios em Gherkin, aplicar técnicas como partição de equivalência, valor limite e '
    'tabela de decisão, automatizar testes de UI com Cypress, de API com Supertest e contratos, de aplicativos com '
    'Appium e WebdriverIO, rodar testes de carga com k6 e colocar tudo isso para rodar sozinho no GitHub Actions.',
    'Alguns módulos foram bem difíceis para mim. A parte de mobile foi a que mais exigiu paciência: configurar '
    'Appium, emuladores e depois o Sauce Labs, entender os seletores de cada plataforma e lidar com sessões lentas e '
    'instáveis. Integração contínua e performance também tiveram uma curva grande, principalmente para entender por '
    'que algo funcionava na minha máquina e falhava no pipeline, ou para interpretar métricas como p95 e taxa de '
    'falhas em vez de simplesmente olhar se o teste "passou". Mesmo assim, foi justamente nesses pontos que mais aprendi.',
    'A principal lição que levo para a vida profissional é que qualidade começa antes do código: critérios bem '
    'escritos e uma estratégia clara evitam retrabalho e mostram onde vale a pena automatizar. Também ficou claro que '
    'automação não substitui a análise do QE – foram os testes manuais e exploratórios das regras de negócio que '
    'revelaram defeitos importantes, como o carrinho sem limite de itens e o login sem bloqueio. Termino a formação '
    'com muito mais maturidade na área, segurança para propor estratégias de teste e um portfólio real no GitHub que '
    'demonstra o fluxo completo de trabalho de um Engenheiro de Qualidade.',
]

REFERENCIAS = [
    [('ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ', False), ('NBR ISO/IEC 25010', True), (': engenharia de sistemas e software – requisitos e avaliação da qualidade de sistemas e software (SQuaRE). Rio de Janeiro: ABNT, 2011.', False)],
    [('BRAZILIAN SOFTWARE TESTING QUALIFICATIONS BOARD. ', False), ('Certified Tester Foundation Level (CTFL) – Syllabus versão 4.0', True), ('. BSTQB, 2023. Disponível em: https://bstqb.online. Acesso em: 6 out. 2026.', False)],
    [('CRISPIN, Lisa; GREGORY, Janet. ', False), ('Agile Testing', True), (': a practical guide for testers and agile teams. Boston: Addison-Wesley, 2009.', False)],
    [('COHN, Mike. ', False), ('Succeeding with Agile', True), (': software development using Scrum. Boston: Addison-Wesley, 2009.', False)],
    [('CYPRESS. ', False), ('Cypress Documentation', True), ('. Disponível em: https://docs.cypress.io. Acesso em: 6 out. 2026.', False)],
    [('EBAC – ESCOLA BRITÂNICA DE ARTES CRIATIVAS E TECNOLOGIA. ', False), ('Profissão: Engenheiro de Qualidade de Software', True), ('. Material didático, módulos 1 a 32. São Paulo: EBAC, 2025-2026.', False)],
    [('GRAFANA LABS. ', False), ('k6 Documentation', True), ('. Disponível em: https://grafana.com/docs/k6. Acesso em: 6 out. 2026.', False)],
    [('GITHUB. ', False), ('GitHub Actions Documentation', True), ('. Disponível em: https://docs.github.com/actions. Acesso em: 6 out. 2026.', False)],
    [('LADJS. ', False), ('Supertest: super-agent driven library for testing HTTP servers', True), ('. Disponível em: https://github.com/ladjs/supertest. Acesso em: 6 out. 2026.', False)],
    [('SAUCE LABS. ', False), ('Sauce Labs Documentation', True), ('. Disponível em: https://docs.saucelabs.com. Acesso em: 6 out. 2026.', False)],
    [('SMART, John Ferguson. ', False), ('BDD in Action', True), (': behavior-driven development for the whole software lifecycle. Shelter Island: Manning, 2014.', False)],
    [('WEBDRIVERIO. ', False), ('WebdriverIO Documentation', True), ('. Disponível em: https://webdriver.io/docs. Acesso em: 6 out. 2026.', False)],
    [('WOOCOMMERCE. ', False), ('WooCommerce REST API Documentation', True), ('. Disponível em: https://woocommerce.github.io/woocommerce-rest-api-docs. Acesso em: 6 out. 2026.', False)],
]
