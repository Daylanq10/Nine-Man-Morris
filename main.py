"""
Upsetti Spaghetti Coders
Kole Keeney, Chris Munns, Daylan Quinn and Greg Robson
10/5/20
CS 449

Nine Men's Morris main file
"""
import pygame
import pygame.freetype
import pygame_menu

# Initializing global variables
# Holds the current player
player = None 

# Holds tokens that need to be placed
player1_start_tokens = None
player2_start_tokens = None

# Holds tokens that a player has in total
player1_total_tokens = None
player2_total_tokens = None

# Holds tokens that a player has in play
player1_board_tokens = None
player2_board_tokens = None

# Holds current number of mills for each player
player1_mills = None
player2_mills = None

# Holds check for if and how many mills was found
mill_check = None

# Creates array for board
arr = []

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
    global arr
    arr = []

    # Create a 2D Array full of 0's with 7 rows and 7 columns
    arr = [[0 for i in range(row)] for j in range(col)]

    # Fill every non playable point with negative numbers -1/red/outer ring, -2/purple/middle ring, -3/black/center point
    # Did this to help differentiate between the layers and make mills easier to spot
    arr[0][1] = -1
    arr[0][2] = -1
    arr[0][4] = -1
    arr[0][5] = -1
    arr[1][0] = -1
    arr[1][2] = -2
    arr[1][4] = -2
    arr[1][6] = -1
    arr[2][0] = -1
    arr[2][1] = -2
    arr[2][5] = -2
    arr[2][6] = -1
    arr[3][3] = -3
    arr[4][0] = -1
    arr[4][1] = -2
    arr[4][5] = -2
    arr[4][6] = -1
    arr[5][0] = -1
    arr[5][2] = -2
    arr[5][4] = -2
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
def check_adjacent(x, y, board, player):
    """
    This checks for adjacent items in the board
    """
    mill = 0    
    row = []
    col = []
    # Compile the playable points of the row
    for i in range(0, 7):
        if board[x][i] >= 0:
            row.append(board[x][i])

    # If the row was the middle row, cut it down to the 3 adjacent points
    if len(row) == 6:
        if y < 3:
            row = row[:3]
        else:
            row = row[3:]

    # Compile the playable points of the column
    for i in range(0, 7):
        if board[i][y] >= 0:
            col.append(board[i][y])

    # If the column was the middle column, cut it down to the 3 adjacent points
    if len(col) == 6:
        if x < 3:
            col = col[:3]
        else:
            col = col[3:]

    # Check if the 3 of the row are all the same and match the selected player, if so, there is a mill
    if row[0] == row[1] == row[2] == player:        
        mill += 1

    # Check if the 3 of the column are all the same and match the selected player, if so, there is a mill
    if col[0] == col[1] == col[2] == player:        
        mill += 1

    # Print in terminal for testing 
    print("mills found ", mill)
    # Return how many mills were found
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
        menu = pygame_menu.Menu(HEIGHT, WIDTH, 'NINE-MEN\'S-MORRIS', theme=pygame_menu.themes.THEME_DARK)

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
    #for now not correctly formatting should be (y,x) to be consistent
    location = (x_location, y_location)
    return location


