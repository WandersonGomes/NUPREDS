Feature: funcionalidade de cada botao da calculadora
    Scenario: verificar se ao apertar os botoes da calculadora os simbolos sao impressos no visor
        Given eu va para a pagina da calculadora
        When eu apertar os botoes da calculadora exceto "btn-clear" e "btn-equals"
        Then terei no visor da calculadora os simbolos de cada botao impresso no visor da calculadora
    
    Scenario: verificar se ao apertar o botao clear o visor ficara limpo
        Given eu va para a pagina da calculadora
        When eu apertar alguns botoes como por exemplo "btn-zero" and "btn-one"
        And depois eu apertar o botao "btn-clear"
        Then terei o visor da calculadora limpo

    Scenario: verificar se ao apertar o botao (igual) o resultado vai ser colocado no historico
        Given eu va para a pagina da calculadora
        When eu apertar os botoes "btn-one", "btn-sum", "btn-one" e depois "btn-equals"
        Then deverar se colocado no topo do historico o resultado "1+1 = 2"
    
    Scenario: verificar se ao apertar o botao (igual) o resultado vai ser colocado no historico
        Given eu va para a pagina da calculadora
        When eu apertar os botoes "btn-one", "btn-division", "btn-zero" e depois "btn-equals"
        Then deverar se colocado no topo do historico o resultado "1/0 = invalid"