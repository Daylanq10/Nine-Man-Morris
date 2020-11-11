"""
Upsetti Spaghetti Coders
THIS FILE IS FOR TESTING PLAYER SWAPPING FUNCTION USING PYTEST
IF USING PYCHARM MAKE SURE TO SET PYTEST AS DEFAULT TESTING IN PREFERENCES
"""

import game_functions
import player


def test_player_1():
    player_1 = player.Player(True, True)
    assert player_1.turn == True
    assert player_1.number == True


def test_user_swap_1_to_2():
    """Checks player 1 to player 2"""
    player_1 = player.Player(True, True)
    player_2 = player.Player(False, True)
    current = player_1.turn
    game_functions.swap_player(player_1, player_2)
    new = player_2.turn
    assert current == new == True


def test_user_swap_2_to_1():
    """Checks player 2 to player 1"""
    player_1 = player.Player(False, True)
    player_2 = player.Player(True, True)
    current = player_2.turn
    game_functions.swap_player(player_1, player_2)
    new = player_1.turn
    assert current == new == True
