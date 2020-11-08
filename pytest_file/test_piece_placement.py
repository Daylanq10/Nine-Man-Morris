"""
Upsetti Spaghetti Coders
THIS FILE IS FOR TESTING THAT A PLAYER CAN PLACE A PIECE USING PYTEST
IF USING PYCHARM MAKE SURE TO SET PYTEST AS DEFAULT TESTING IN PREFERENCES
"""

"""
DOES NOT WORK.
"""

import game_functions
import player
import board


def test_user_place_piece():
    """
    Player to place piece on board in top left corner
    """
    global player_1
    global player_2
    game_board = board.Board()
    player_1 = player.Player(True, True)
    player_2 = player.Player(False, True)
    game_functions.update_grid(board=game_board, location=(0,0))
    assert game_board.grid[0][0] == 1
