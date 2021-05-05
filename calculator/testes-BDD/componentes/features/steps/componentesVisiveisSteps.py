from behave import given, when, then
import json.scanner
import ipdb

url_calculadora = 'http://127.0.0.1:8000/'
id_calculadora = 'calculator'

# FUNCOES AUXILIARES
def ler_json(arquivo_json):
    with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

# SCENARIO: botoes de 0 a 9
@given('eu acesse a pagina da calculadora')
def acessando_pagina_calculadora(context):
    context.navegador.get(url_calculadora)

@when('eu encontrar a calculadora')
def encontrando_calculadora_na_pagina(context):
    context.calculadora = context.navegador.find_element_by_id(id_calculadora)

@then('ela tera todos os botoes da lista localizada em "{arquivo_json}"')
def checando_presenca_botoes_0_a_9(context, arquivo_json):
    lista_botoes_calculadora = ler_json(arquivo_json)["botoes_calculadora"]
    for botao in lista_botoes_calculadora:
        assert context.calculadora.find_element_by_id(botao["id"]).text == botao["label"]

@then('ela tera o visor com o id "{id}" disponivel')
def checando_disponibilidade_visor_calculadora(context, id):
    visor = context.calculadora.find_element_by_id(id)
    assert bool(visor) == True

@when('eu estiver na pagina')
def ficando_pagina_calculadora(context):
    pass

@then('ela tera uma caixa contendo o historico de operacoes feita pela calculadora com o id "{id}"')
def procurando_caixa_historico(context, id):
    context.box_historic = context.navegador.find_element_by_id(id)
    assert bool(context.box_historic) == True

@then('a caixa do historico tera um cabecalho h2 com o texto "{texto}"')
def verificando_h2_historic_box(context, texto):
    cabecalho_h2 = context.box_historic.find_element_by_tag_name("h2")
    assert (cabecalho_h2.text == texto) == True

@then('ela tera um botao com id "{id}" com o seguinte texto "{texto}"')
def verifando_se_o_botao_limpa_historico_disponivel(context, id, texto):
    botao= context.navegador.find_element_by_id(id)
    assert bool(botao) == True 