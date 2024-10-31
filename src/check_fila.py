def check_fila(sudoku):
    
    assert isinstance(sudoku, list)

    for fila in sudoku:

        rango_numeros_correctos = list(range(1, len(fila)+1))
        if rango_numeros_correctos != sorted(fila):
            return False    
                      
    return True



if __name__ == '__main__':
    
    
    assert check_fila([[1, 2, 3],
                       [2, 3, 1],     #Test_correcto
                       [3, 1, 2]])
    
    assert check_fila( [[0, 2, 3, 4, 5],
                        [2, 3, 1, 5, 6],
                        [4, 5, 2, 1, 3],  #número_fuera_de_rango
                        [3, 4, 5, 2, 1],
                        [5, 6, 4, 3, 2]]) is False
    
    assert check_fila([[1, 2, 3, 4],
                       [2, 3, 1, 2],  #Test_número_no_presente
                       [4, 1, 2, 3],
                       [2, 3, 1, 4]]) is False
    
    assert check_fila([[1, 2, 3, 4],
                       [2, 3, 1, 3],  #Test_números_repetidos
                       [3, 1, 2, 3],
                       [4, 4, 4, 2]]) is False
    