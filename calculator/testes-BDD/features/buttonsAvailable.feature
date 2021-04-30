Feature: botoes disponiveis na calculadora
  Scenario: confirmando a presenca dos botoes
    Given eu acesse a pagina da calculadora
    When eu procurar pela seguinte lista de botoes com os seguintes ids:
      | id                  |
      | btn-clear           |
      | btn-parentese-left  |
      | btn-parentese-right |
      | btn-division        |
      | btn-seven           |
      | btn-eight           |
      | btn-nine            |
      | btn-multiplication  |
      | btn-four            |
      | btn-five            |
      | btn-six             |
      | btn-one             |
      | btn-two             |
      | btn-three           |
      | btn-sum             |
      | btn-zero            |
      | btn-point           |
      | btn-equals          |
    Then eu vou encontrar todos eles disponiveis e com os seguintes labels:
      | label   |
      | C       |
      | (       |
      | )       |
      | /       |
      | 7       |
      | 8       |
      | 9       |
      | *       |
      | 4       |
      | 5       |
      | 6       |
      | 1       |
      | 2       |
      | 3       |
      | +       |
      | 0       |
      | .       |
      | =       |
