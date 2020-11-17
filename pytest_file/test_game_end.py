"""
Upsetti Spaghetti Coders
THIS FILE IS FOR TESTING CHECK_ADJACENT FUNCTION USING PYTEST
IF USING PYCHARM MAKE SURE TO SET PYTEST AS DEFAULT TESTING IN PREFERENCES
"""

"""Not sure how to approach this. Player objects could have winning variable inside maybe"""

import game_functions
import player


def game_end_player1_wins_no_moves():
    """The game has ended and player 1 wins"""

    player_turn = "Player 1's Turn"
    stage = "Game Over: no moves"
    player_1 = player.Player(True, True)

    game_functions.display_stats(player_turn, stage)

    # Nothing to assert. Tried strings created in display_stats but that does not reach outside function.
