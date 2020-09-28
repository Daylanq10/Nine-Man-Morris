"""
Upsetti Spaghetti Coders
Kole Keeney, Chris Munns, Daylan Quinn and Greg Robson
9/28/20
CS 449

Nine Men's Morris main file
"""


def main():
    # Create the game board
    board = create_board()

    # Just a statement to print out a representation of the board, not needed
    for i in range(0, 7):
        print(board[i])


# Function that initializes the game board then returns it
def create_board():
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


# Function that checks for the creation of a new mill given a piece has just been played
# Should be called with the x and y coordinates of the point just played, and the game board for arr
# Returns true if it finds a mill, returns false if not
def check_adjacent(x, y, arr):
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


main()
