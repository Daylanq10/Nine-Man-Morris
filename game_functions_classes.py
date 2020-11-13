"""
Upsetti Spaghetti Coders
THIS FILE IS TO HOLD THE FUNCTIONS USED TO CREATE THE MAIN FILE AND GAME
SEPARATED FUNCTIONS FROM MAIN FILE TO ENABLE PYTEST
"""

"""
HAVING ISSUES WITH DOUBLE MILLS. THINK IT IS DUE TO SETTING OF NEW MILL IN ADJ CHECK AND THEN 
IN REMOVAL IT IS NOT CHANGING NEW MILL TO FALSE SINCE THERE IS STILL A MILL SOMEHOW
"""

import pygame
import pygame.freetype
import pygame_menu
import copy
import board
import player

pygame.init()

# Color codes for consistent use
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
dark_green = (0, 111, 2)
blue = (0, 0, 200)
dark_blue = (0, 4, 126)
black = (0, 0, 0)
orange = (255, 165, 0)

# Distances for consistency
WIDTH = 1000
HEIGHT = 800
MARGIN = 25
LEFT_D = 250
TOP_D = 50
BLOCK_SIZE = 75

# Works with pygame.freetype import to allow easier display of words to screen
GAME_FONT = pygame.freetype.Font(None, 24)
STAT_FONT = pygame.freetype.Font(None, 20)


def menu():
    """
    This creates the menu and allows for different game options
    """

    # Run until the user asks to quit
    menu_view = True
    while menu_view:
        # Did the user click the window close button?
        for event in pygame.event.get():  # User did something
            print(event)
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit()  # Flag that we are done so we exit this loop
                quit()  # This exits pygame all together

        # Sets screen to correct dimensions
        surface = pygame.display.set_mode((WIDTH, HEIGHT))

        # Menu setup
        menu_screen = pygame_menu.Menu(
            HEIGHT, WIDTH, 'NINE-MEN\'S-MORRIS', theme=pygame_menu.themes.THEME_DARK)

        # These are for all the buttons on the menu and corresponding functions
        # TO POSSIBLY IMPLEMENT SCORE KEEPING FROM DATABASE?
        menu_screen.add_text_input('Name: ', default='John Doe')
        menu_screen.add_button('Play Computer', computer_game)
        menu_screen.add_button('2-Player Game', two_player_game)
        menu_screen.add_button('Quit', pygame_menu.events.EXIT)

        # Loops until choice is made
        menu_screen.mainloop(surface)


def drop_location(location: tuple) -> tuple:
    """
    This finds the clicked coordinates on the screen and places them in an ordered pair of coordinates
    while also allowing to click the menu button
    """

    # These are clicked location coordinates
    x = location[0]
    y = location[1]

    # THIS ALL FINDS THE Columns TO USE
    if (y > 650) and (y < 725):
        x_location = 6
    elif (y > 550) and (y < 625):
        x_location = 5
    elif (y > 450) and (y < 525):
        x_location = 4
    elif (y > 350) and (y < 425):
        x_location = 3
    elif (y > 250) and (y < 325):
        x_location = 2
    elif (y > 150) and (y < 225):
        x_location = 1
    elif (y > 50) and (y < 125):
        x_location = 0
    else:
        x_location = -1

    # THIS ALL FINDS THE ROWS TO USE
    if (x > 250) and (x < 325):
        y_location = 0
    elif (x > 350) and (x < 425):
        y_location = 1
    elif (x > 450) and (x < 525):
        y_location = 2
    elif (x > 550) and (x < 625):
        y_location = 3
    elif (x > 650) and (x < 725):
        y_location = 4
    elif (x > 750) and (x < 825):
        y_location = 5
    elif (x > 850) and (x < 925):
        y_location = 6
    else:
        y_location = -1

    # This takes you to the menu function
    if (x > 35) and (x < 115) and (y > 450) and (y < 500):
        menu()

    # Returns made ordered pair coordinates for game use
    # for now not correctly formatting should be (y,x) to be consistent
    location = (x_location, y_location)
    return location


