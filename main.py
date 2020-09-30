"""
Upsetti Spaghetti Coders
Kole Keeney, Chris Munns, Daylan Quinn and Greg Robson
9/28/20
CS 449

Nine Men's Morris main file
"""
import pygame
import pygame.freetype
import pygame_menu


def show_board(board: list):
    """
    This is used to show the contents of the board in the console
    """

    # Just a statement to print out a representation of the board
    for i in range(0, 7):
        print(board[i])


# Function that initializes the game board then returns it
def create_board():
    """
    This creates the board with usable and unusable coordinates
    """
    # Set the rows and the columns to 7
    row, col = (7, 7)

    # Create a 2D Array full of 0's with 7 rows and 7 columns
    arr = [[0 for i in range(row)] for j in range(col)]

    # Fill every non playable point with a -1
    arr[0][1] = -1
    arr[0][2] = -1
    arr[0][4] = -1
    arr[0][5] = -1
    arr[1][0] = -1
    arr[1][2] = -1
    arr[1][4] = -1
    arr[1][6] = -1
    arr[2][0] = -1
    arr[2][1] = -1
    arr[2][5] = -1
    arr[2][6] = -1
    arr[3][3] = -1
    arr[4][0] = -1
    arr[4][1] = -1
    arr[4][5] = -1
    arr[4][6] = -1
    arr[5][0] = -1
    arr[5][2] = -1
    arr[5][4] = -1
    arr[5][6] = -1
    arr[6][1] = -1
    arr[6][2] = -1
    arr[6][4] = -1
    arr[6][5] = -1

    # Return the new board
    return arr


def swap_player(current: str) -> str:
    """
    This swaps the player from player 1 to player 2
    """
    if current == "Player_1":
        return "Player_2"
    else:
        return "Player_1"


# Function that checks for the creation of a new mill given a piece has just been played
# Should be called with the x and y coordinates of the point just played, and the game board for arr
# Returns true if it finds a mill, returns false if not
def check_adjacent(x, y, arr):
    """
    This checks for adjacent items in the board
    """
    mill = False
    row = []
    col = []
    # Compile the playable points of the row
    for i in range(0, 7):
        if arr[x][i] is not -1:
            row.append(arr[x][i])

    # If the row was the middle row, cut it down to the 3 adjacent points
    if len(row) == 6:
        if y < 3:
            row = row[:3]
        else:
            row = row[3:]

    # Compile the playable points of the column
    for i in range(0, 7):
        if arr[i][y] is not -1:
            col.append(arr[i][y])

    # If the column was the middle column, cut it down to the 3 adjacent points
    if len(col) == 6:
        if x < 3:
            col = col[:3]
        else:
            col = col[3:]

    # Check if the 3 of the row are all the same, if so, there is a mill
    if row[0] == row[1] == row[2]:
        mill = True

    # Check if the 3 of the column are all the same, if so, there is a mill
    if col[0] == col[1] == col[2]:
        mill = True

    # Return if a mill was found
    return mill


def menu():
    """
    This creates the menu and allows for different game options
    """

    # Run until the user asks to quit
    menu = True
    while menu:
        # Did the user click the window close button?
        for event in pygame.event.get():  # User did something
            print(event)
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit()  # Flag that we are done so we exit this loop
                quit()  # This exits pygame all together

        # Sets screen to correct dimensions
        surface = pygame.display.set_mode((WIDTH, HEIGHT))

        # Menu setup
        menu = pygame_menu.Menu(HEIGHT, WIDTH, 'NINE-MAN-MORRIS', theme=pygame_menu.themes.THEME_DARK)

        # These are for all the buttons on the menu and corresponding functions
        menu.add_text_input('Name :', default='John Doe')  # TO POSSIBLY IMPLEMENT SCORE KEEPING FROM DATABASE?
        menu.add_button('Play Computer', computer_game)
        menu.add_button('2-Player Game', two_player_game)
        menu.add_button('Quit', pygame_menu.events.EXIT)

        # Loops until choice is made
        menu.mainloop(surface)


