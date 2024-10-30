def check_es_cuadrado(sudoku):
    
    assert isinstance(sudoku, list)

    lon_columna = len(sudoku)
    for fila in range(lon_columna):
        if len(sudoku[fila]) != lon_columna:
            return False
    
    return True
        


if __name__ == '__main__':
    
    assert check_es_cuadrado([[1, 2, 3],
                              [2, 3, 1]]) is False

    assert check_es_cuadrado([[1, 2, 3],
                              [2, 3, 1],
                              [3, 1]]) is False

