"""
Upsetti Spaghetti Coders
THIS FILE IS FOR THE PLAYER OBJECTS THAT GOVERN EACH OF THE TWO
PEOPLE OR AI PLAYING THE NINE MAN'S MORRIS GAME.
"""

class Player:
    def __init__(self, num, play):

        self.number = num  # 1 for player_1, 2 for player_2
        self.playable = play  # True = Human, False = AI

        self.start_tokens = 9
        self.board_tokens = 0

        self.mills = 0  # needs to be updated in functions to allow for certain criteria
        self.mill_positions = []
        self.new_mill = False

        self.selected_move = False

        self.past_possible = []
        self.clicked_pos = None

        self.moves = 0

        self.stage = "Stage 1: Placing"

    # Returns total tokens
    def get_total_tokens(self):
        return self.board_tokens + self.start_tokens

    # Increments moves
    def inc_moves(self):
        self.moves += 1

    def dec_moves(self):
        self.moves -= 1
