def print_board(board):
    print("  0 1 2")
    for idx, row in enumerate(board):
        print(idx, " ".join(row))

def check_win(board, mark):
    for row in board:
        if all(s == mark for s in row):
            return True
    for col in range(3):
        if all(row[col] == mark for row in board):
            return True
    if all(board[i][i] == mark for i in range(3)):
        return True
    if all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False

def check_draw(board):
    for row in board:
        if any(s == "-" for s in row):
            return False
    return True

board = [["-" for _ in range(3)] for _ in range(3)]
current_mark = "X"

while True:
    print_board(board)
    print(f"Игрок {current_mark}, сделай ход (номер строки и столбца через пробел): ")

    try:
        row, col = map(int, input().split())
        if board[row][col] != "-":
            print("Эта ячейка уже занята!")
            continue
    except (ValueError, IndexError):
        print("Некорректный ввод. Ввведите номера строки и столбца между 0 и 2 через пробел")
        continue

    board[row][col] = current_mark

    if check_win(board, current_mark):
        print_board(board)
        print(f"Игрок {current_mark} выиграл!")
        break

    if check_draw(board):
        print_board(board)
        print("Ничья!")
        break

    current_mark = "O" if current_mark == "X" else "X"