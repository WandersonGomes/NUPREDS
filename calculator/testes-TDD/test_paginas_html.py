import pytest
import os

DIR_TEMPLATES = '/home/lobonegro/Desktop/NUPREDS/calculator/templates'

def test_index_html():
    arquivos = os.listdir(DIR_TEMPLATES)
    assert ("index.html" in arquivos) == True