Feature: verificando os componentes visiveis na tela da calculadora
    Scenario: checar a lista de botoes disponivel no diretorio json
        Given eu acesse a pagina da calculadora
        When eu encontrar a calculadora
        Then ela tera todos os botoes da lista localizada em "/home/lobonegro/Desktop/NUPREDS/calculator/testes-BDD/componentes/features/json/botoes.json"

    Scenario: checar se o visor da calculadora esta disponivel
        Given eu acesse a pagina da calculadora
        When eu encontrar a calculadora
        Then ela tera o visor com o id "visor" disponivel

    Scenario: verificando a disponibilidade de um historico de operacoes
        Given eu acesse a pagina da calculadora
        When eu estiver na pagina
        Then ela tera uma caixa contendo o historico de operacoes feita pela calculadora com o id "historic"
        And a caixa do historico tera um cabecalho h2 com o texto "Calculation History:"