def update_grid(grid: list, location: tuple):
    """
    This changes the game grid with a 1 for player 1 and a 2 for player 2
    """
    # Declare global variables
    global arr
    global player
    global player1_start_tokens
    global player2_start_tokens
    global player1_total_tokens
    global player2_total_tokens
    global player1_board_tokens
    global player2_board_tokens
    global player1_mills
    global player2_mills
    global mill_check


    # If there is currently not a mill
    if mill_check == 0:

        # If the player has a token
        if player1_start_tokens != 0 or player2_start_tokens != 0:

            # If location in not usable then pass through function
            if (location[0] < 0) or (location[1] < 0):
                pass

            # if location is usable
            elif grid[location[0]][location[1]] == 0:

                # If this is player 1
                if player == "Player_1":
                    # Set tile to current player
                    grid[location[0]][location[1]] = 1
                    # Decrement placement token
                    player1_start_tokens -= 1
                    # Check if this created a mill and how many
                    if check_adjacent(location[0], location[1], arr, 1) > 0:
                        # Set mill check
                        mill_check = check_adjacent(location[0], location[1], arr, 1)
                        # Add mill/s to player
                        player1_mills += mill_check
                    # Swap players if a mill was not created
                    else:
                        player = swap_player(player)
                    


                # If this is player 2
                elif player == "Player_2":
                    # Set tile to current player
                    grid[location[0]][location[1]] = 2
                    # Decrement placement token
                    player2_start_tokens -= 1
                    # Check if this created a mill and how many
                    if check_adjacent(location[0], location[1], arr, 2) > 0:
                        # Set mill check
                        mill_check = check_adjacent(location[0], location[1], arr, 2)
                        # Add mill/s to player
                        player2_mills += mill_check
                    # Swap players if a mill was not created
                    else:
                        player = swap_player(player)
                    

    # If a mill just occurred and a piece is about to be removed
    else:
        removable = True
      
        # If location in not usable then pass through function
        if (location[0] < 0) or (location[1] < 0):
            pass

        # If location has a player 2 tile and this is player 1
        elif grid[location[0]][location[1]] == 2 and player == "Player_1":
            # Set found mills
            mill_check = check_adjacent(location[0], location[1], arr, 2)
            # If the piece being removed has mill/s
            if mill_check > 0:                
                # If the number of mills don't match placed tokens
                if player2_mills/player2_board_tokens < .30:
                    removable = False
                #If there is a stacked mill check to see if there is a loose token
                else:
                    for i in range (0,7):
                        for j in range (0,7):
                            if arr[i][j] == 2:
                                if check_adjacent(i,j,arr,2) == 0:
                                    removable = False
                    
            # If it passes the test
            if removable:
                # Check how many mills will be removed and take them from player
                if mill_check > 0:
                        player2_mills -= mill_check
                # Set tile to empty
                grid[location[0]][location[1]] = 0
                # Remove token from Player 2
                player2_total_tokens -= 1
                # Swap players
                player = swap_player(player)
                # Set mill check to false now that it has occurred
                mill_check = 0

        # If location has a player 1 tile and this is player 2
        elif grid[location[0]][location[1]] == 1 and player == "Player_2":
            # Set found mills
            mill_check = check_adjacent(location[0], location[1], arr, 1)
            # If the piece being removed has mill/s
            if mill_check > 0:
                # If the number of mills don't match placed tokens
                if player1_mills/player1_board_tokens < .30:
                    removable = False
                #If there is a stacked mill check to see if there is a loose token
                else:
                    for i in range (0,7):
                        for j in range (0,7):
                            if arr[i][j] == 1:
                                if check_adjacent(i,j,arr,1) == 0:
                                    removable = False
            # If it passes the test
            if removable:
                # Check how many mills will be removed and take them from player
                if mill_check > 0:
                        player1_mills -= mill_check
                # Set tile to empty
                grid[location[0]][location[1]] = 0
                # Remove token from Player 1
                player1_total_tokens -= 1
                # Swap players
                player = swap_player(player)
                # Set mill check to false now that it has occurred
                mill_check = 0

    # Update and check if all token counts are consistent after each update
    if player1_board_tokens > player1_total_tokens:
        player1_board_tokens = player1_total_tokens
    else:
        player1_board_tokens = player1_total_tokens - player1_start_tokens

    if player2_board_tokens > player2_total_tokens:
        player2_board_tokens = player2_total_tokens
    else:
        player2_board_tokens = player2_total_tokens - player2_start_tokens
    # Output board in console to see update made
    show_board(grid)
    # Print click (x,y)
    print(location[1],location[0])
    # Print all tracked tokens and mills for each player
    print (player1_start_tokens, player1_total_tokens, player1_board_tokens, player1_mills)
    print (player2_start_tokens, player2_total_tokens, player2_board_tokens, player2_mills)


