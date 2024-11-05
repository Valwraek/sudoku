def check_es_cuadrado(sudoku):
    
    assert isinstance(sudoku, list)

    lon_fila_sudoku = len(sudoku)
    for fila in sudoku:
        if len(fila) != lon_fila_sudoku:
            return False
    
    return True
        

if __name__ == '__main__':
    
    assert check_es_cuadrado([[1, 2, 3],
                              [2, 3, 1]]) is False

    assert check_es_cuadrado([[1, 2, 3],
                              [2, 3, 1],
                              [3, 1]]) is False

