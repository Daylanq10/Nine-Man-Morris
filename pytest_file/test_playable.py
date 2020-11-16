import game_functions
import board
import player


def test_no_movable_piece():
    """
    Player to place piece on board in top left corner
    """

    test_grid = board.Board()
    # board with all pieces placed and player 1 turn starts and no playable moves avaliable
    test_grid.grid = [[1, -1, -1, 2, -1, -1, 1],
                      [-1, 1, -2, 2, -2, 1, -1],
                      [-1, -2, 0, 0, 0, -2, -1],
                      [2, 2, 0, -3, 0, 2, 2],
                      [-1, -2, 0, 2, 0, -2, -1],
                      [-1, 1, -2, 2, -2, 1, -1],
                      [1, -1, -1, 2, -1, -1, 1]]

    player_1 = player.Player(1, True)
    player_2 = player.Player(2, True)
    player_1.moves = 9
    player_2.moves = 9
    player_1.board_tokens = 9
    player_2.board_tokens = 9
    player_1.start_tokens = 0
    player_2.start_tokens = 0
    player_1.board_positions = [(6, 0), (0, 0), (0, 6), (6, 6), (5, 1), (1, 1), (1, 5), (5, 5)]

    assert not game_functions.playable(test_grid, player_1)


def test_movable_piece():
    """
    Player to place piece on board in top left corner
    """

    test_grid = board.Board()
    # board with all pieces placed and player 1 turn starts and no playable moves avaliable
    test_grid.grid = [[1, -1, -1, 2, -1, -1, 1],
                      [-1, 1, -2, 2, -2, 1, -1],
                      [-1, -2, 0, 0, 0, -2, -1],
                      [2, 2, 0, -3, 0, 2, 2],
                      [-1, -2, 0, 2, 0, -2, -1],
                      [-1, 1, -2, 2, -2, 1, -1],
                      [1, -1, -1, 2, -1, -1, 1]]

    player_1 = player.Player(1, True)
    player_2 = player.Player(2, True)
    player_1.moves = 9
    player_2.moves = 9
    player_1.board_tokens = 9
    player_2.board_tokens = 9
    player_1.start_tokens = 0
    player_2.start_tokens = 0
    player_2.board_positions = [(3, 0), (0, 3), (3, 6), (6, 3), (3, 1), (1, 3), (3, 5), (5, 3), (4, 3)]

    assert game_functions.playable(test_grid, player_2)