
from copy import deepcopy
from player import Player
from board import Board
import math
import random


ROWS = 7
COL = 7


# Testing stuff
# board = Board()
# human = Player(False, True)
# ai = Player(True, False)


# # ai.start_tokens = 0
# # human.start_tokens = 0

# player = 2
# opponent = 1

# # # board.grid[0][0] = 1
# board.grid[1][1] = 1
# # board.grid[6][6] = 1
# board.grid[1][5] = 1
# board.grid[2][3] = 1

# # # # board.grid[0][6] = 1
# human.start_tokens -= 3
# #board.grid[6][0] = 2
# # # board.grid[1][1] = 1
# # # board.grid[6][6] = 1
# # # board.grid[6][3] = 1

# # # # neutral
# board.grid[0][0] = 2
# board.grid[3][2] = 2

# # # board.grid[1][5] = 2
# # # board.grid[2][4] = 2
# board.grid[6][3] = 2
# ai.start_tokens -= 3

# # one mill
# board.grid[0][0] = 2


# For printing the board


def print_grid(board):
    for i in range(len(board)):
        print(board[i])


# print_grid(board.grid)


# Create node class that is the basis of the Monte Carlo tree


class Node():
    def __init__(self, parent, board, piece, move, removal, ai, player):
        # Holds all attrubutes for tree formation
        self.piece = piece
        self.move = move
        self.removal = removal
        self.player = deepcopy(player)
        self.ai = deepcopy(ai)
        self.board = board.copy()
        self.visits = 0
        self.score = 0.0
        self.children = []
        self.parent = parent

# Checks if a mill was created


def check_adjacent(x, y, board, player_piece):
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
    if row[0] == row[1] == row[2] == player_piece:
        mill += 1

    # Check if the 3 of the column are all the same and match the selected player, if so, there is a mill
    if col[0] == col[1] == col[2] == player_piece:
        mill += 1

    # Return how many mills were found
    return mill


def add(board, x, y):
    # Changes valid move to 3
    if board[x][y] == 0:
        board[x][y] = 3


def find_moves(board, location):

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

# Generates all the potential moves the AI can take and create nodes on the tree for them


