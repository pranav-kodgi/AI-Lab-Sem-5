import random


def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")


def check_win(board, player):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] == player:
            return True
    return False


def play():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    print("--- Human (X) vs Computer (O) ---")
    print_board(board)

    for turn in range(9):
        if turn % 2 == 0:
            while True:
                move = input("Your turn (1-9): ")
                if move in board:
                    board[int(move) - 1] = "X"
                    break
                print("Invalid choice, try again.")
            
            print_board(board)
            if check_win(board, "X"):
                print("You won!")
                return
        else:
            print("Computer's turn:")
            empty_spots = [i for i, spot in enumerate(board) if spot not in ["X", "O"]]
            computer_move = random.choice(empty_spots)
            board[computer_move] = "O"
            
            print_board(board)
            if check_win(board, "O"):
                print("Computer wins!")
                return

    print("It's a tie!")


if __name__ == "__main__":
    play()
