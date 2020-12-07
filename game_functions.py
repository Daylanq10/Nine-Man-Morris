"""
Upsetti Spaghetti Coders
THIS FILE IS TO HOLD THE FUNCTIONS USED TO CREATE THE MAIN FILE AND GAME
SEPARATED FUNCTIONS FROM MAIN FILE TO ENABLE PYTEST
"""

"""
IN FIND_MOVES THERE ARE TWO UNUSED VARIABLES. NOT SURE IF IT IS AN ERROR OR IF THEY ARE JUST NOT NEEDED.
"""

"""
CANNOT GET TEST_CHANGE_PLAYER TO WORK. IT HAS TO DO WITH THE FACT THAT THE FUNCTION SWAP_PLAYER WORKS WITH GLOBAL 
VARIABLES AND I AM HAVING TROUBLE REPLICATING THAT IN PYTEST.  LOOK BELOW FOR UPDATED INFO.
"""

"""
IN ORDER FOR TEST_CHANGE_PLAYER TO WORK I HAD TO ADD VARIABLES OF PLAYER_1 AND PLAYER_2 TO SWAP_PLAYER FUNCTION.
EVERYTHING STILL WORKS AS IT DID BEFORE BUT I JUST WANT TO LET THAT BE KNOWN IN CASE IT EFFECTED SOMETHING
I DID NOT CATCH.  I LEFT ALL THE GLOBAL VARIABLES OF PLAYER_1 AND PLAYER_2 AND DID NOT MESS WITH THEM.
"""

"""
TESTING IS NOT COMPLETE BUT IS STARTED. TEST_PIECE_DECREMENT AND TEST_PIECE_PLACEMENT ARE NOT OPERATIONAL.
THERE ARE ISSUES WITH NESTED FUNCTIONS I BELIEVE THAT MAKES TESTING DIFFICULT
"""

"""
THE LOCATION OF DISPLAYING IN DISPLAY_STATS THAT SOMEONE HAS WON DUE TO THERE BEING NO MORE PLACEMENTS ON THE BOARD RUNS INTO 
THE ACUTAL GAME BOARD. NEEDS TO BE MOVED AROUND A LITTLE FOR PRETTIER GUI.
"""


# Initializing both players
from monte_carlo_computer import monte_carlo
import pygame
import pygame.freetype
import pygame_menu
import copy
import board
import player
player_1 = None
player_2 = None

# Holds check for if and how many mills was found
mill_check = None

# Creates array for board
arr = []

# Create previous points
last_x = 5
last_y = 5

TOKEN_ONE = 1
TOKEN_TWO = 2

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
TRAPPED_FONT = pygame.freetype.Font(None, 18)


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


def swap_player(player_1: player.Player, player_2: player.Player):
    """
    Swaps global variables of two players labeled player_1 and player_2
    """
    if player_1.turn:
        player_1.turn = False
        player_2.turn = True
    else:
        player_1.turn = True
        player_2.turn = False


# Function that checks for the creation of a new mill given a piece has just been played
# Should be called with the x and y coordinates of the point just played, and the game board
# Returns true if it finds a mill, returns false if not
def check_adjacent(x: int, y: int, board: board.Board, player_piece: int) -> int:
    """
    This checks for adjacent items in the board
    """

    mill = 0
    row = []
    col = []

    # Compile the playable points of the row
    for i in range(0, 7):
        if board.grid[x][i] >= 0:
            row.append(board.grid[x][i])

    # If the row was the middle row, cut it down to the 3 adjacent points
    if len(row) == 6:
        if y < 3:
            row = row[:3]
        else:
            row = row[3:]

    # Compile the playable points of the column
    for i in range(0, 7):
        if board.grid[i][y] >= 0:
            col.append(board.grid[i][y])

    # If the column was the middle column, cut it down to the 3 adjacent points
    if len(col) == 6:
        if x < 3:
            col = col[:3]
        else:
            col = col[3:]

    # Check if the 3 of the row are all the same and match the selected player, if so, there is a mill
    if row[0] == row[1] == row[2] == player_piece:
        mill += 1

    # Check if the 3 of the column are all the same and match the selected player, if so, there is a mill
    if col[0] == col[1] == col[2] == player_piece:
        mill += 1

    # Print in terminal for testing
    print("mills found ", mill)
    # Return how many mills were found
    return mill


