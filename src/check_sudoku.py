from src.check_vacio import check_vacio
from src.check_es_cuadrado import check_es_cuadrado
from src.check_es_real import check_es_real
from src.check_fila import check_fila
from src.check_columna import check_columna
def check_sudoku(sudoku):
    
    assert isinstance(sudoku, list)
    
    return check_vacio(sudoku) and check_es_cuadrado(sudoku) \
        and check_es_real(sudoku) and check_fila(sudoku) \
        and check_columna(sudoku)
     