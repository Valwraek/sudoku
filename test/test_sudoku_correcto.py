from src.check_sudoku import check_sudoku


def test_check_sudoku():
    correcto = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]
    
    assert check_sudoku(correcto)