def ai_moves(board, node):
    moves = []
    enemy = []
    pieces = []
    rem = True

    grid = deepcopy(board)
    ai_copy = Player(False, False)
    ai_copy = deepcopy(node.ai)
    player_copy = Player(True, True)
    player_copy = deepcopy(node.player)

    # Find all open spots
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                temp_place = [i, j]
                moves.append(temp_place)
    # Find all pieces for the AI
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                temp_place = [i, j]
                pieces.append(temp_place)

    # if AI is in stage 1
    if ai_copy.start_tokens > 0:

        ai_copy.start_tokens -= 1
        ai_copy.board_tokens += 1
        # Look all possible moves
        for i in range(len(moves)):
            # Create a copy of board and add a piece to this place
            temp_grid = deepcopy(grid)
            temp_grid[moves[i][0]][moves[i][1]] = 2
            temp_move = moves[i]
            # Check for mills
            mills = check_adjacent(moves[i][0], moves[i][1], temp_grid, 2)
            # If there is one
            if mills > 0:
                rem = True
                # Check for standalone pieces
                for r in range(len(temp_grid)):
                    for j in range(len(temp_grid[r])):
                        if temp_grid[r][j] == 1:
                            temp_enemy = [r, j]
                            enemy.append(temp_enemy)
                            if check_adjacent(temp_enemy[0], temp_enemy[1], temp_grid, 1) == 0:
                                rem = False
                # For all enemies
                for p in range(len(enemy)):
                    # Create copy of board for all enemies to be removed and check for mills
                    ai_copy_2 = deepcopy(ai_copy)
                    temp_grid_2 = deepcopy(temp_grid)
                    enemy_mills = check_adjacent(
                        enemy[p][0], enemy[p][1], temp_grid_2, 1)
                    # If no mills, remove and create new node
                    if enemy_mills == 0:
                        player_copy.board_tokens -= 1
                        temp_grid_2[enemy[p][0]][enemy[p][1]] = 0

                        new_node = Node(node, temp_grid_2, None,
                                        temp_move, enemy[p], ai_copy_2, player_copy)
                        node.children.append(new_node)
                    # If mills but no straglers remove and create node
                    elif enemy_mills > 0 and rem == True:
                        player_copy.board_tokens -= 1
                        temp_grid_2[enemy[p][0]][enemy[p][1]] = 0
                        new_node = Node(node, temp_grid_2, None,
                                        temp_move, enemy[p], ai_copy, player_copy)
                        node.children.append(new_node)
                    # Else there are straglers and this is invalid
                    else:
                        pass
            # No mill was formed create node with piece placed
            else:

                new_node = Node(node, temp_grid, None, temp_move,
                                None, ai_copy, player_copy)
                node.children.append(new_node)
    # Else if in stage 2
    elif ai_copy.start_tokens == 0 and len(pieces) > 3:
        # For all pieces
        for i in range(len(pieces)):
            # Create a copy of the board for all pieces and find valid moves
            temp_grid = deepcopy(grid)
            find_moves(temp_grid, (pieces[i][0], pieces[i][1]))
            movement = []

            for l in range(len(temp_grid)):
                for k in range(len(temp_grid)):
                    if temp_grid[l][k] == 3:
                        movement.append([l, k])
                        temp_grid[l][k] = 0
            # If there are valid moves
            if len(movement) > 0:
                # For every move
                for m in range(len(movement)):
                    # Create a board for each move and move piece
                    mills = 0
                    temp_grid_2 = deepcopy(temp_grid)
                    temp_grid_2[pieces[i][0]][pieces[i][1]] = 0
                    temp_grid_2[movement[m][0]][movement[m][1]] = 2

                    # Check for mills
                    mills = check_adjacent(
                        movement[m][0], movement[m][1], temp_grid_2, 2)

                    temp_piece = [pieces[i][0], pieces[i][1]]
                    temp_move = [movement[m][0], movement[m][1]]

                    # If a mill was formed
                    if mills > 0:
                        rem = True
                        # Check if there is any stragler pieces for the enemy
                        for n in range(len(temp_grid_2)):
                            for d in range(len(temp_grid_2[n])):
                                if temp_grid_2[n][d] == 1:
                                    temp_enemy = [n, d]
                                    enemy.append(temp_enemy)
                                    if check_adjacent(temp_enemy[0], temp_enemy[1], temp_grid_2, 1) == 0:
                                        rem = False
                        # For each enemy
                        for u in range(len(enemy)):
                            # Create a copy of the board
                            temp_grid_3 = deepcopy(temp_grid_2)
                            # Check if in mill
                            enemy_mills = check_adjacent(
                                enemy[u][0], enemy[u][1], temp_grid_3, 1)
                            # If not in mill, remove and create node
                            if enemy_mills == 0:
                                player_copy.board_tokens -= 1
                                temp_grid_3[enemy[u][0]][enemy[u][1]] = 0

                                new_node = Node(node, temp_grid_3, temp_piece,
                                                temp_move, enemy[u], ai_copy, player_copy)
                                node.children.append(new_node)
                            # If in a mill but there are no straglers remove and create node
                            elif enemy_mills > 0 and rem == True:
                                player_copy.board_tokens -= 1
                                temp_grid_3[enemy[u][0]][enemy[u][1]] = 0

                                new_node = Node(node, temp_grid_3, temp_piece,
                                                temp_move, enemy[u], ai_copy, player_copy)
                                node.children.append(new_node)
                            # There are straglers still on the board
                            else:
                                pass
                    # No mill was formed so move piece and create node
                    else:
                        new_node = Node(node, temp_grid_2, temp_piece, temp_move,
                                        None, ai_copy, player_copy)
                        node.children.append(new_node)
                    enemy = []
    # Else in stage 3
    else:
        # For each piece
        for i in range(len(pieces)):
            # Create a copy of the board
            temp_grid = deepcopy(grid)
            # Find all moves
            for m in range(len(grid)):
                for r in range(len(grid[m])):
                    if temp_grid[m][r] == 0:
                        temp_grid[m][r] = 3
            movement = []
            for l in range(len(temp_grid)):
                for k in range(len(temp_grid)):
                    if temp_grid[l][k] == 3:
                        movement.append([l, k])
                        temp_grid[l][k] = 0
            # If there are valid moves
            if len(movement) > 0:
                # For each move
                for j in range(len(movement)):
                    # Create a copy of the board and move piece
                    temp_grid_2 = deepcopy(temp_grid)

                    temp_grid_2[pieces[i][0]][pieces[i][1]] = 0
                    temp_grid_2[movement[j][0]][movement[j][1]] = 2
                    # Check for mills formed
                    mills = check_adjacent(
                        movement[j][0], movement[j][1], temp_grid_2, 2)
                    temp_piece = [pieces[i][0], pieces[i][1]]
                    temp_move = [movement[j][0], movement[j][1]]
                    # If mills has been formed
                    if mills > 0:

                        rem = True
                        # Find all enemies
                        for d in range(len(temp_grid)):
                            for r in range(len(temp_grid[i])):
                                if temp_grid[d][r] == 1:
                                    temp_enemy = [d, r]
                                    enemy.append(temp_enemy)
                                    if check_adjacent(temp_enemy[0], temp_enemy[1], temp_grid_2, 1) == 0:
                                        rem = False
                        # For each enemy
                        for q in range(len(enemy)):
                            # Create a copy of the board and check enemies for mills
                            temp_grid_3 = deepcopy(temp_grid_2)
                            enemy_mills = check_adjacent(
                                enemy[q][0], enemy[q][1], temp_grid_3, 1)
                            # If not in mill remove and create new node
                            if enemy_mills == 0:
                                player_copy.board_tokens -= 1
                                temp_grid_3[enemy[q][0]][enemy[q][1]] = 0

                                new_node = Node(node, temp_grid_3, temp_piece,
                                                temp_move, enemy[q], ai_copy, player_copy)
                                node.children.append(new_node)
                            # If in mill but no straglers remove and create node
                            elif enemy_mills > 0 and rem == True:
                                player_copy.board_tokens -= 1
                                temp_grid_3[enemy[q][0]][enemy[q][1]] = 0

                                new_node = Node(node, temp_grid_3, temp_piece,
                                                temp_move, enemy[q], ai_copy, player_copy)
                                node.children.append(new_node)
                            # Else there are straglers and is invalid
                            else:
                                pass
                    # No mill found create node
                    else:
                        new_node = Node(node, temp_grid, temp_piece, temp_move,
                                        None, ai_copy, player_copy)
                        node.children.append(new_node)

