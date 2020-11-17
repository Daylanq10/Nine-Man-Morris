"""
Upsetti Spaghetti Coders
THIS FILE IS FOR TESTING CHECK_ADJACENT FUNCTION USING PYTEST
IF USING PYCHARM MAKE SURE TO SET PYTEST AS DEFAULT TESTING IN PREFERENCES
"""

import game_functions
import board
import player

"""Global variables of selected/player_1/player_2 disrupts testing"""


# Tried adding globals to testing and doesnt work
# global player_1
# global player_2
# global selected

# Attempted this didn't work
# player_1 = player.Player(True, True)
# player_2 = player.Player(False, True)
# selected = False

def test_movement_open_position():
    """Test that the moving phase allows a piece to be selected and show open positions"""
    test_board = board.Board()
    test_board.grid = [[1, -1, -1, 0, -1, -1, 1],
                       [-1, 0, -2, 0, -2, 0, -1],
                       [-1, -2, 0, 1, 0, -2, -1],
                       [0, 0, 0, -3, 0, 0, 0],
                       [-1, -2, 0, 0, 0, -2, -1],
                       [-1, 0, -2, 0, -2, 0, -1],
                       [1, -1, -1, 0, -1, -1, 1]]

    player_1 = player.Player(True, True)
    player_2 = player.Player(False, True)
    selected = False
    player_1.board_tokens = 5
    player_1.start_tokens = 0
    player_2.start_tokens = 0

    game_functions.move_piece(test_board, (0, 0), 1)

    # Possible places replaced 0 with 10
    assert test_board == [[1, -1, -1, 10, -1, -1, 1],
                          [-1, 0, -2, 0, -2, 0, -1],
                          [-1, -2, 0, 1, 0, -2, -1],
                          [10, 0, 0, -3, 0, 0, 0],
                          [-1, -2, 0, 0, 0, -2, -1],
                          [-1, 0, -2, 0, -2, 0, -1],
                          [1, -1, -1, 0, -1, -1, 1]]
