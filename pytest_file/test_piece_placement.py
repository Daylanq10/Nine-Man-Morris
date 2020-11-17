"""
Upsetti Spaghetti Coders
THIS FILE IS FOR TESTING CHECK_ADJACENT FUNCTION USING PYTEST
IF USING PYCHARM MAKE SURE TO SET PYTEST AS DEFAULT TESTING IN PREFERENCES
"""

import game_functions
import board
import player

"""Global variables of player_1/player_2 disrupts testing"""


# Tried adding globals to testing and doesnt work
# global player_1
# global player_2

# Attempted this didn't work
# player_1 = player.Player(True, True)
# player_2 = player.Player(False, True)

def test_open_position_placement():
    """Test that the spot is open and can be used in location (0,0)"""
    test_board = board.Board()
    player_1 = player.Player(True, True)

    game_functions.place_piece(test_board, (0, 0), player_1, 1)

    assert player_1.start_tokens == 8
    assert player_1.board_tokens == 1
    assert test_board.grid == [[1, -1, -1, 0, -1, -1, 0],
                               [-1, 0, -2, 0, -2, 0, -1],
                               [-1, -2, 0, 0, 0, -2, -1],
                               [0, 0, 0, -3, 0, 0, 0],
                               [-1, -2, 0, 0, 0, -2, -1],
                               [-1, 0, -2, 0, -2, 0, -1],
                               [0, -1, -1, 0, -1, -1, 0]]


def test_closed_position_placement():
    """Test that the spot is occupied and cannot be used in location (0,0)"""
    """Player 2 pieces occupies (0,0) so Player_1 object remains the same"""
    test_board = board.Board()
    test_board.grid = [[2, -1, -1, 0, -1, -1, 0],
                       [-1, 0, -2, 0, -2, 0, -1],
                       [-1, -2, 0, 0, 0, -2, -1],
                       [0, 0, 0, -3, 0, 0, 0],
                       [-1, -2, 0, 0, 0, -2, -1],
                       [-1, 0, -2, 0, -2, 0, -1],
                       [0, -1, -1, 0, -1, -1, 0]]

    player_1 = player.Player(True, True)

    game_functions.place_piece(test_board, (0, 0), player_1, 1)

    assert player_1.start_tokens == 9
    assert player_1.board_tokens == 0
    assert test_board.grid == [[2, -1, -1, 0, -1, -1, 0],
                               [-1, 0, -2, 0, -2, 0, -1],
                               [-1, -2, 0, 0, 0, -2, -1],
                               [0, 0, 0, -3, 0, 0, 0],
                               [-1, -2, 0, 0, 0, -2, -1],
                               [-1, 0, -2, 0, -2, 0, -1],
                               [0, -1, -1, 0, -1, -1, 0]]