# Create random move at any point on the board


def random_move(board, mine, yours, starting):
    onboard = []
    rem = True
    grid = deepcopy(board)
    # piece,move, removal
    result = [None, None, None]

    # Find all your pieces
    def find_piece(grid):
        pieces = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == mine:
                    temp_place = [i, j]
                    pieces.append(temp_place)

        if len(pieces) == []:
            return None
        random.shuffle(pieces)
        return pieces[0]

    # Find all open spots
    def find_move(grid):
        moves = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    temp_place = [i, j]
                    moves.append(temp_place)

        if len(moves) == []:
            return None
        random.shuffle(moves)
        return moves[0]

    # Find all enemy tokens
    def find_enemy(grid, yours):
        enemy = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == yours:
                    temp_place = [i, j]
                    enemy.append(temp_place)

        if len(enemy) == []:
            return None
        random.shuffle(enemy)
        return enemy[0]

    # Count tokens on board
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == mine:
                temp_place = [i, j]
                onboard.append(temp_place)
    # If stage 1
    if starting > 0:
        # Create a copy of the board and find a valid move
        temp_grid = deepcopy(grid)
        move = None
        while move == None:
            move = find_move(temp_grid)
        # Place piece and check for mills
        temp_grid[move[0]][move[1]] = mine
        mills = check_adjacent(move[0], move[1], temp_grid, mine)
        # If there are mills
        if mills > 0:
            removal = None
            rem = True
            for a in range(len(temp_grid)):
                for b in range(len(temp_grid[a])):
                    if temp_grid[a][b] == yours:
                        if check_adjacent(a, b, temp_grid, yours) == 0:
                            rem = False

            # refresh through enemy pieces until you find a valid one to remove and record
            while removal == None:
                #rem = True
                target = find_enemy(temp_grid, yours)
                # if check_adjacent(target[0], target[1], temp_grid, yours) == 0:
                #     rem = False
                enemy_mills = check_adjacent(
                    target[0], target[1], temp_grid, yours)
                # If enemy has no mills
                if enemy_mills == 0:
                    removal = [target[0], target[1]]
                    result[1] = move
                    result[2] = removal
                    return result
                # If enemy has mills but no straglers
                elif enemy_mills > 0 and rem == True:
                    removal = [target[0], target[1]]
                    result[1] = move
                    result[2] = removal
                    return result
                # Repeats if not a valid piece
        else:
            # else just record the move
            result[1] = move
            return result
    # if stage 2
    elif starting == 0 and len(onboard) > 3:

        piece = None
        movement = []

        temp_grid = deepcopy(grid)

        # Rotate through pieces until you find one with a valid move
        while piece == None:
            # Create a copy of the board to work on
            temp_grid = deepcopy(grid)
            # Find piece
            temp_piece = find_piece(temp_grid)
            # Look for moves
            find_moves(temp_grid, (temp_piece[0], temp_piece[1]))
            movement = []
            # If a valid place appears set piece and break
            for l in range(len(temp_grid)):
                for k in range(len(temp_grid)):
                    if temp_grid[l][k] == 3:
                        movement.append([l, k])
                        temp_grid[l][k] = 0
            if len(movement) > 0:
                piece = temp_piece

        # Pick any of the movements as they are all valid
        random.shuffle(movement)
        move = movement[0]
        mills = 0
        temp_grid_2 = deepcopy(temp_grid)
        # Move piece
        temp_grid_2[piece[0]][piece[1]] = 0
        temp_grid_2[move[0]][move[1]] = mine
        # Check for mills
        mills = check_adjacent(
            move[0], move[1], temp_grid_2, mine)
        # If there are mills

        if mills > 0:
            removal = None
            rem = True
            for a in range(len(temp_grid)):
                for b in range(len(temp_grid[a])):
                    if temp_grid[a][b] == yours:
                        if check_adjacent(a, b, temp_grid, yours) == 0:
                            rem = False

            # Search for a valid piece to remove
            while removal == None:
                #rem = True
                # Find a valid enemy
                target = find_enemy(temp_grid, yours)
                # Check for straglers
                # if check_adjacent(target[0], target[1], temp_grid, 2) == 0:
                #rem = False
                enemy_mills = check_adjacent(
                    target[0], target[1], temp_grid, yours)
                # If not in mill remove and record
                if enemy_mills == 0:
                    removal = [target[0], target[1]]
                    result[0] = piece
                    result[1] = move
                    result[2] = removal
                    return result
                # If in mill but no straglers remove and record
                elif enemy_mills > 0 and rem == True:
                    removal = [target[0], target[1]]
                    result[0] = piece
                    result[1] = move
                    result[2] = removal
                    return result
                # Repeat if invalid
        # No mill found move and record
        else:
            result[0] = piece
            result[1] = move
            return result
    # If in stage 3
    else:
        piece = None
        movement = []
        temp_grid = deepcopy(grid)
        # Find a valid piece
        while piece == None:
            # Create a copy of the board
            temp_grid = deepcopy(grid)

            temp_piece = find_piece(temp_grid)
            # Search for any valid moves it has
            for l in range(len(temp_grid)):
                for k in range(len(temp_grid)):
                    if temp_grid[l][k] == 0:
                        movement.append([l, k])
            if len(movement) > 0:
                piece = temp_piece

        # If valid move found select one at random
        random.shuffle(movement)
        move = movement[0]
        mills = 0
        temp_grid_2 = deepcopy(temp_grid)
        # Move piece
        temp_grid_2[piece[0]][piece[1]] = 0
        temp_grid_2[move[0]][move[1]] = mine
        # Check for mills
        mills = check_adjacent(
            move[0], move[1], temp_grid_2, mine)
        # If there is a mill
        if mills > 0:
            removal = None
            rem = True
            for a in range(len(temp_grid)):
                for b in range(len(temp_grid[a])):
                    if temp_grid[a][b] == yours:
                        if check_adjacent(a, b, temp_grid, yours) == 0:
                            rem = False

            # Find a valid enemy

            while removal == None:
                #rem = True
                # Find a valid enemy
                target = find_enemy(temp_grid, yours)
                # if check_adjacent(target[0], target[1], temp_grid, yours) == 0:
                # rem = False
                enemy_mills = check_adjacent(
                    target[0], target[1], temp_grid, yours)
                # If enemy isn't in a mill remove and record
                if enemy_mills == 0:
                    removal = [target[0], target[1]]
                    result[0] = piece
                    result[1] = move
                    result[2] = removal
                    return result
                # If in mill but no straglers remove and record
                elif enemy_mills > 0 and rem == True:
                    removal = [target[0], target[1]]
                    result[0] = piece
                    result[1] = move
                    result[2] = removal
                    return result
                # Else invalid and repeat
        else:
            # If no mill record the move
            result[0] = piece
            result[1] = move
            return result

