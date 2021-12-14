def check_surroundings(board, x: int, y: int):

    for i in range(x-1, x+1):
        for j in range(y-1, y+1):
            try:
                if i == x and j == y:
                    continue
                elif board[i][j] <= board[x][y]:
                    return 0
            except IndexError:
                continue
    print(int(board[x][y]) + 1)
    return int(board[x][y]) + 1

def get_cell(board, x, y):
    try:
        return int(board[x][y])
    except IndexError:
        return 9  # border of map is equal to a high node


def check_surroundings2(board, x, y):
    if board[x][y] < get_cell(board, x-1, y)\
        and board[x][y] < get_cell(board, x+1, y)\
        and board[x][y] < get_cell(board, x, y-1)\
        and board[x][y] < get_cell(board, x, y+1):
        return int(board[x][y]) +1 
    else: return 0
        

with open("09-input.txt") as file:



    lines = [x.strip() for x in file.readlines()]
    board = [list(map(int, x)) for x in lines]


    sum = 0
    for k in range(len(board)):
        for l in range(len(board[k])):
            sum += check_surroundings2(board, k, l)

    print(sum)
