from behave import given, when, then
import json

url_calculadora = 'http://127.0.0.1:8000/'
lista_botoes_json = '/home/lobonegro/Desktop/NUPREDS/calculator/testes-BDD/componentes/features/json/botoes.json'

# FUNCOES AUXILIARES
def ler_json(arquivo_json):
    with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

@given('eu va para a pagina da calculadora')
def indo_para_a_pagina_calculadora(context):
    context.navegador.get(url_calculadora)


@when('eu apertar os botoes da calculadora exceto "{botao1}" e "{botao2}"')
def apertar_botoes(context, botao1, botao2):
    botoes = ler_json(lista_botoes_json)["botoes_calculadora"]
    context.calculadora = context.navegador.find_element_by_id("calculator")
    context.resultado_esperado = ''
    for botao in botoes:
        if botao["id"] != botao1 and botao["id"] != botao2:
            context.calculadora.find_element_by_id(botao["id"]).click()
            context.resultado_esperado += botao["label"]


@then('terei no visor da calculadora os simbolos de cada botao impresso no visor da calculadora')
def verificando_o_visor_calculadora(context):
    visor = context.calculadora.find_element_by_id("visor")
    assert (visor.get_attribute("value") == context.resultado_esperado) == True


@when('eu apertar alguns botoes como por exemplo "{botao1}" and "{botao2}"')
def apertando_os_dois_botoes_para_testar_o_botao_clear(context, botao1, botao2):
    context.calculadora = context.navegador.find_element_by_id("calculator")
    context.calculadora.find_element_by_id(botao1).click()
    context.calculadora.find_element_by_id(botao2).click()

@when('depois eu apertar o botao "{id}"')
def apertando_botao_clear(context, id):
    context.calculadora.find_element_by_id(id).click()

@then('terei o visor da calculadora limpo')
def checando_visor_calculadora_limpo(context):
    visor = context.calculadora.find_element_by_id("visor")
    assert (visor.get_attribute("value") == "") == True

@when('eu apertar os botoes "{botao1}", "{botao2}", "{botao3}" e depois "{botao4}"')
def apertando_um_mais_um(context, botao1, botao2, botao3, botao4):
    calculadora = context.navegador.find_element_by_id("calculator")
    calculadora.find_element_by_id(botao1).click()
    calculadora.find_element_by_id(botao2).click()
    calculadora.find_element_by_id(botao3).click()
    calculadora.find_element_by_id(botao4).click()


@then('deverar se colocado no topo do historico o resultado "{conteudo}"')
def step_impl(context, conteudo):
    historico = context.navegador.find_element_by_id("historic")
    resultados_historico = historico.find_elements_by_tag_name("div")
    assert (resultados_historico[0].text == conteudo) == True