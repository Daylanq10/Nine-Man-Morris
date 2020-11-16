"""
Upsetti Spaghetti Coders
THIS FILE IS FOR THE BOARD OBJECT THAT IS GOVERNED BY OBJECTS FROM
THE PLAYER CLASS IN THE NINE MAN'S MORRIS GAME.
"""


class Board:
    def __init__(self):
        self.grid = self.create_board()
        self.is_playable = self.playable_positions()

    # Function that initializes the game board then returns it
    def create_board(self):
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

    def display(self):
        """
        This is used to show the contents of the board in the console
        """
        print()
        # Just a statement to print out a representation of the board
        for i in range(0, 7):
            print(self.grid[i])

    def playable_positions(self):
        """
        This sets for only allowing clicking of playable spots
        """
        usable = []
        for x in range(7):
            for y in range(7):
                if self.grid[x][y] == 0:
                    usable.append((x,y))
        return usable
