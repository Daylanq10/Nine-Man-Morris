"""
Upsetti Spaghetti Coders
THIS FILE IS FOR TESTING CHECK_ADJACENT FUNCTION USING PYTEST
IF USING PYCHARM MAKE SURE TO SET PYTEST AS DEFAULT TESTING IN PREFERENCES
"""

import player


def test_decrement_of_player():
    """Test that the player object start pieces can decrement
    and player object board pieces can increment"""
    player_1 = player.Player(True, True)

    player_1.start_tokens -= 1
    player_1.board_tokens += 1

    assert player_1.start_tokens == 8
    assert player_1.board_tokens == 1
