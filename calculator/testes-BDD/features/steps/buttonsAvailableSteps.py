from behave import given, when, then
import ipdb

url_calculator = 'http://127.0.0.1:8000'

@given('eu acesse a pagina da calculadora')
def acessando_pagina_calculadora(context):
    context.navegador.get(url_calculator)

@when('eu procurar pela seguinte lista de botoes com os seguintes ids')
def procurando_pelos_botoes(context):
    context.label_botoes = []
    for row in context.table:
        botao = context.navegador.find_element_by_id(row["id"])
        context.label_botoes.append(botao.text)

@then('eu vou encontrar todos eles disponiveis e com os seguintes labels')
def checando_labels_botoes_encontrados(context):
    for row in context.table:
        assert (row["label"] in context.label_botoes) == True
