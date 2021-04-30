from selenium.webdriver import Firefox
import behave

def before_all(context):
    context.navegador = Firefox()

def after_all(context):
    context.navegador.quit()