def swap_player(first_player: player.Player, second_player: player.Player) -> player.Player:
    """
    If a turn was taken which leaves a remainder on the total moves of the game then player_2 is up
    Otherwise player_1 is up
    """
    if first_player.moves == second_player.moves:
        return first_player
    else:
        return second_player


# Function that checks for the creation of a new mill given a piece has just been played
# Should be called with the x and y coordinates of the point just played, and the game board
# Returns true if it finds a mill, returns false if not
def check_adjacent(x: int, y: int, game_board: board.Board, current_player: player.Player) -> int:
    """
    This checks for adjacent items in the board for mills and returns the number of mills found from the
    last placed move for the current player
    """

    mill = 0
    row = []
    col = []

    # Compile the playable points of the row
    for i in range(0, 7):
        if game_board.grid[x][i] >= 0:
            row.append(game_board.grid[x][i])

    # If the row was the middle row, cut it down to the 3 adjacent points
    if len(row) == 6:
        if y < 3:
            row = row[:3]
        else:
            row = row[3:]

    # Compile the playable points of the column
    for i in range(0, 7):
        if game_board.grid[i][y] >= 0:
            col.append(game_board.grid[i][y])

    # If the column was the middle column, cut it down to the 3 adjacent points
    if len(col) == 6:
        if x < 3:
            col = col[:3]
        else:
            col = col[3:]

    # Check if the 3 of the row are all the same and match the selected player, if so, there is a mill
    if row[0] == row[1] == row[2] == current_player.number:
        mill += 1

    # Check if the 3 of the column are all the same and match the selected player, if so, there is a mill
    if col[0] == col[1] == col[2] == current_player.number:
        mill += 1

    # If a new mill has been formed then new_mill for current player is set ot true
    # This allows for the remove_piece function to be called later
    if mill > 0:
        current_player.new_mill = True

    # Return how many mills were found
    return mill


# finds adjacent moves in phase 2
def find_moves(location: tuple):
    """
    Finds adjacent moves that are playable for phase 2 and returns a list of playable spots
    """
    # checks the location and adds it as a move, which will highlight it in add
    if location == (0, 0):
        return [(0, 3), (3, 0)]

    if location == (3, 0):
        return [(0, 0), (6, 0), (3, 1)]

    if location == (6, 0):
        return [(6, 3), (3, 0)]

    if location == (1, 1):
        return [(1, 3), (3, 1)]

    if location == (3, 1):
        return [(1, 1), (3, 0), (5, 1), (3, 2)]

    if location == (5, 1):
        return [(5, 3), (3, 1)]

    if location == (2, 2):
        return [(2, 3), (3, 2)]

    if location == (3, 2):
        return [(2, 2), (3, 1), (4, 2)]

    if location == (4, 2):
        return [(4, 3), (3, 2)]

    if location == (0, 3):
        return [(0, 0), (0, 6), (1, 3)]

    if location == (1, 3):
        return [(0, 3), (2, 3), (1, 1), (1, 5)]

    if location == (2, 3):
        return [(2, 2), (2, 4), (1, 3)]

    if location == (4, 3):
        return [(4, 2), (4, 4), (5, 3)]

    if location == (5, 3):
        return [(5, 1), (4, 3), (6, 3), (5, 5)]

    if location == (6, 3):
        return [(6, 0), (6, 6), (5, 3)]

    if location == (2, 4):
        return [(2, 3), (3, 4)]

    if location == (3, 4):
        return [(2, 4), (3, 5), (4, 4)]

    if location == (4, 4):
        return [(3, 4), (4, 3)]

    if location == (1, 5):
        return [(1, 3), (3, 5)]

    if location == (3, 5):
        return [(1, 5), (5, 5), (3, 4), (3, 6)]

    if location == (5, 5):
        return [(5, 3), (3, 5)]

    if location == (0, 6):
        return [(0, 3), (3, 6)]

    if location == (3, 6):
        return [(0, 6), (3, 5), (6, 6)]

    if location == (6, 6):
        return [(6, 3), (3, 6)]


