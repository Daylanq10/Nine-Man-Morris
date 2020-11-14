import game_functions
import player
import board


def test_update_grid():
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

    game_functions.update_grid(test_grid, (0, 0), player_1)
    game_functions.update_grid(test_grid, (1, 1), player_2)

    game_functions.update_grid(test_grid, (0, 3), player_1)
    game_functions.update_grid(test_grid, (1, 3), player_2)

    game_functions.update_grid(test_grid, (0, 6), player_1)
    game_functions.update_grid(test_grid, (2, 3), player_2)

    assert test_grid.grid == [[1, -1, -1, 1, -1, -1, 1],
                              [-1, 2, -2, 2, -2, 0, -1],
                              [-1, -2, 0, 2, 0, -2, -1],
                              [0, 0, 0, -3, 0, 0, 0],
                              [-1, -2, 0, 0, 0, -2, -1],
                              [-1, 0, -2, 0, -2, 0, -1],
                              [0, -1, -1, 0, -1, -1, 0]]

    assert player_1.board_tokens == 3
    assert player_2.board_tokens == 3
    assert player_1.start_tokens == 6
    assert player_2.start_tokens == 6
    assert player_1.moves == 3
    assert player_2.moves == 3
