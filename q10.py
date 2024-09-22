"""
(a) Write a class called Connect4 that implements the logic of a Connect4 game. 
    Use the Tic_tac_toe class from this chapter as a starting point.

(b) Use the Connect4 class to create a simple text-based version of the game.
"""

class Connect4:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.B = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.player = 1

    def get_open_spots(self):
        return [c for c in range(self.cols) if self.B[0][c] == 0]

    def is_valid_move(self, c):
        return 0 <= c < self.cols and self.B[0][c] == 0

    def make_move(self, c):
        if self.is_valid_move(c):
            for r in range(self.rows - 1, -1, -1):
                if self.B[r][c] == 0:
                    self.B[r][c] = self.player
                    self.player = 3 - self.player  # Switch between 1 and 2
                    return True
        return False

    def check_for_winner(self):
        # Check horizontal
        for r in range(self.rows):
            for c in range(self.cols - 3):
                if self.B[r][c] == self.B[r][c+1] == self.B[r][c+2] == self.B[r][c+3] != 0:
                    return self.B[r][c]

        # Check vertical
        for r in range(self.rows - 3):
            for c in range(self.cols):
                if self.B[r][c] == self.B[r+1][c] == self.B[r+2][c] == self.B[r+3][c] != 0:
                    return self.B[r][c]

        # Check diagonal (top-left to bottom-right)
        for r in range(self.rows - 3):
            for c in range(self.cols - 3):
                if self.B[r][c] == self.B[r+1][c+1] == self.B[r+2][c+2] == self.B[r+3][c+3] != 0:
                    return self.B[r][c]

        # Check diagonal (bottom-left to top-right)
        for r in range(3, self.rows):
            for c in range(self.cols - 3):
                if self.B[r][c] == self.B[r-1][c+1] == self.B[r-2][c+2] == self.B[r-3][c+3] != 0:
                    return self.B[r][c]

        # Check for draw
        if self.get_open_spots() == []:
            return 0

        return -1

def print_board(game):
    chars = ['.', 'X', 'O']
    for r in range(game.rows):
        for c in range(game.cols):
            print(chars[game.B[r][c]], end=' ')
        print()
    print(' '.join(str(i) for i in range(game.cols)))

def play_connect4():
    game = Connect4()
    while game.check_for_winner() == -1:
        print_board(game)
        while True:
            try:
                c = int(input(f'Enter column (0-6), player {game.player}: '))
                if game.make_move(c):
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a valid integer.")

    print_board(game)
    result = game.check_for_winner()
    if result == 0:
        print("It's a draw.")
    else:
        print(f'Player {result} wins!')

if __name__ == "__main__":
    play_connect4()