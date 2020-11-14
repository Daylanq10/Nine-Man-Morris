import game_functions
import board
import player


def test_player_1_first_click():
    """Test if chosen for player 1 spot makes adjacent spots 10"""
    test_grid = board.Board()
    # board with all pieces placed and moving phase to begin
    test_grid.grid = [[1, -1, -1, 2, -1, -1, 1],
                      [-1, 2, -2, 1, -2, 2, -1],
                      [-1, -2, 2, 0, 0, -2, -1],
                      [2, 1, 0, -3, 0, 1, 2],
                      [-1, -2, 0, 0, 1, -2, -1],
                      [-1, 2, -2, 1, -2, 2, -1],
                      [1, -1, -1, 2, -1, -1, 1]]

    player_1 = player.Player(1, True)
    player_1.start_tokens = 0
    player_1.board_tokens = 9
    player_1.moves = 9

    game_functions.move_piece(test_grid, (4, 4), player_1)

    assert test_grid.grid == [[1, -1, -1, 2, -1, -1, 1],
                              [-1, 2, -2, 1, -2, 2, -1],
                              [-1, -2, 2, 0, 0, -2, -1],
                              [2, 1, 0, -3, 10, 1, 2],
                              [-1, -2, 0, 10, 1, -2, -1],
                              [-1, 2, -2, 1, -2, 2, -1],
                              [1, -1, -1, 2, -1, -1, 1]]

    assert player_1.moves == 9
    assert player_1.past_possible == [(4, 3), (3, 4)] or [(3, 4), (4, 3)]
    assert player_1.clicked_pos == (4, 4)


def test_player_1_reclick_position():
    """Test if chosen for player 1 spot makes adjacent spots 10"""
    test_grid = board.Board()
    # board with all pieces placed and location (4,4) already clicked
    test_grid.grid = [[1, -1, -1, 2, -1, -1, 1],
                      [-1, 2, -2, 1, -2, 2, -1],
                      [-1, -2, 2, 0, 0, -2, -1],
                      [2, 1, 0, -3, 10, 1, 2],
                      [-1, -2, 0, 10, 1, -2, -1],
                      [-1, 2, -2, 1, -2, 2, -1],
                      [1, -1, -1, 2, -1, -1, 1]]

    player_1 = player.Player(1, True)
    player_1.start_tokens = 0
    player_1.board_tokens = 9
    player_1.moves = 9
    player_1.past_possible = [(4, 3), (3, 4)]
    player_1.clicked_pos = (4, 4)

    game_functions.move_piece(test_grid, (4, 4), player_1)

    assert test_grid.grid == [[1, -1, -1, 2, -1, -1, 1],
                              [-1, 2, -2, 1, -2, 2, -1],
                              [-1, -2, 2, 0, 0, -2, -1],
                              [2, 1, 0, -3, 0, 1, 2],
                              [-1, -2, 0, 0, 1, -2, -1],
                              [-1, 2, -2, 1, -2, 2, -1],
                              [1, -1, -1, 2, -1, -1, 1]]

    assert player_1.moves == 9
    assert player_1.past_possible == []
    assert player_1.clicked_pos is None


def test_player_1_move_made():
    """Test if chosen for player 1 spot makes adjacent spots 10"""
    test_grid = board.Board()
    # board with all pieces placed and location (4,4) already clicked
    test_grid.grid = [[1, -1, -1, 2, -1, -1, 1],
                      [-1, 2, -2, 1, -2, 2, -1],
                      [-1, -2, 2, 0, 0, -2, -1],
                      [2, 1, 0, -3, 10, 1, 2],
                      [-1, -2, 0, 10, 1, -2, -1],
                      [-1, 2, -2, 1, -2, 2, -1],
                      [1, -1, -1, 2, -1, -1, 1]]

    player_1 = player.Player(1, True)
    player_1.start_tokens = 0
    player_1.board_tokens = 9
    player_1.moves = 9
    player_1.past_possible = [(4, 3), (3, 4)]
    player_1.clicked_pos = (4, 4)

    game_functions.move_piece(test_grid, (4, 3), player_1)

    assert test_grid.grid == [[1, -1, -1, 2, -1, -1, 1],
                              [-1, 2, -2, 1, -2, 2, -1],
                              [-1, -2, 2, 0, 0, -2, -1],
                              [2, 1, 0, -3, 0, 1, 2],
                              [-1, -2, 0, 1, 0, -2, -1],
                              [-1, 2, -2, 1, -2, 2, -1],
                              [1, -1, -1, 2, -1, -1, 1]]

    assert player_1.past_possible == []
    assert player_1.clicked_pos is None
    assert player_1.moves == 10


