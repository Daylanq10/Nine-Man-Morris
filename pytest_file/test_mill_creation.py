"""
Upsetti Spaghetti Coders
THIS FILE IS FOR TESTING CHECK_ADJACENT FUNCTION USING PYTEST
IF USING PYCHARM MAKE SURE TO SET PYTEST AS DEFAULT TESTING IN PREFERENCES
"""

import game_functions
import board


def test_adjacent_none():
    """Checks no mill is present"""
    test_grid = board.Board()
    assert game_functions.check_adjacent(x=0, y=0, board=test_grid, player_piece=1) == 0


def test_adjacent_horizontal():
    """Checks horizontal mill"""
    test_grid = board.Board()

    test_grid.grid[0][0] = 1
    test_grid.grid[0][3] = 1
    test_grid.grid[0][6] = 1

    assert game_functions.check_adjacent(x=0, y=6, board=test_grid, player_piece=1) == 1


def test_adjacent_vertical():
    """Checks vertical mill"""
    test_grid = board.Board()

    test_grid.grid[2][2] = 2
    test_grid.grid[3][2] = 2
    test_grid.grid[4][2] = 2

    assert game_functions.check_adjacent(x=4, y=2, board=test_grid, player_piece=2) == 1