# works with find_moves function, checks space, if valid changes color and adds it to/returns moves list
def add(board: board.Board, x: int, y: int):
    """
    If valid spot on board '0' then change to '3' for possible moves list
    """
    if board.grid[x][y] == 0:
        board.grid[x][y] = 3


# finds adjacent moves in phase 2
def find_moves(board: board.Board, location: tuple):
    """
    Finds adjacent moves that are playable for phase 2
    """
    row = []
    col = []
    x = location[0]
    y = location[1]

    # Compile the playable points of the row
    for i in range(0, 7):
        if board.grid[x][i] >= 0:
            row.append(board.grid[x][i])

    # If the row was the middle row, cut it down to the 3 adjacent points

    # THIS STATEMENT IS NOT USED
    if len(row) == 6:
        if y < 3:
            row = row[:3]
        else:
            row = row[3:]

    # Compile the playable points of the column
    for i in range(0, 7):
        if board.grid[i][y] >= 0:
            col.append(board.grid[i][y])

    # If the column was the middle column, cut it down to the 3 adjacent points

    # THIS STATEMENT IS NOT USED
    if len(col) == 6:
        if x < 3:
            col = col[:3]
        else:
            col = col[3:]

    # checks the location and adds it as a move, which will highlight it in add
    if location == (0, 0):
        add(board, 0, 3)
        add(board, 3, 0)

    if location == (3, 0):
        add(board, 0, 0)
        add(board, 6, 0)
        add(board, 3, 1)

    if location == (6, 0):
        add(board, 6, 3)
        add(board, 3, 0)

    if location == (1, 1):
        add(board, 1, 3)
        add(board, 3, 1)

    if location == (3, 1):
        add(board, 1, 1)
        add(board, 3, 0)
        add(board, 5, 1)
        add(board, 3, 2)

    if location == (5, 1):
        add(board, 5, 3)
        add(board, 3, 1)

    if location == (2, 2):
        add(board, 2, 3)
        add(board, 3, 2)

    if location == (3, 2):
        add(board, 2, 2)
        add(board, 3, 1)
        add(board, 4, 2)

    if location == (4, 2):
        add(board, 4, 3)
        add(board, 3, 2)

    if location == (0, 3):
        add(board, 0, 0)
        add(board, 0, 6)
        add(board, 1, 3)

    if location == (1, 3):
        add(board, 0, 3)
        add(board, 2, 3)
        add(board, 1, 1)
        add(board, 1, 5)

    if location == (2, 3):
        add(board, 2, 2)
        add(board, 2, 4)
        add(board, 1, 3)

    if location == (4, 3):
        add(board, 4, 2)
        add(board, 4, 4)
        add(board, 5, 3)

    if location == (5, 3):
        add(board, 5, 1)
        add(board, 4, 3)
        add(board, 6, 3)
        add(board, 5, 5)

    if location == (6, 3):
        add(board, 6, 0)
        add(board, 6, 6)
        add(board, 5, 3)

    if location == (2, 4):
        add(board, 2, 3)
        add(board, 3, 4)

    if location == (3, 4):
        add(board, 2, 4)
        add(board, 3, 5)
        add(board, 4, 4)

    if location == (4, 4):
        add(board, 3, 4)
        add(board, 4, 3)

    if location == (1, 5):
        add(board, 1, 3)
        add(board, 3, 5)

    if location == (3, 5):
        add(board, 1, 5)
        add(board, 5, 5)
        add(board, 3, 4)
        add(board, 3, 6)

    if location == (5, 5):
        add(board, 5, 3)
        add(board, 3, 5)

    if location == (0, 6):
        add(board, 0, 3)
        add(board, 3, 6)

    if location == (3, 6):
        add(board, 0, 6)
        add(board, 3, 5)
        add(board, 6, 6)

    if location == (6, 6):
        add(board, 6, 3)
        add(board, 3, 6)


def place_piece(board: board.Board, location: tuple, player: player.Player, player_token: int):
    """
    This allows for the current player to place their game piece/check mills/change game totals
    This is for phase 1
    """
    global mill_check

    # If location in not usable then pass through function
    # Set tile to current player
    board.grid[location[0]][location[1]] = player_token
    # Decrement placement token and increment board token
    player.start_tokens -= 1
    player.board_tokens += 1
    # Check if this created a mill and how many
    if check_adjacent(location[0], location[1], board, player_token) > 0:
        # Set mill check
        mill_check = check_adjacent(
            location[0], location[1], board, player_token)
        # Add mill/s to player
        player.mills += mill_check
    # Swap players if a mill was not created
    else:
        swap_player(player_1, player_2)