def place_piece(game_board: board.Board, location: tuple, current_player: player.Player):
    """
    This allows for the current player to place their game piece/check mills/change game totals
    This is for phase 1
    """

    # If location in not usable then pass through function
    # Set tile to current player
    game_board.grid[location[0]][location[1]] = current_player.number
    # Decrement placement token and increment board token
    current_player.start_tokens -= 1
    current_player.board_tokens += 1
    current_player.inc_moves()
    # Check if this created a mill and how many
    if check_adjacent(location[0], location[1], game_board, current_player) > 0:
        # Add mill/s to player
        current_player.mills += check_adjacent(location[0], location[1], game_board, current_player)


def move_piece(game_board: board.Board, location: tuple, current_player: player.Player):
    """
    Allows the player to move a selected peice for phase 2
    """
    # if location is usable and another piece is not already selected,
    # finds valid moves saved to
    if game_board.grid[location[0]][location[1]] == current_player.number and current_player.past_possible == []:
        positions = find_moves(location)
        current_player.clicked_pos = location
        for item in positions:
            if game_board.grid[item[0]][item[1]] == 0:
                current_player.past_possible.append(item)
                game_board.grid[item[0]][item[1]] = current_player.number * 10

    # this covers for clicking on a spot and removing the possible moves and selecting another spot to move from
    elif location == current_player.clicked_pos:
        for item in current_player.past_possible:
            if item[0] != location[0] or item[1] != location[1]:
                game_board.grid[item[0]][item[1]] = 0

        current_player.past_possible = []
        current_player.clicked_pos = None

    # If a spot has been clicked on this allows for clicking on possible positions to move piece
    elif game_board.grid[location[0]][
        location[1]] == current_player.number * 10 and location in current_player.past_possible:
        game_board.grid[location[0]][location[1]] = current_player.number
        game_board.grid[current_player.clicked_pos[0]][current_player.clicked_pos[1]] = 0
        for item in current_player.past_possible:
            if item[0] != location[0] or item[1] != location[1]:
                game_board.grid[item[0]][item[1]] = 0
        current_player.past_possible = []
        if check_adjacent(location[0], location[1], game_board, current_player) > 0:
            # Add mill/s to player
            current_player.mills += check_adjacent(location[0], location[1], game_board, current_player)
        # move has been made so resetting stats for current player
        current_player.clicked_pos = None
        current_player.past_possible = []
        current_player.inc_moves()


def fly_piece(game_board: board.Board, location: tuple, current_player: player.Player):
    """
    Allows a player to have a selected piece 'fly' for phase 3
    """
    # if location is usable and another piece isnt already selected, finds valid moves, saves location, and triggers selection
    if game_board.grid[location[0]][location[1]] == current_player.number and current_player.past_possible == []:
        for i in range(7):
            for j in range(7):
                if game_board.grid[i][j] == 0:
                    current_player.past_possible.append((i, j))
                    game_board.grid[i][j] = current_player.number * 10
        current_player.clicked_pos = location

    # this covers for clicking on a spot and removing the possible moves and selecting another spot to move from
    elif location == current_player.clicked_pos:
        for item in current_player.past_possible:
            if item[0] != location[0] or item[1] != location[1]:
                game_board.grid[item[0]][item[1]] = 0

        current_player.past_possible = []
        current_player.clicked_pos = None

        # If a spot has been clicked on this allows for clicking on possible positions to move piece
    elif game_board.grid[location[0]][location[1]] == current_player.number * 10 and location in current_player.past_possible:
        game_board.grid[location[0]][location[1]] = current_player.number
        game_board.grid[current_player.clicked_pos[0]][current_player.clicked_pos[1]] = 0
        for item in current_player.past_possible:
            if item[0] != location[0] or item[1] != location[1]:
                game_board.grid[item[0]][item[1]] = 0
        current_player.past_possible = []
        if check_adjacent(location[0], location[1], game_board, current_player) > 0:
            # Add mill/s to player
            current_player.mills += check_adjacent(location[0], location[1], game_board, current_player)
        # move has been made so resetting stats for current player
        current_player.clicked_pos = None
        current_player.past_possible = []
        current_player.inc_moves()


