
prompt_1 = "Please enter the board size\n"
prompt_2 = "Please enter how many squares you want to place\n"
prompt_3 = "Please enter the coordinates of a square you want to place\n"
prompt_4 = "Please enter a target square coordinate, or enter exit to exit\n"
prompt_5 = "Congratulations, you won!"
prompt_6 = "Thanks for playing."
error_message_1 = "Improper board size"
error_message_2 = "Improper amount of squares"
error_message_3 = "Incorrect input format for square coordinates"
error_message_4 = "Improper square coordinates"
error_message_5 = "Sign already placed to square"


def change(inside):
    if inside == "-":
        return "+"
    elif inside == "+":
        return "-"
    else:
        return inside

while True:
    size = int(input(prompt_1))
    if size < 5 or size > 9 :
        print(error_message_1)
        continue
    break

while True:
    square_number = int(input(prompt_2))
    if square_number < 1 or square_number > (size**2):
        print(error_message_2)
        continue
    break

row = []
board = []
# for first line
for m in range(size + 1):
    if m == 0:
        row.append(" ")
    else:
        row.append(m)
board.append(row)
row = []

# for remaining lines
for i in range(1, size + 1):
    row.append(i)
    for m in range(size):
        row.append("-")
    board.append(row)
    row = []


# EMPTY BOARD
empty_board = []
# for first line
for m in range(size + 1):
    if m == 0:
        row.append(" ")
    else:
        row.append(m)
empty_board.append(row)
row = []

# for remaining lines
for i in range(1, size + 1):
    row.append(i)
    for m in range(size):
        row.append("-")
    empty_board.append(row)
    row = []

# CREATING THE BOARD
while True:
    a = 0
    while a < square_number:
        coordinate = input(prompt_3)
        coordinate = coordinate.split()
        coordinate = [coordinate [0], coordinate[1]]
        try:
            x = int(coordinate[0])
            y = int(coordinate[1])
        except:
            print(error_message_3)
            continue

        if x == int(x) and y == int(y):
            pass
        else:
            print(error_message_3)

        if x > size or y > size or x < 1 or y < 1:
            print(error_message_4)
            continue

        if board[x][y] == "+":
            print(error_message_5)
            continue
        else:
            board[x][y] = change(board[x][y])

        for i in range(size + 1):
            for m in range(size):
                print(board[i][m] , end= " ")
            print(board[i][size],end="")
            print()
        a += 1
    break

# THE ACTUAL GAME
while True:
    target_coordinate = input(prompt_4)

    if target_coordinate.lower().strip() == "exit":
        break

    target_coordinate = target_coordinate.split()
    target_coordinate = [target_coordinate[0],target_coordinate[1]]

    try:
        x = int(target_coordinate[0])
        y = int(target_coordinate[1])
    except:
        print(error_message_3)
        continue

    if x == int(x) and y == int(y):
        pass
    else:
        print(error_message_3)

    if x > size or y > size or x < 1 or y < 1:
        print(error_message_4)
        continue

    if x < size and y < size:
        board[x][y] = change(board[x][y])
        board[x-1][y+1] = change(board[x-1][y+1])
        board[x-1][y-1] = change(board[x-1][y-1])
        board[x+1][y+1] = change(board[x+1][y+1])
        board[x+1][y-1] = change(board[x+1][y-1])
    elif x == size and y < size:
        board[x][y] = change(board[x][y])
        board[x - 1][y + 1] = change(board[x - 1][y + 1])
        board[x - 1][y - 1] = change(board[x - 1][y - 1])

    elif x < size and y == size:
        board[x][y] = change(board[x][y])
        board[x - 1][y - 1] = change(board[x - 1][y - 1])
        board[x + 1][y - 1] = change(board[x + 1][y - 1])

    elif x == size and y == size:
        board[x][y] = change(board[x][y])
        board[x - 1][y - 1] = change(board[x - 1][y - 1])

    for i in range(size + 1):
        for m in range(size):
            print(board[i][m], end=" ")
        print(board[i][size], end="")
        print()

    if board == empty_board:
        print(prompt_5)
        break

print(prompt_6)