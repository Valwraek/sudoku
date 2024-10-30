


def check_sudoku(sudoku):
    
    assert isinstance(sudoku, list)
    
    sudoku_vacio = [[]]
    if sudoku == sudoku_vacio:
        return False
        
    
    return True