def update_grid(game_board: board.Board, location: tuple, current_player: player.Player):
    """
    This changes the game grid with a 1 for player 1 and a 2 for player 2
    """

    ####STAGE 1####
    if current_player.start_tokens != 0:

        if (location[0] < 0) or (location[1] < 0):
            pass

        elif game_board.grid[location[0]][location[1]] == 0:
            place_piece(game_board, location, current_player)

    ####STAGE 2####
    elif current_player.start_tokens == 0 and current_player.board_tokens > 3:

        if (location[0] < 0) or (location[1] < 0):
            pass

        else:
            move_piece(game_board, location, current_player)

    ####STAGE 3####
    elif current_player.start_tokens == 0 and current_player.board_tokens == 3:

        if (location[0] < 0) or (location[1] < 0):
            pass

        else:
            fly_piece(game_board, location, current_player)

    game_board.display()
    print("Clicked location ->", "(" + str(location[1]) + "," + str(location[0]) + ")")
    print("This moves player ->", current_player.number)
    print("Start Tokens ->", current_player.start_tokens, "\nTotal Tokens ->", current_player.get_total_tokens(),
          "\nBoard Tokens ->", current_player.board_tokens, "\nMills ->", current_player.mills, "\nMove ->",
          current_player.moves)


def remove_piece(game_board: board.Board, location: tuple,
                 current_player: player.Player, first_player: player.Player, second_player: player.Player):
    """
    Checks if the current player is player_1 or player_2 and then removes a piece of the other players board pieces
    Takes into account the game conditions of piece removal
    Cannot remove a piece that is in an opposing players mills unless that is only optional move
    """

    # If a mill just occurred and a piece is about to be removed
    removable = True

    # If location in not usable then pass through function
    if (location[0] < 0) or (location[1] < 0):
        pass

    if current_player.number == 1:
        opposing_player = second_player
    else:
        opposing_player = first_player

    # If location has a player 2 tile and this is player 1
    if game_board.grid[location[0]][location[1]] == opposing_player.number:

        # If the piece being removed has mill/s
        if check_adjacent(location[0], location[1], game_board, opposing_player) > 0:
            # If the number of mills don't match placed tokens
            if opposing_player.mills / opposing_player.board_tokens < .30:
                removable = False
            # If there is a stacked mill check to see if there is a loose token
            else:
                for i in range(0, 7):
                    for j in range(0, 7):
                        if game_board.grid[i][j] == opposing_player.number:
                            if check_adjacent(i, j, game_board, opposing_player) == 0:
                                removable = False

        # If it passes the test
        if removable:

            current_player.new_mill = False

            # Check how many mills will be removed and take them from player
            if check_adjacent(location[0], location[1], game_board, opposing_player) > 0:
                opposing_player.mills -= check_adjacent(location[0], location[1], game_board, opposing_player)
            # Set tile to empty
            game_board.grid[location[0]][location[1]] = 0
            # Remove token from Player 2
            opposing_player.board_tokens -= 1


