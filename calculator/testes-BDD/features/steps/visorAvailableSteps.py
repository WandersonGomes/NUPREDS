from behave import given, when, then

url_calculator = "http://127.0.0.1:8000/"

@given('eu acesse a calculadora')
def acessando_pagina_calculadora(context):
    context.navegador.get(url_calculator)

@when('eu procurar pelo visor da calculadora pelo id "{id}"')
def procurando_visor_calculadora(context, id):
    context.visor = context.navegador.find_element_by_id(id)

@then('eu vou encontra-lo disponivel')
def checando_visor_disponivel(context):
    assert bool(context.visor) == True