def two_player_game():
    """
    This is where the output and logic is put together to create a two player game
    """
    # Creates game board (if menu is visited then resets board -> can be changed if needed)
    board = create_board()
    # Shows board in console for developer use
    show_board(board)

    # Declare global player variable
    global player
    # Set it to player 1
    player = "Player_1"

    # Declare global starting tokens  
    global player1_start_tokens    
    global player2_start_tokens
    global player1_total_tokens
    global player2_total_tokens
    global player1_board_tokens
    global player2_board_tokens
    global player1_mills
    global player2_mills
    global mill_check

    # Set / Reset the default of mill_check to false
    mill_check = 0

    # Set them to 9 at start of game
    player1_start_tokens = 9   
    player2_start_tokens = 9
    player1_total_tokens = 9
    player2_total_tokens = 9
    player1_board_tokens = 0
    player2_board_tokens = 0
    player1_mills = 0
    player2_mills = 0

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
                if mill_check > 0: # Checks if that move made a mill
                    #mill_check = True
                    print ("Mill was found") # Prints in terminal
                    pos = pygame.mouse.get_pos()
                    update_grid(board, drop_location(pos))
                print("Click ", pos)


        # This outputs the game grid from the console to screen with correct coordinates

        # Resets screen so things can be changed in between frames
        screen.fill(black)

        #draw various board components
        # outer rectangle
        pygame.draw.rect(screen, (150,150,150), (285, 85, 605, 605), 3)

        # middle rectangle
        pygame.draw.rect(screen, (150,150,150), (385, 185, 405, 405), 3)

        # inner rectangle
        pygame.draw.rect(screen, (150,150,150), (485, 285, 205, 205), 3)

        # lines
        pygame.draw.line(screen, (150,150,150), (585, 85), (585, 285), 3)
        pygame.draw.line(screen, (150,150,150), (585, 485), (585, 685), 3)
        pygame.draw.line(screen, (150, 150, 150), (250, 385), (485, 385), 3)
        pygame.draw.line(screen, (150, 150, 150), (685, 385), (885, 385), 3)

        for x in range(7):
            for y in range(7):
                rect = pygame.Rect(x * (BLOCK_SIZE + MARGIN) + LEFT_D, y * (BLOCK_SIZE + MARGIN) + TOP_D, BLOCK_SIZE,
                                   BLOCK_SIZE)

                # If usable spot place white square
                if board[y][x] == 0:
                    pygame.draw.rect(screen, white, rect)

                # If player 1 spot place green square
                if board[y][x] == 1:
                    pygame.draw.rect(screen, green, rect)

                # If player 2 spot place blue square
                if board[y][x] == 2:
                    pygame.draw.rect(screen, blue, rect)


        # If player 1 turn then output player 1
        if player == "Player_1":
            player_turn = "Player 1's Turn" 
            player_tokens = "Pieces left: " + str(player1_start_tokens) # Displays remaining tokens            

            GAME_FONT.render_to(screen, (40, 350), player_turn, (100, 100, 100)) # Places text
            pygame.draw.rect(screen, green, (40, 390, 40, 40)) # Displays players token avatar
            GAME_FONT.render_to(screen, (90, 400), player_tokens, (100, 100, 100)) # Places text

        # If player 2 turn then output player 2
        elif player == "Player_2":
            player_turn = "Player 2's Turn" 
            player_tokens = "Pieces left: " + str(player2_start_tokens) # Displays remaining tokens
            
            GAME_FONT.render_to(screen, (40, 350), player_turn, (100, 100, 100)) # Places text
            pygame.draw.rect(screen, blue, (40, 390, 40, 40)) # Displays players token avatar
            GAME_FONT.render_to(screen, (90, 400), player_tokens, (100, 100, 100)) # Places text

        #if mill_check, display text, needs remove piece function
        if mill_check > 0:
            GAME_FONT.render_to(screen, (25,150), " Mill found!", white)


        # This is to output the menu button
        pygame.draw.rect(screen, white, (40, 450, 80, 40))
        GAME_FONT.render_to(screen, (50, 460), "Menu", (100, 100, 100))


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
purple = (185,0,255)

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
pygame.display.set_caption("Nine Men's Morris")

# Menu function allows for everything to be called as needed. This is where all the magic happens.
menu()

# Done! Time to quit.
pygame.quit()
