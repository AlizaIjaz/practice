import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def tick_tack_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    print("Welcome to Tick-Tack-Toe!")

    while True:
        clear()
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, 2): "))
        
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != ' ':
            print("Invalid move. Try again.")
            input("Press Enter to continue...")
            continue
        
        board[row][col] = current_player

        if check_winner(board, current_player):
            clear()
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            clear()
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = 'X' if current_player == 'O' else 'O'

if __name__ == "__main__":
    tick_tack_toe()
