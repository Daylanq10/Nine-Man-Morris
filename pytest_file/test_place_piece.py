"""
Upsetti Spaghetti Coders
THIS FILE IS FOR TESTING THAT A PLAYER CAN PLACE A PIECE USING PYTEST
IF USING PYCHARM MAKE SURE TO SET PYTEST AS DEFAULT TESTING IN PREFERENCES
"""

import game_functions_classes
import player
import board


def test_user_place_piece():
    """
    Player to place piece on board in top left corner
    """

    test_grid = board.Board()
    # board with all pieces placed and moving phase to begin
    test_grid.grid = [[0, -1, -1, 0, -1, -1, 0],
                      [-1, 0, -2, 0, -2, 0, -1],
                      [-1, -2, 0, 0, 0, -2, -1],
                      [0, 0, 0, -3, 0, 0, 0],
                      [-1, -2, 0, 0, 0, -2, -1],
                      [-1, 0, -2, 0, -2, 0, -1],
                      [0, -1, -1, 0, -1, -1, 0]]

    player_1 = player.Player(1, True)
    player_2 = player.Player(2, True)

    game_functions_classes.place_piece(test_grid, (1, 1), player_1)
    game_functions_classes.place_piece(test_grid, (0, 0), player_2)

    assert test_grid.grid == [[2, -1, -1, 0, -1, -1, 0],
                              [-1, 1, -2, 0, -2, 0, -1],
                              [-1, -2, 0, 0, 0, -2, -1],
                              [0, 0, 0, -3, 0, 0, 0],
                              [-1, -2, 0, 0, 0, -2, -1],
                              [-1, 0, -2, 0, -2, 0, -1],
                              [0, -1, -1, 0, -1, -1, 0]]

    assert player_1.start_tokens == 8
    assert player_2.start_tokens == 8
    assert player_1.board_tokens == 1
    assert player_2.board_tokens == 1
