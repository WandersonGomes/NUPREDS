Feature: verificar se o visor da calculadora esta disponivel
  Scenario: verificando se o visor esta disponivel na calculadora
    Given eu acesse a calculadora
    When eu procurar pelo visor da calculadora pelo id "visor"
    Then eu vou encontra-lo disponivel