def move_piece(board: board.Board, location: tuple, player: int):
    """
    Allows the player to move a selected peice for phase 2
    """
    global player_1
    global player_2
    global mill_check
    global last_x
    global last_y
    global selected

    if (location[0] < 0) or (location[1] < 0):
        pass

    # if location is usable and another piece is not already selected,
    # finds valid moves, saves location, and triggers selection
    elif board.grid[location[0]][location[1]] == player and not selected:
        find_moves(board, location)
        last_x = location[0]
        last_y = location[1]
        selected = True
        board.grid[location[0]][location[1]] *= 10

    # if you want to pick a different piece, just click the first piece and it will reset
    elif selected and board.grid[location[0]][location[1]] == player:
        selected = False
        for i in range(7):
            for j in range(7):
                if board.grid[i][j] == 3:
                    board.grid[i][j] = 0
                if board.grid[i][j] == 10 or board.grid[i][j] == 20:
                    board.grid[i][j] /= 10
        find_moves(board, location)
        last_x = location[0]
        last_y = location[1]
        selected = True
        board.grid[location[0]][location[1]] *= 10

        # if user selects a highlighted piece, then the piece moves, program checks for mills, and if none it swaps players
    elif board.grid[location[0]][location[1]] == 3:
        selected = False
        board.grid[location[0]][location[1]] = player
        board.grid[last_x][last_y] = 0
        mill_check = check_adjacent(location[0], location[1], board, player)
        for i in range(7):
            for j in range(7):
                if board.grid[i][j] == 3:
                    board.grid[i][j] = 0
                if board.grid[i][j] == 10 or board.grid[i][j] == 20:
                    board.grid[i][j] /= 10
        if mill_check == 0:
            swap_player(player_1, player_2)


def fly_piece(board: board.Board, location: tuple, player: int):
    """
    Allows a player to have a selected piece 'fly' for phase 3
    """
    global arr
    global player_1
    global player_2
    global mill_check
    global last_x
    global last_y
    global selected

    if (location[0] < 0) or (location[1] < 0):
        pass

    # if location is usable and another piece isnt already selected, finds valid moves, saves location, and triggers selection
    elif board.grid[location[0]][location[1]] == player and not selected:
        for i in range(7):
            for j in range(7):
                if board.grid[i][j] == 0:
                    board.grid[i][j] = 3
        last_x = location[0]
        last_y = location[1]
        selected = True
        board.grid[location[0]][location[1]] *= 10

    # if you want to pick a different piece, just click the first piece and it will reset
    elif selected and board.grid[location[0]][location[1]] == player:
        for i in range(7):
            for j in range(7):
                if board.grid[i][j] == 10 or board.grid[i][j] == 20:
                    board.grid[i][j] /= 10
        board.grid[location[0]][location[1]] *= 10

    # if user selects a highlighted piece, then the piece moves, program checks for mills, and if none it swaps players
    elif board.grid[location[0]][location[1]] == 3:
        selected = False
        board.grid[location[0]][location[1]] = player
        board.grid[last_x][last_y] = 0
        mill_check = check_adjacent(location[0], location[1], board, player)
        for i in range(7):
            for j in range(7):
                if board.grid[i][j] == 3:
                    board.grid[i][j] = 0
                if board.grid[i][j] == 10 or board.grid[i][j] == 20:
                    board.grid[i][j] /= 10
        if mill_check == 0:
            swap_player(player_1, player_2)


