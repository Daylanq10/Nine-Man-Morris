"""
Upsetti Spaghetti Coders
THIS FILE IS FOR TESTING PURPOSES USING PYTEST
IF USING PYCHARM MAKE SURE TO SET PYTEST AS DEFAULT TESTING IN PREFERENCES
"""

import game_functions
import player

def test_user_swap_1():
    """Checks player 1 to player 2"""
    player_1 = player.Player(True, True)
    player_2 = player.Player(False, True)
    current = player_1.turn
    game_functions.swap_player(player_1, player_2)
    new = player_2.turn
    assert current == new == True


def test_user_swap_2():
    """Checks player 2 to player 1"""
    player_1 = player.Player(False, True)
    player_2 = player.Player(True, True)
    current = player_2.turn
    game_functions.swap_player(player_1, player_2)
    new = player_1.turn
    assert current == new == True


def test_drop_location_1():
    """Checks drop location is correct"""
    location = game_functions.drop_location((900, 200))
    assert location == (1, 6)


def test_drop_location_2():
    """Checks drop location is correct"""
    location = game_functions.drop_location((400, 400))
    assert location == (3, 1)


def test_adjacent_1():
    """Checks no mill is present"""
    test_grid = game_functions.create_board()
    assert game_functions.check_adjacent(x=0, y=0, board=test_grid, p=1) == 0


def test_adjacent_2():
    """Checks horizontal mill"""
    test_grid = game_functions.board.Board()
    test_grid = test_grid.create_board()
    test_grid[0][0] = 1
    test_grid[0][3] = 1
    test_grid[0][6] = 1

    assert game_functions.check_adjacent(x=0, y=6, board=test_grid, player_piece=1) == 1


def test_adjacent_3():
    """Checks vertical mill"""
    test_grid = board.Board()
    test_grid = test_grid.create_board()
    test_grid[2][2] = 2
    test_grid[3][2] = 2
    test_grid[4][2] = 2

    assert game_functions.check_adjacent(x=4, y=2, board=test_grid, player_piece=2) == 1