def playable(game_board: board.Board, first_player: player.Player, second_player: player.Player) -> bool:
    """
    This checks the board with the current player and uses find_moves to determine if there is a playable move.
    Returns true if there is a playable move and false if there is not.
    Using import of copy to make deepcopy
    """
    """
    # Dictates which piece to look for
    if first_player.turn:
        piece = 1
    if second_player.turn:
        piece = 2

    # Counter to determine if playable spots are avaliable
    play_spot = 0

    temp_board = copy.deepcopy(board)

    # Checks for pieces that are playable and uses find_moves
    for row in range(7):
        for col in range(7):
            if temp_board.grid[row][col] == piece:
                find_moves(temp_board, (row, col))

    # If find_moves placed 3 on grid then increment counter
    for row in temp_board.grid:
        if 3 in row:
            play_spot += 1

    if play_spot > 0:
        return True
    else:
        return False
        """
    pass


def display_stats(current_player: player.Player, first_player: player.Player, second_player:player.Player):
    """
    This takes into account whose turn is coming next. It is set to the next turn because the swap_player
    function does not update until the next iteration of the game update. Ensured to start player 1.
    """
    if current_player.number == 1 and current_player.board_tokens == 0:
        upcoming_player = current_player
        player_turn = "Player 1's turn"
        color = green

    elif current_player.number == 1:
        upcoming_player = second_player
        player_turn = "Player 2's turn"
        color = blue

    else:
        upcoming_player = first_player
        player_turn = "Player 1's turn"
        color = green

    if current_player.start_tokens != 0:
        current_player.stage = "Stage 1: Placing"
    elif current_player.start_tokens == 0 and upcoming_player.board_tokens > 3:
        current_player.stage = "Stage 2: Moving"
    elif current_player.start_tokens == 0 and upcoming_player.board_tokens == 3:
        current_player.stage = "Stage 3: Flying"

    # If stage one
    if current_player.stage == "Stage 1: Placing":
        # Set strings for board and place tokens
        player_start_tokens = "Pieces to Place:   " + \
                              str(upcoming_player.start_tokens)  # Displays placing tokens
        player_board_tokens = "Pieces on Board: " + \
                              str(upcoming_player.board_tokens)  # Displays board tokens
        # Displays players turn
        STAT_FONT.render_to(
            screen, (90, 300), player_turn, (100, 100, 100))
        # Displays players token avatar
        pygame.draw.rect(screen, color, (40, 290, 40, 40))
        # Displays players start token
        STAT_FONT.render_to(
            screen, (40, 350), player_start_tokens, (100, 100, 100))
        # Displays players board token
        STAT_FONT.render_to(
            screen, (40, 400), player_board_tokens, (100, 100, 100))
        # Displays current stage
        GAME_FONT.render_to(
            screen, (40, 50), current_player.stage, (100, 100, 100))
    # Else for both stage 2 or 3
    elif current_player.stage == "Stage 2: Moving" or upcoming_player.stage == "Stage 3: Flying":
        # Set strings for board tokens
        player_board_tokens = "Pieces left: " + \
                              str(upcoming_player.board_tokens)  # Displays board tokens
        # Displays players turn
        STAT_FONT.render_to(
            screen, (90, 350), player_turn, (100, 100, 100))
        # Displays players token avatar
        pygame.draw.rect(screen, color, (40, 340, 40, 40))
        # Displays players board token
        STAT_FONT.render_to(
            screen, (40, 400), player_board_tokens, (100, 100, 100))
        # Displays current stage
        GAME_FONT.render_to(
            screen, (40, 50), current_player.stage, (100, 100, 100))
    elif current_player.stage == "Game Over: no moves" or current_player.stage == "Game Over":
        # Displays a popup endgame message

        """
        if current_player.stage == "Game Over":
            pass
            # FIGURE OUT WHAT TO DO HERE
            printout = str(other.get_total_tokens()) + " to 2!"

        else:
            printout = "No playable moves!"
        if player.number:
            STAT_FONT.render_to(
                screen, (40, 350), "Player 2 Wins " + printout, (100, 100, 100))
        else:
            STAT_FONT.render_to(
                screen, (40, 350), "Player 1 Wins " + printout, (100, 100, 100))
        STAT_FONT.render_to(
            screen, (40, 400), "Hit menu to exit!", (100, 100, 100))
        # Displays current stage of Game Over
        GAME_FONT.render_to(
            screen, (40, 50), current_player.stage, (100, 100, 100))
            """


