def check_columna(sudoku):
    
    rango_longitud_sudoku = range(len(sudoku))

    for posicion_columna in rango_longitud_sudoku:
        
        comprobador_columna = []
        for posicion_fila in rango_longitud_sudoku:
            comprobador_columna.append(sudoku[posicion_fila][posicion_columna])
        
        rango_numeros_correctos = list(range(1, len(sudoku)+1))
        if rango_numeros_correctos != sorted(comprobador_columna):
            return False  
    
    return True




if __name__ == '__main__':
    
    assert check_columna([[1, 2, 3],
                          [2, 3, 1],
                          [3, 1, 2]])
    
    assert check_columna([[1, 2, 3],
                          [2, 3, 1],  #numero_repetido_columna
                          [2, 3, 1]]) is False
    
    assert check_columna([[1, 2, 3, 4],
                          [2, 3, 1, 3],  #numero_repetido_fila_columna
                          [3, 1, 2, 3],
                          [4, 4, 4, 2]]) is False
     