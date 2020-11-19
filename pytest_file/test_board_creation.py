"""
Upsetti Spaghetti Coders
THIS FILE IS FOR TESTING CHECK_ADJACENT FUNCTION USING PYTEST
IF USING PYCHARM MAKE SURE TO SET PYTEST AS DEFAULT TESTING IN PREFERENCES
"""

import board


def test_24_playable_positions():
    """Test that the game board is created correctly"""
    test_board = board.Board()
    playable = 0
    for x in range(7):
        for y in range(7):
            if test_board.grid[x][y] == 0:
                playable += 1

    # If there are 24 playable spots they will be represented by 0 in the grid
    assert playable == 24
    assert test_board.grid == [[0, -1, -1, 0, -1, -1, 0],
                               [-1, 0, -2, 0, -2, 0, -1],
                               [-1, -2, 0, 0, 0, -2, -1],
                               [0, 0, 0, -3, 0, 0, 0],
                               [-1, -2, 0, 0, 0, -2, -1],
                               [-1, 0, -2, 0, -2, 0, -1],
                               [0, -1, -1, 0, -1, -1, 0]]
