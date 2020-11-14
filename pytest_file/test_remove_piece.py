import game_functions_classes
import board
import player


def test_removal_no_mill():
    """Checks that player 2 piece will be removed from location (3,1)"""
    test_grid = board.Board()
    test_grid.grid = [[0, -1, -1, 0, -1, -1, 0],
                      [-1, 0, -2, 0, -2, 0, -1],
                      [-1, -2, 0, 0, 0, -2, -1],
                      [0, 2, 0, -3, 0, 0, 0],
                      [-1, -2, 0, 0, 0, -2, -1],
                      [-1, 0, -2, 0, -2, 0, -1],
                      [0, -1, -1, 0, -1, -1, 0]]

    player_1 = player.Player(1, True)
    player_2 = player.Player(2, True)

    game_functions_classes.remove_piece(test_grid, (3, 1), player_1, player_1, player_2)

    assert test_grid.grid == [[0, -1, -1, 0, -1, -1, 0],
                              [-1, 0, -2, 0, -2, 0, -1],
                              [-1, -2, 0, 0, 0, -2, -1],
                              [0, 0, 0, -3, 0, 0, 0],
                              [-1, -2, 0, 0, 0, -2, -1],
                              [-1, 0, -2, 0, -2, 0, -1],
                              [0, -1, -1, 0, -1, -1, 0]]


def test_removal_with_mill_other_piece_present():
    """Checks that player 2 piece will not be removed from (3,1) because mill is present and other piece on (6,0).
        Player 1 just created mill on (0,3).
    """
    test_grid = board.Board()
    test_grid.grid = [[0, -1, -1, 1, -1, -1, 0],
                      [-1, 0, -2, 1, -2, 0, -1],
                      [-1, -2, 0, 1, 0, -2, -1],
                      [2, 2, 2, -3, 0, 0, 0],
                      [-1, -2, 0, 0, 0, -2, -1],
                      [-1, 0, -2, 0, -2, 0, -1],
                      [2, -1, -1, 0, -1, -1, 0]]

    player_1 = player.Player(1, True)
    player_1.board_tokens = 3
    player_2 = player.Player(2, True)
    player_2.board_tokens = 4
    player_2.mills = 1
    player_2.mill_positions = [[(3, 0), (3, 1), (3, 2)]]

    # player 1 just created this mill
    game_functions_classes.check_adjacent(0, 3, test_grid, player_1)

    # attempts to click on a player 2 mill piece
    game_functions_classes.remove_piece(test_grid, (3, 1), player_1, player_1, player_2)

    # removal rejected and board is the same
    assert test_grid.grid == [[0, -1, -1, 1, -1, -1, 0],
                              [-1, 0, -2, 1, -2, 0, -1],
                              [-1, -2, 0, 1, 0, -2, -1],
                              [2, 2, 2, -3, 0, 0, 0],
                              [-1, -2, 0, 0, 0, -2, -1],
                              [-1, 0, -2, 0, -2, 0, -1],
                              [2, -1, -1, 0, -1, -1, 0]]

    assert player_1.mills == 1
    assert player_2.mills == 1
    assert player_1.board_tokens == 3
    assert player_2.board_tokens == 4
    assert player_2.mill_positions == [[(3, 0), (3, 1), (3, 2)]]


def test_removal_with_double_mill_in_play():
    """Checks that player 2 piece will not be removed from (3,1) because mill is present and other piece on (6,0).
        Player 1 just created mill on (0,3).
    """
    test_grid = board.Board()
    test_grid.grid = [[0, -1, -1, 1, -1, -1, 0],
                      [-1, 2, -2, 1, -2, 0, -1],
                      [-1, -2, 0, 1, 0, -2, -1],
                      [2, 2, 2, -3, 0, 0, 0],
                      [-1, -2, 0, 0, 0, -2, -1],
                      [-1, 2, -2, 0, -2, 0, -1],
                      [0, -1, -1, 1, -1, -1, 1]]

    player_1 = player.Player(1, True)
    player_1.board_tokens = 5
    player_2 = player.Player(2, True)
    player_2.board_tokens = 5
    player_2.mills = 2
    player_2.mill_positions = [[(3, 0), (3, 1), (3, 2)], [(1, 1), (3, 1), (5, 1)]]

    # player 1 just created this mill
    game_functions_classes.check_adjacent(0, 3, test_grid, player_1)

    # attempts to click on a player 2 mill piece
    game_functions_classes.remove_piece(test_grid, (3, 1), player_1, player_1, player_2)

    # removal rejected and board is the same
    assert test_grid.grid == [[0, -1, -1, 1, -1, -1, 0],
                              [-1, 2, -2, 1, -2, 0, -1],
                              [-1, -2, 0, 1, 0, -2, -1],
                              [2, 0, 2, -3, 0, 0, 0],
                              [-1, -2, 0, 0, 0, -2, -1],
                              [-1, 2, -2, 0, -2, 0, -1],
                              [0, -1, -1, 1, -1, -1, 1]]

    assert player_1.mills == 1
    assert player_2.mills == 0
    assert player_1.board_tokens == 5
    assert player_2.board_tokens == 4
    assert player_2.mill_positions == []
