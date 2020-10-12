"""
Upsetti Spaghetti Coders
THIS FILE IS FOR TESTING PURPOSES USING PYTEST
IF USING PYCHARM MAKE SURE TO SET PYTEST AS DEFAULT TESTING IN PREFERENCES
"""

import game_functons


def test_user_swap_1(current="Player_1"):
    """Checks player 1 to player 2"""
    new = game_functons.swap_player(current)
    assert new != current


def test_user_swap_2(current="Player_2"):
    """Checks player 2 to player 1"""
    new = game_functons.swap_player(current)
    assert new != current


def test_drop_location_1():
    """Checks drop location is correct"""
    location = game_functons.drop_location((900, 200))
    assert location == (1, 6)


def test_drop_location_2():
    """Checks drop location is correct"""
    location = game_functons.drop_location((400, 400))
    assert location == (3, 1)


def test_adjacent_1():
    """Checks no mill is present"""
    test_grid = game_functons.create_board()
    assert game_functons.check_adjacent(x=0, y=0, board=test_grid, player="Player_1") == 0


def test_adjacent_2():
    """Checks horizontal mill"""
    test_grid = game_functons.create_board()

    test_grid[0][0] = 1
    test_grid[0][3] = 1
    test_grid[0][6] = 1

    assert game_functons.check_adjacent(x=0, y=6, board=test_grid, player=1) == 1


def test_adjacent_3():
    """Checks vertical mill"""
    test_grid = game_functons.create_board()

    test_grid[2][2] = 2
    test_grid[3][2] = 2
    test_grid[4][2] = 2

    assert game_functons.check_adjacent(x=4, y=2, board=test_grid, player=2) == 1

