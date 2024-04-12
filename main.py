import os

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def display_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal
        print("  0 | 1 | 2 ")
        print(" -----------")
        for i, row in enumerate(self.board):
            print(f"{i} {' | '.join(row)} ")
            if i < 2:
                print(" -----------")

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        else:
            return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

def get_input(prompt):
    print(prompt)
    return input()

def main():
    game = TicTacToe()
    game.display_board()

    while True:
        row = int(get_input("Enter row (0, 1, 2): "))
        col = int(get_input("Enter column (0, 1, 2): "))

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid input. Row and column must be between 0 and 2.")
            continue

        if game.make_move(row, col):
            game.display_board()
            game.switch_player()
        else:
            print("That cell is already occupied. Try again.")

if __name__ == "__main__":
    main()