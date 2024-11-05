#import casos_test.casos_test_sudoku as casos_test
from decimal import Decimal
def check_es_real(sudoku):
    
    assert isinstance(sudoku, list)
    
    for fila_indice in sudoku:
        for columna_indice in fila_indice:
                       
            if es_digito(columna_indice) is False or es_negativo(columna_indice):
                
                return False                                
    return True

def es_digito(numero):
    
    if isinstance(numero, int) is True:
        
        return True
    return False

def es_negativo(numero):
    
    if Decimal(numero).is_signed():
        
        return True
    return False
            


if __name__ == '__main__':


    assert check_es_real([[1, 2, 3],
                          [2, 3, 1],
                          [3, 1, 2]])  
    assert check_es_real([[1, 1.5], 
                          [1.5, 1]]) is False
    assert check_es_real([[1, 2, 3],
                          [2, -3, 1],
                          [3, 1, -2]]) is False