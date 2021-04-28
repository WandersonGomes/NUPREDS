import pytest
import os

STATIC_DIR = "/home/lobonegro/Desktop/NUPREDS/calculator/static/"

def test_static_index_css():
    arquivosCSS = os.listdir(os.path.join(STATIC_DIR, "css"))
    assert ("index.css" in arquivosCSS) == True

def test_static_index_js():
    arquivosJS = os.listdir(os.path.join(STATIC_DIR, "js"))
    assert ("index.js" in arquivosJS) == True