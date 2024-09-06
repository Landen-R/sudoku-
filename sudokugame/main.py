import random

# Hardcoded password for solving
PASSWORD = "imaquitter1122"


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def is_valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def generate_partial_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    attempts = 10  # Number of random filled cells

    while attempts > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        num = random.randint(1, 9)

        if is_valid(board, num, (row, col)) and board[row][col] == 0:
            board[row][col] = num
            attempts -= 1
    return board


def user_input(board):
    while True:
        print("\nInput your move in the format: row col number (or type 'solve' to solve, 'quit' to quit):")
        move = input().strip().lower()

        if move == 'solve':
            password_attempt = input("Enter password to solve: ")
            if password_attempt == PASSWORD:
                if solve(board):
                    print("Solved board:")
                    print_board(board)
                else:
                    print("No solution exists.")
            else:
                print("Incorrect password. Solve denied.")
            break
        elif move == 'quit':
            print("Exiting the game...")
            break

        try:
            row, col, num = map(int, move.split())
            if is_valid(board, num, (row - 1, col - 1)):
                board[row - 1][col - 1] = num
                print_board(board)
            else:
                print("Invalid move.")
        except:
            print("Invalid input. Try again.")


def main():
    while True:
        board = generate_partial_board()
        print("Generated board:")
        print_board(board)
        user_input(board)

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
