import pytest
from src.check_columna import check_columna
import casos_test.casos_test_sudoku as casos_test

@pytest.mark.comprobar_columna
def test_check_columna():
    
    assert check_columna(casos_test.correcto)
    assert check_columna(casos_test.numero_repetido_fila_columna) is False
    assert check_columna(casos_test.numero_repetido_columna) is False