# Function for traversal and expansion


def traverse(node, player, opponent, exploration):

    # Set markers for tracking
    best = None
    best_weight = 0
    curr_weight = 0

    # look through children
    for j in range(len(node.children)):

        # if there is an unvisited node just select it
        if node.children[j].visits == 0:

            return node.children[j]

    # Else get the weight of all children and choose the best
    for i in range(len(node.children)):

        curr_weight = (node.children[i].score/node.children[i].visits) + exploration*(
            math.sqrt((math.log(node.visits)/node.children[i].visits)))
        # Checks and holds the highest score
        if curr_weight > best_weight:
            best_weight = curr_weight
            # Record the position of best child in parent array
            best = i

    # if we are unable to calc weight return original node
    if best == None:
        return node

    # If the best weight has children traverse them
    if node.children[best].children != []:

        return traverse(node.children[best], player, opponent, exploration)

    # Else we need to expand and create the best options children
    else:
        # Generate some random move for the opponent
        token = 0
        blocked = True
        for i in range(len(node.children[best].board)):
            for j in range(len(node.children[best].board[i])):
                if node.children[best].board[i][j] == 1:
                    token += 1
                    temp_board = deepcopy(node.children[best].board)
                    find_moves(temp_board, (i, j))
                    for l in range(len(temp_board)):
                        for k in range(len(temp_board)):
                            if temp_board[l][k] == 3:
                                blocked = False

        if token < 3 and node.children[best].player.start_tokens == 0 or blocked == True:

            return node.children[best]
        else:
            moves = random_move(
                node.children[best].board, opponent, player, node.children[best].player.start_tokens)
            # If a piece was selected set
            if moves[0] != None:
                node.children[best].board[moves[0][0]][moves[0][1]] = 0
            # If None then in stage 1 so decrement start tokens
            else:
                node.children[best].player.start_tokens -= 1
            # If a move was selected set
            if moves[1] != None:
                node.children[best].board[moves[1][0]][moves[1][1]] = 1
            # If something was removed set
            if moves[2] != None:
                node.children[best].board[moves[2][0]][moves[1][1]] = 0

        # If nothing was possible just return the original node
        if moves == []:
            return node
        # Create all possible moves for ai and generate nodes as children for all
        ai_moves(node.children[best].board, node.children[best])

        # Then traverse those children
        return traverse(node.children[best], player, opponent, exploration)

