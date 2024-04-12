
import curses

# Function to initialize the curses screen
def initialize_screen():
    screen = curses.initscr()
    curses.curs_set(0)  # Hide cursor
    screen.keypad(True)  # Enable keypad mode
    curses.noecho()      # Don't echo keypresses
    return screen

# Function to create the game board
def create_board(size):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    return board

# Function to display the game board
def display_board(screen, board, cursor_x, cursor_y):
    screen.clear()
    for y in range(len(board)):
        for x in range(len(board[y])):
            cell = board[y][x]
            screen.addstr(y * 2, x * 4, f" {cell} |")
        screen.addstr(y * 2 + 1, 0, "----" * len(board) + "-")
    screen.addstr(cursor_y * 2, cursor_x * 4, f"({board[cursor_y][cursor_x]})", curses.A_REVERSE)
    screen.refresh()

# Function to handle player input and navigation
def handle_input(screen, board, cursor_x, cursor_y):
    while True:
        key = screen.getch()
        if key == curses.KEY_UP and cursor_y > 0:
            cursor_y -= 1
        elif key == curses.KEY_DOWN and cursor_y < len(board) - 1:
            cursor_y += 1
        elif key == curses.KEY_LEFT and cursor_x > 0:
            cursor_x -= 1
        elif key == curses.KEY_RIGHT and cursor_x < len(board[0]) - 1:
            cursor_x += 1
        elif key == ord('\n'):  # Enter key
            if board[cursor_y][cursor_x] == ' ':
                return cursor_x, cursor_y
        display_board(screen, board, cursor_x, cursor_y)  # Update display with new cursor position

# Function to check if a player has won
def check_winner(board, player):
    size = len(board)
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(size):
        if all(board[row][col] == player for row in range(size)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(size)):
        return True
    if all(board[i][size - i - 1] == player for i in range(size)):
        return True
    return False

# Function to check for a draw
def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

# Function to check if a player has won
def check_winner(board, player):
    size = len(board)
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(size):
        if all(board[row][col] == player for row in range(size)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(size)):
        return True
    if all(board[i][size - i - 1] == player for i in range(size)):
        return True
    return False


## Main function to run the game
def main(screen):
    # Initialize game parameters
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    screen.clear()
    screen.addstr("Enter the size of the board (5-25): ")
    screen.refresh()
    size = int(screen.getstr().decode())
    screen.addstr("Enter the number of players (2-4): ")
    screen.refresh()
    num_players = int(screen.getstr().decode())
    players = [chr(ord('X') + i) for i in range(num_players)]  # Assign symbols to players

    # Get player names
    player_names = []
    for i in range(num_players):
        screen.addstr(f"Enter the name of player {i+1}: ")
        screen.refresh()
        name = screen.getstr().decode()
        player_names.append(name)

    # Initialize game board and cursor position
    board = create_board(size)
    cursor_x, cursor_y = 0, 0

    # Main game loop
    turn = 0
    winner = None
    while True:
        current_player = players[turn % num_players]
        screen.addstr(f"\n{player_names[turn % num_players]}'s turn ({current_player})\n")
        display_board(screen, board, cursor_x, cursor_y)
        x, y = handle_input(screen, board, cursor_x, cursor_y)
        board[y][x] = current_player
        if check_winner(board, current_player):
            winner = player_names[turn % num_players]
            break
        elif check_draw(board):
            winner = "Draw"
            break
        turn += 1
        screen.refresh()
        curses.napms(500)  # Delay between turns

    return winner

# Run the game
if __name__ == "__main__":
    winner = curses.wrapper(main)
    if winner == "Draw":
        print("The game ended in a draw!")
    else:
        print(f"Congratulations, {winner} wins!")