def two_player_game():
    """
    This is where the output and logic is put together to create a two player game
    """
    # Creates game board (if menu is visited then resets board -> can be changed if needed)
    game_board = board.Board()

    # Shows board in console for developer use
    game_board.display()

    # Create both players
    player_1 = player.Player(1, True)
    player_2 = player.Player(2, True)

    # for start of game purpose
    player_to_use = player_1

    # Sets standard for screen dimensions
    global screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Run until the user asks to quit
    running = True
    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                running = False  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # print("Click ->", pos)    # Commented this because it was getting annoying

                # This is used if a new mill was formed so action can be taken to remove a piece
                if player_1.new_mill or player_2.new_mill:  # Checks if that move made a mill
                    pos = pygame.mouse.get_pos()
                    remove_piece(game_board, drop_location(pos), player_to_use, player_1, player_2)

                # This is a standard move
                else:
                    # Updates game grid in console
                    player_to_use = swap_player(player_1, player_2)
                    update_grid(game_board, drop_location(pos), player_to_use)

        # This outputs the game grid from the console to screen with correct coordinates

        # Resets screen so things can be changed in between frames
        screen.fill(black)

        # draw various board components
        # outer rectangle
        pygame.draw.rect(screen, (150, 150, 150), (285, 85, 605, 605), 3)

        # middle rectangle
        pygame.draw.rect(screen, (150, 150, 150), (385, 185, 405, 405), 3)

        # inner rectangle
        pygame.draw.rect(screen, (150, 150, 150), (485, 285, 205, 205), 3)

        # lines
        pygame.draw.line(screen, (150, 150, 150), (585, 85), (585, 285), 3)
        pygame.draw.line(screen, (150, 150, 150), (585, 485), (585, 685), 3)
        pygame.draw.line(screen, (150, 150, 150), (250, 385), (485, 385), 3)
        pygame.draw.line(screen, (150, 150, 150), (685, 385), (885, 385), 3)

        # Draw the board
        for x in range(7):
            for y in range(7):
                rect = pygame.Rect(x * (BLOCK_SIZE + MARGIN) + LEFT_D, y * (BLOCK_SIZE + MARGIN) + TOP_D, BLOCK_SIZE,
                                   BLOCK_SIZE)

                # If usable spot place white square
                if game_board.grid[y][x] == 0:
                    pygame.draw.rect(screen, white, rect)

                # If player 1 spot place green square
                if game_board.grid[y][x] == 1:
                    pygame.draw.rect(screen, green, rect)

                # If player 1 selected spot place dark green square
                if game_board.grid[y][x] == 10:
                    pygame.draw.rect(screen, dark_green, rect)

                # If player 2 spot place blue square
                if game_board.grid[y][x] == 2:
                    pygame.draw.rect(screen, blue, rect)

                # If player 2 selected spot place dark blue square
                if game_board.grid[y][x] == 20:
                    pygame.draw.rect(screen, dark_blue, rect)

                # empty cells that a player can move to in phase two are assigned 3
                if game_board.grid[y][x] == 3:
                    pygame.draw.rect(screen, orange, rect)

        # used for output of data
        display_stats(player_to_use, player_1, player_2)

        # if mill_check, display text, needs remove piece function
        if player_to_use.new_mill:
            GAME_FONT.render_to(screen, (25, 150), " Mill found!", white)

        # This is to output the menu button
        pygame.draw.rect(screen, white, (40, 450, 80, 40))
        GAME_FONT.render_to(screen, (50, 460), "Menu", (100, 100, 100))

        pygame.display.flip()


def computer_game():
    """
    This will be used for future game mode to play against computer
    """
    pass
