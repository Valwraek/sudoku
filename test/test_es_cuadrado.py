import pytest
from src.check_es_cuadrado import check_es_cuadrado
import casos_test.casos_test_sudoku as casos_test

@pytest.mark.es_cuadrado
def test_es_cuadrado():

    assert check_es_cuadrado(casos_test.correcto)
    assert check_es_cuadrado(casos_test.irregular_fila) is False
    assert check_es_cuadrado(casos_test.irregular_columna) is False