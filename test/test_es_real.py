import pytest
from src.check_es_real import check_es_real
import casos_test.casos_test_sudoku as casos_test

@pytest.mark.es_real
def test_es_real():
    
    assert check_es_real(casos_test.correcto)   
    assert check_es_real(casos_test.caracteres) is False
    assert check_es_real(casos_test.numeros_decimales) is False
    assert check_es_real(casos_test.numeros_negativos) is False
    