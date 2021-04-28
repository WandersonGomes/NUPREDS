import pytest
import os

BASE_DIR = '/home/lobonegro/Desktop/NUPREDS/calculator/'

def test_templates_criado():
    diretorios = os.listdir(BASE_DIR)
    assert ("templates" in diretorios) == True

def test_static_criado():
    diretorios = os.listdir(BASE_DIR)
    assert ("static" in diretorios) == True

def test_static_css_criado():
    diretoriosStatic = os.listdir(os.path.join(BASE_DIR, "static"))
    assert ("css" in diretoriosStatic) == True

def test_static_js_criado():
    diretoriosStatic = os.listdir(os.path.join(BASE_DIR, "static"))
    assert ("js" in diretoriosStatic) == True