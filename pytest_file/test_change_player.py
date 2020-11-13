"""
Upsetti Spaghetti Coders
THIS FILE IS FOR TESTING PLAYER SWAPPING FUNCTION USING PYTEST
IF USING PYCHARM MAKE SURE TO SET PYTEST AS DEFAULT TESTING IN PREFERENCES
"""

import game_functions_classes
import player


def test_player_1():
    player_1 = player.Player(1, True)
    assert player_1.number == 1
    assert player_1.moves == 0


def test_user_swap_1_to_2():
    """Checks player 1 to player 2"""
    player_1 = player.Player(1, True)
    player_1.moves = 3
    player_2 = player.Player(2, True)
    player_2.moves = 2
    assert game_functions_classes.swap_player(player_1, player_2) == player_2


def test_user_swap_2_to_1():
    """Checks player 2 to player 1"""
    player_1 = player.Player(1, True)
    player_1.moves = 3
    player_2 = player.Player(2, True)
    player_2.moves = 3
    assert game_functions_classes.swap_player(player_1, player_2)
