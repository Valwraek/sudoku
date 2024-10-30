#import casos_test.casos_test_sudoku as casos_test
from decimal import Decimal
def check_es_real(sudoku):
    
    for fila_indice in range(len(sudoku)):
        for columna_indice in range(len(sudoku[fila_indice])):
            
            numero = sudoku[fila_indice][columna_indice]           
            if isinstance(numero, int) is False:
                return False
            if Decimal(numero).is_signed():
                print(numero)
                return False  
    return True



if __name__ == '__main__':


    assert check_es_real([[1, 2, 3],
                          [2, 3, 1],
                          [3, 1, 2]])  
    assert check_es_real([[1, 1.5], 
                          [1.5, 1]]) is False
    assert check_es_real([[1, 2, 3],
                          [2, -3, 1],
                          [3, 1, -2]]) is False