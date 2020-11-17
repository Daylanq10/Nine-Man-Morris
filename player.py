"""
Upsetti Spaghetti Coders
THIS FILE IS FOR THE PLAYER OBJECTS THAT GOVERN EACH OF THE TWO
PEOPLE OR AI PLAYING THE NINE MAN'S MORRIS GAME.
"""

class Player:
    def __init__(self, num, play):
        self.number = num  # Player 1 or 2, True = 1, False = 2
        self.playable = play  # True = Human, False = AI
        self.start_tokens = 9
        self.board_tokens = 0
        self.mills = 0
        self.turn = num  # True = their turn, False = opponent's turn

    # Returns total tokens
    def get_total_tokens(self):
        return self.board_tokens + self.start_tokens
