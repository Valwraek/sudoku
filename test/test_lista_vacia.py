import pytest
from src.check_sudoku import check_sudoku
import casos_test.casos_test_sudoku as casos_test

@pytest.mark.sudoku_vacio
def test_es_sudoku_vacio():
    
    assert check_sudoku(casos_test.lista_vacia) is False