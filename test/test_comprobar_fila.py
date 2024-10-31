import pytest
from src.check_fila import check_fila
import casos_test.casos_test_sudoku as casos_test

@pytest.mark.comprobar_fila
def test_comprobar_fila():
    assert check_fila(casos_test.correcto)
    assert check_fila(casos_test.numero_no_presente) is False
    assert check_fila(casos_test.numero_repetido_fila_columna) is False