import pytest
from src.check_vacio import check_vacio
import casos_test.casos_test_sudoku as casos_test

@pytest.mark.sudoku_vacio
def test_es_sudoku_vacio():
    
    assert check_vacio(casos_test.correcto)
    assert check_vacio(casos_test.lista_vacia) is False
    assert check_vacio(casos_test.numeros_decimales)
    