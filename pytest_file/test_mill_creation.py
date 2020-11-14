"""
Upsetti Spaghetti Coders
THIS FILE IS FOR TESTING CHECK_ADJACENT FUNCTION USING PYTEST
IF USING PYCHARM MAKE SURE TO SET PYTEST AS DEFAULT TESTING IN PREFERENCES
"""

import game_functions_classes
import board
import player


def test_mill_found():
    player_1 = player.Player(1, True)

    assert game_functions_classes.mill_found(3, player_1, []) == 1
    assert player_1.new_mill
    assert player_1.mills == 1


def test_adjacent_none():
    """Checks no mill is present, placed random pieces on grid around (0,0)"""
    test_grid = board.Board()
    test_grid.grid = [[1, -1, -1, 2, -1, -1, 2],
                      [-1, 1, -2, 2, -2, 1, -1],
                      [-1, -2, 0, 0, 0, -2, -1],
                      [1, 2, 0, -3, 0, 0, 0],
                      [-1, -2, 0, 0, 0, -2, -1],
                      [-1, 2, -2, 0, -2, 0, -1],
                      [2, -1, -1, 0, -1, -1, 0]]

    player_1 = player.Player(1, True)

    assert game_functions_classes.check_adjacent(0, 0, test_grid, player_1) == 0
    assert player_1.mills == 0
    assert not player_1.new_mill
    assert player_1.mill_positions == []



def test_adjacent_horizontal():
    """Checks horizontal mill, placed player 1 mill on top row"""
    test_grid = board.Board()
    test_grid.grid = [[1, -1, -1, 1, -1, -1, 1],
                      [-1, 0, -2, 2, -2, 1, -1],
                      [-1, -2, 0, 0, 0, -2, -1],
                      [1, 0, 0, -3, 0, 0, 0],
                      [-1, -2, 0, 0, 0, -2, -1],
                      [-1, 0, -2, 0, -2, 0, -1],
                      [2, -1, -1, 0, -1, -1, 0]]

    player_1 = player.Player(1, True)

    assert game_functions_classes.check_adjacent(0, 6, test_grid, player_1) == 1
    assert player_1.new_mill
    assert player_1.mills == 1
    assert player_1.mill_positions == [[(0,0), (0,3), (0,6)]]


def test_adjacent_vertical():
    """Checks vertical mill, placed player 1 mill in column 0"""
    test_grid = board.Board()
    test_grid.grid = [[1, -1, -1, 2, -1, -1, 2],
                      [-1, 0, -2, 2, -2, 1, -1],
                      [-1, -2, 0, 0, 0, -2, -1],
                      [1, 0, 0, -3, 0, 0, 0],
                      [-1, -2, 0, 0, 0, -2, -1],
                      [-1, 0, -2, 0, -2, 0, -1],
                      [1, -1, -1, 0, -1, -1, 0]]

    player_1 = player.Player(1, True)

    mills = game_functions_classes.check_adjacent(3, 0, test_grid, player_1)

    assert mills == 1
    assert player_1.new_mill
    assert player_1.mills == 1
    assert player_1.mill_positions == [[(0,0), (3,0), (6,0)]]


def test_double_mill():
    test_grid = board.Board()
    test_grid.grid = [[0, -1, -1, 0, -1, -1, 0],
                      [-1, 1, -2, 0, -2, 0, -1],
                      [-1, -2, 0, 0, 0, -2, -1],
                      [1, 1, 1, -3, 0, 0, 0],
                      [-1, -2, 0, 0, 0, -2, -1],
                      [-1, 1, -2, 0, -2, 0, -1],
                      [0, -1, -1, 0, -1, -1, 0]]

    player_1 = player.Player(1, True)

    assert game_functions_classes.check_adjacent(3, 1, test_grid, player_1) == 2
    assert player_1.new_mill
    assert player_1.mills == 2
    assert player_1.mill_positions == [[(3,0), (3,1), (3,2)], [(1,1), (3,1), (5,1)]]