# rollout by playing a dummy game with all random moves


def rollout(node, player, opponent):

    # Use a temp board for this
    node = deepcopy(node)
    board = node.board.copy()
    # Create trackers
    game_over = False
    turn = 0
    score = 0
    tokens = [0, 0]
    blocked_1 = True
    blocked_2 = True

    # While game is still going
    while not game_over:
        blocked_1 = True
        blocked_2 = True

        tokens[0] = 0
        tokens[1] = 0
        # Check for win condition
        # Run through the board
        for i in range(len(board)):
            for j in range(len(board[i])):
                # Count tokens for each player and see if they're blocked in
                if board[i][j] == 1:
                    tokens[0] += 1
                    temp_board = deepcopy(board)
                    find_moves(temp_board, (i, j))
                    for l in range(len(temp_board)):
                        for k in range(len(temp_board)):
                            if temp_board[l][k] == 3:
                                blocked_1 = False

                if board[i][j] == 2:
                    tokens[1] += 1
                    temp_board = deepcopy(board)
                    find_moves(temp_board, (i, j))
                    for l in range(len(temp_board)):
                        for k in range(len(temp_board)):
                            if temp_board[l][k] == 3:
                                blocked_2 = False

        # If human lost report a win
        if tokens[0] < 3 or blocked_1 == True:

            score = 2

            return score
        # If AI lost report a lose
        if tokens[1] < 3 or blocked_2 == True:
            score = 0

            return score

        # Player 1 Input:
        if turn == 0:

            # Random move

            moves = random_move(board, 1, 2, node.player.start_tokens)

            # Record depending of output
            if moves[0] != None:
                board[moves[0][0]][moves[0][1]] = 0
            else:
                node.player.start_tokens -= 1
            if moves[1] != None:
                board[moves[1][0]][moves[1][1]] = 1
            if moves[2] != None:
                board[moves[2][0]][moves[2][1]] = 0

            # Progress turn
            turn += 1
            turn = turn % 2

        # Player 1 Input:
        else:

            # Random move

            moves = random_move(board, 2, 1, node.ai.start_tokens)

            # Record depending of output
            if moves[0] != None:
                board[moves[0][0]][moves[0][1]] = 0
            else:
                node.ai.start_tokens -= 1
            if moves[1] != None:
                board[moves[1][0]][moves[1][1]] = 2
            if moves[2] != None:
                board[moves[2][0]][moves[2][1]] = 0

            # Progress turn
            turn += 1
            turn = turn % 2


