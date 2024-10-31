from src.check_sudoku import check_sudoku
import casos_test.casos_test_sudoku as casos_test

def test_check_sudoku():

    assert check_sudoku(casos_test.correcto)
    assert check_sudoku(casos_test.lista_vacia) is False
    
    assert check_sudoku(casos_test.irregular_fila) is False
    assert check_sudoku(casos_test.irregular_columna) is False
    
    assert check_sudoku(casos_test.numeros_decimales) is False
    assert check_sudoku(casos_test.caracteres) is False
    
    assert check_sudoku(casos_test.numero_no_presente) is False
    assert check_sudoku(casos_test.numero_fuera_del_rango) is False
    
    assert check_sudoku(casos_test.numero_repetido_fila_columna) is False 
    assert check_sudoku(casos_test.numero_repetido_columna) is False  

    