def update_grid(board: board.Board, location: tuple):
    """
    This changes the game grid with a 1 for player 1 and a 2 for player 2
    """
    # Declare global variables
    global arr
    global player_1
    global player_2
    global mill_check
    global last_x
    global last_y
    global selected

    # If there is currently not a mill
    if mill_check == 0:

        ####STAGE 1####
        # If the player has a token
        if player_1.start_tokens != 0 or player_2.start_tokens != 0:
            # If location in not usable then pass through function
            if (location[0] < 0) or (location[1] < 0):
                pass
            # if location is usable
            elif board.grid[location[0]][location[1]] == 0:
                print(board.grid[location[0]][location[1]])
                # If this is player 1
                if player_1.turn:
                    place_piece(board, location, player_1, TOKEN_ONE)

                # If this is player 2
                elif player_2.turn:
                    place_piece(board, location, player_2, TOKEN_TWO)

        ####STAGE 2####
        # If no start tokens begin to check board tokens for adjacency
        if player_1.turn and player_1.start_tokens == 0 and player_1.board_tokens > 3:
            move_piece(board, location, TOKEN_ONE)

        # Player 2 checking for adjacency after tokens are placed
        if player_2.turn and player_2.start_tokens == 0 and player_2.board_tokens > 3:
            move_piece(board, location, TOKEN_TWO)

        ####STAGE 3####
        # Flying phase player 1!
        if player_1.turn and player_1.start_tokens == 0 and player_1.board_tokens == 3:
            fly_piece(board, location, TOKEN_ONE)

        # Flying phase player 2!
        if player_2.turn and player_2.start_tokens == 0 and player_2.board_tokens == 3:
            fly_piece(board, location, TOKEN_TWO)

    # If a mill just occurred and a piece is about to be removed
    else:
        removable = True

        # If location in not usable then pass through function
        if (location[0] < 0) or (location[1] < 0):
            pass

        # If location has a player 2 tile and this is player 1
        elif board.grid[location[0]][location[1]] == 2 and player_1.turn:
            # Set found mills
            mill_check = check_adjacent(location[0], location[1], board, 2)
            # If the piece being removed has mill/s
            if mill_check > 0:
                # If the number of mills don't match placed tokens
                if player_2.mills / player_2.board_tokens < .30:
                    removable = False
                # If there is a stacked mill check to see if there is a loose token
                else:
                    for i in range(0, 7):
                        for j in range(0, 7):
                            if board.grid[i][j] == 2:
                                if check_adjacent(i, j, board, 2) == 0:
                                    removable = False

            # If it passes the test
            if removable:
                # Check how many mills will be removed and take them from player
                if mill_check > 0:
                    player_2.mills -= mill_check
                # Set tile to empty
                board.grid[location[0]][location[1]] = 0
                # Remove token from Player 2
                player_2.board_tokens -= 1
                # Swap players
                swap_player(player_1, player_2)
                # Set mill check to false now that it has occurred
                mill_check = 0

        # If location has a player 1 tile and this is player 2
        elif board.grid[location[0]][location[1]] == 1 and player_2.turn:
            # Set found mills
            mill_check = check_adjacent(location[0], location[1], board, 1)
            # If the piece being removed has mill/s
            if mill_check > 0:
                # If the number of mills don't match placed tokens
                if player_1.mills / player_1.board_tokens < .30:
                    removable = False
                # If there is a stacked mill check to see if there is a loose token
                else:
                    for i in range(0, 7):
                        for j in range(0, 7):
                            if board.grid[i][j] == 1:
                                if check_adjacent(i, j, board, 1) == 0:
                                    removable = False
            # If it passes the test
            if removable:
                # Check how many mills will be removed and take them from player
                if mill_check > 0:
                    player_1.mills -= mill_check
                # Set tile to empty
                board.grid[location[0]][location[1]] = 0
                # Remove token from Player 1
                player_1.board_tokens -= 1
                # Swap players
                swap_player(player_1, player_2)
                # Set mill check to false now that it has occurred
                mill_check = 0

    # Output board in console to see update made
    board.display()
    # Print click (x,y)
    print(location[1], location[0])
    # Print all tracked tokens and mills for each player
    print(player_1.start_tokens, player_1.get_total_tokens(),
          player_1.board_tokens, player_1.mills)
    print(player_2.start_tokens, player_2.get_total_tokens(),
          player_2.board_tokens, player_2.mills)


def playable(board: board.Board, first_player: player.Player, second_player: player.Player) -> bool:
    """
    This checks the board with the current player and uses find_moves to determine if there is a playable move.
    Returns true if there is a playable move and false if there is not.
    Using import of copy to make deepcopy
    """
    # Dictates which piece to look for
    if first_player.turn:
        piece = 1
    else:
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


