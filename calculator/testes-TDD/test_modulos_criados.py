import pytest
import os

BASE_DIR = '/home/lobonegro/Desktop/NUPREDS/calculator/'

def test_modulo_core_criado():
    diretorios = os.listdir(BASE_DIR)
    assert ("core" in diretorios) == True
        