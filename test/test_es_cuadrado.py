import pytest
from src.check_sudoku import check_sudoku
import casos_test.casos_test_sudoku as casos_test

@pytest.mark.es_cuadrado
def test_es_cuadrado():

    assert check_sudoku(casos_test.correcto)
    assert check_sudoku(casos_test.irregular_fila) is False
    assert check_sudoku(casos_test.irregular_columna) is False