def display_stats(turn: str, stage: str):
    """
    This takes into account whos turn it is and what stage that player is in and then displays for
    current player use.  Also holds win conditions for a player with less than 3 pieces left.
    """
    player_turn = turn
    # Set player and color
    if player_turn == "Player 1's Turn":
        player = player_1
        other = player_2
        color = green
    else:
        player = player_2
        other = player_1
        color = blue
    # If stage one
    if stage == "Stage 1: Placing":
        # Set strings for board and place tokens
        player_start_tokens = "Pieces to Place:   " + \
                              str(player.start_tokens)  # Displays placing tokens
        player_board_tokens = "Pieces on Board: " + \
                              str(player.board_tokens)  # Displays board tokens
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
            screen, (40, 50), stage, (100, 100, 100))
    # Else for both stage 2 or 3
    elif stage == "Stage 2: Moving" or stage == "Stage 3: Flying":
        # Set strings for board tokens
        player_board_tokens = "Pieces left: " + \
                              str(player.board_tokens)  # Displays board tokens
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
            screen, (40, 50), stage, (100, 100, 100))
    elif stage == "Game Over: no moves" or stage == "Game Over":
        # Displays a popup endgame message
        if stage == "Game Over":
            printout = str(other.get_total_tokens()) + " to 2!"
        else:
            printout = "No playable moves!"
        if player.number:
            STAT_FONT.render_to(
                screen, (40, 350), printout, (100, 100, 100))
            STAT_FONT.render_to(
                screen, (40, 400), "Player 2 Wins ", (100, 100, 100))
        else:
            STAT_FONT.render_to(
                screen, (40, 350), printout, (100, 100, 100))
            STAT_FONT.render_to(
                screen, (40, 400), "Player 1 Wins ", (100, 100, 100))
        # Displays current stage of Game Over
        TRAPPED_FONT.render_to(
            screen, (40, 50), stage, (100, 100, 100))


def two_player_game():
    """
    This is where the output and logic is put together to create a two player game
    """
    # Creates game board (if menu is visited then resets board -> can be changed if needed)
    game_board = board.Board()

    # Shows board in console for developer use
    game_board.display()

    # Create both players
    global player_1
    global player_2
    # Set it to player 1
    player_1 = player.Player(True, True)
    player_2 = player.Player(False, True)

    # Set / Reset the default of mill_check to false
    global mill_check
    mill_check = 0

    # Sets standard for screen dimensions
    global screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Sets current piece selection to false
    global selected
    selected = False

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
                # Updates game grid in console

                update_grid(game_board, drop_location(pos))

                if mill_check > 0:  # Checks if that move made a mill
                    # mill_check = True
                    print("Mill was found")  # Prints in terminal
                    pos = pygame.mouse.get_pos()
                    update_grid(game_board, drop_location(pos))
                print("Click ", pos)

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

        # If player 1 turn then output player 1
        if player_1.turn:
            player_turn = "Player 1's Turn"
            # If there are still tokens to place
            if player_1.start_tokens != 0:
                # Then stage 1 then display stats
                stage = "Stage 1: Placing"
            # If start tokens are empty but total tokens above three
            elif player_1.start_tokens == 0 and player_1.get_total_tokens() > 3:
                # Then stage 2 and display stats
                stage = "Stage 2: Moving"

                # This checks if there is a usable move for win condition
                movable = playable(game_board, player_1, player_2)
                if not movable:
                    stage = "Game Over: no moves"

            elif player_1.start_tokens == 0 and player_1.get_total_tokens() == 3:
                # Stage 3 and display stats
                stage = "Stage 3: Flying"
            else:
                # Win condition for less than 3 tokens available
                stage = "Game Over"

            display_stats(player_turn, stage)

        # If player 2 turn then output player 2
        else:
            player_turn = "Player 2's Turn"
            # If there are still tokens to place
            if player_2.start_tokens != 0:
                # Then stage 1 then display stats
                stage = "Stage 1: Placing"
            # If start tokens are empty but total tokens above three
            elif player_2.start_tokens == 0 and player_2.get_total_tokens() > 3:
                # Then stage 2 and display stats
                stage = "Stage 2: Moving"

                # This checks if there is a usable move for win condition
                movable = playable(game_board, player_1, player_2)
                if not movable:
                    stage = "Game Over: no moves"

            elif player_2.start_tokens == 0 and player_2.get_total_tokens() == 3:
                # Stage 3 and display stats
                stage = "Stage 3: Flying"
            else:
                # Win condition for less than 3 tokens available
                stage = "Game Over"

            display_stats(player_turn, stage)

        # if mill_check, display text, needs remove piece function
        if mill_check > 0:
            GAME_FONT.render_to(screen, (25, 150), " Mill found!", white)

        # This is to output the menu button
        pygame.draw.rect(screen, white, (40, 450, 80, 40))
        GAME_FONT.render_to(screen, (50, 460), "Menu", (100, 100, 100))

        pygame.display.flip()


def computer_game():

    pass
