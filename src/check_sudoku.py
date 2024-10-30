from src.check_vacio import check_vacio
from src.check_es_cuadrado import check_es_cuadrado
from src.check_es_real import check_es_real
def check_sudoku(sudoku):
    
    assert isinstance(sudoku, list)
    
    return check_vacio(sudoku) and check_es_cuadrado(sudoku) and check_es_real(sudoku)