def drop_location(location: tuple) -> tuple:
    """
    This finds the clicked coordinates on the screen and places them in an ordered pair of coordinates
    while also allowing to click the menu button
    """

    # These are clicked location coordinates
    x = location[0]
    y = location[1]

    # THIS ALL FINDS THE ROW TO USE
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

    # THIS ALL FINDS THE COLUMN TO USE
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
    if (x > 35) and (x < 115) and (y > 390) and (y < 430):
        menu()

    # Returns made ordered pair coordinates for game use
    location = (x_location, y_location)
    return location


def update_grid(grid: list, location: tuple):
    """
    This changes the game grid with a 1 for player 1 and a 2 for player 2
    """
    global player

    # If location in not usable then pass through function
    if (location[0] == -1) or (location[1] == -1):
        pass

    # if location is usable
    elif grid[location[0]][location[1]] == 0:

        # Place 1 in spot and swap to player 2
        if player == "Player_1":
            grid[location[0]][location[1]] = 1
            player = swap_player(player)

        # Place 2 in spot and swap to player 1
        else:
            grid[location[0]][location[1]] = 2
            player = swap_player(player)

    # Output this to console in case something goes wrong
    else:
        print("invalid")

    # Output board in console to see update made
    show_board(grid)


def two_player_game():
    """
    This is where the output and logic is put together to create a two player game
    """
    # Creates game board (if menu is visited then resets board -> can be changed if needed)
    board = create_board()
    # Shows board in console for developer use
    show_board(board)

    # Created global player so the use of player can be used in functions
    global player
    player = "Player_1"

    # Sets standard for screen dimensions
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
                # Updates game grid in console
                update_grid(board, drop_location(pos))
                # Outputs clicked coordinates in console
                print("Click ", pos)

        # Resets screen so things can be changed in between frames
        screen.fill(black)

        # This outputs the game grid from the console to screen with correct coordinates
        for x in range(7):
            for y in range(7):
                rect = pygame.Rect(x * (BLOCK_SIZE + MARGIN) + LEFT_D, y * (BLOCK_SIZE + MARGIN) + TOP_D, BLOCK_SIZE,
                                   BLOCK_SIZE)

                # If not usable spot place red square
                if board[y][x] == -1:
                    pygame.draw.rect(screen, red, rect)

                # If usable spot place white square
                if board[y][x] == 0:
                    pygame.draw.rect(screen, white, rect)

                # If player 1 spot place green square
                if board[y][x] == 1:
                    pygame.draw.rect(screen, green, rect)

                # If player 2 spot place green square
                if board[y][x] == 2:
                    pygame.draw.rect(screen, blue, rect)

        # If player 1 turn then output player 1
        if player == "Player_1":
            player_turn = "Player 1's Turn"
            GAME_FONT.render_to(screen, (40, 350), player_turn, (100, 100, 100))

        # If player 2 turn then output player 2
        else:
            player_turn = "Player 2's Turn"
            GAME_FONT.render_to(screen, (40, 350), player_turn, (100, 100, 100))

        # This is to output the menu button
        pygame.draw.rect(screen, white, (35, 390, 80, 40))
        GAME_FONT.render_to(screen, (40, 400), "Menu", (100, 100, 100))

        pygame.display.flip()


def computer_game():
    """
    This will be used for future game mode to play against computer
    """
    pass


pygame.init()

# Color codes for consistent use
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
black = (0, 0, 0)

# Distances for consistency
WIDTH = 1000
HEIGHT = 800
MARGIN = 25
LEFT_D = 250
TOP_D = 50
BLOCK_SIZE = 75

# Works with pygame.freetype import to allow easier display of words to screen
GAME_FONT = pygame.freetype.Font(None, 24)

# Set title of screen
pygame.display.set_caption("Connect 4 Game")

# Menu function allows for everything to be called as needed. This is where all the magic happens.
menu()

# Done! Time to quit.
pygame.quit()