# Backprop the parents until you reach root
def backpropagate(node, score):

    # if node.move == None and node.piece == None and node.removal == None:
    #     return

    node.parent.visits += 1
    node.parent.score += score
    if node.parent.parent != None:

        backpropagate(node.parent, score)

# Main driver function

        # Board_class, AI#, Human#, AI class, Human Class, weight for exploration (stick to two), how many time you want to run (at least 100)


def monte_carlo(copy, player, opponent, ai_class, human_class, exploration, iteration):
    copy = copy.grid.copy()
    # Create empty root node
    root = Node(None, copy, None, None, None, ai_class, human_class)
    # Create initial moves in tree by parsing through any valid input
    ai_moves(copy, root)
    #count = 1

    total = 0
    # For for how ever many times we want to run the simulation
    for i in range(iteration):
        # print("ping", count)
        # count += 1
        # Traverse tree and expand as needed to find best candidate

        leaf_node = traverse(root, player, opponent, exploration)

        # rollout the simulation and get the score
        simulation = rollout(leaf_node, player, opponent)

        if simulation == 2:
            point = 1
        elif simulation == 3:
            point = 0.5
        else:
            point = 0
        total += point
        # Add a visit to this node and the score that was earned win/lose/draw
        leaf_node.visits += 1
        leaf_node.score += point

        # Backprop up to the root
        backpropagate(leaf_node, point)
    print("Total points", total)
    # Trackers for the winning move
    final_move = None
    final_score = 0

    container = []
    # Search children of root for best move based on score

    for i in range(len(root.children)):
        # If move creates a mill, prioritize
        if root.children[i].removal != None:

            root.children[i].score = 10000
        # Set score marker
        x = root.children[i].score

        print(root.children[i].piece,
              root.children[i].move, root.children[i].removal, root.children[i].score, root.children[i].visits)
        # If the score is greater than the previous greatest
        if x > final_score:
            # set high score and move set
            final_score = x

            final_move = [root.children[i].piece,
                          root.children[i].move, root.children[i].removal]
    # If multiple had the highest score, gather then choose one randomly
    for i in range(len(root.children)):
        if root.children[i].score == final_score:
            container.append([root.children[i].piece,
                              root.children[i].move, root.children[i].removal])
    if container != []:
        random.shuffle(container)
        final_move = container[0]

    # Return [[piece], [move], [removal]]
    return final_move


#print(monte_carlo(board, 2, 1, ai, human, 2, 100))
