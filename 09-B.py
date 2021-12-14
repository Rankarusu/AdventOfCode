def get_cell(board, x, y):
    try:
        return int(board[x][y])
    except IndexError:
        return 9  # border of map is equal to a high node, probably not needed, lul


def check_surroundings(board, x, y):
    if board[x][y] < get_cell(board, x-1, y)\
        and board[x][y] < get_cell(board, x+1, y)\
        and board[x][y] < get_cell(board, x, y-1)\
        and board[x][y] < get_cell(board, x, y+1):
        return (x,y)


def checkbasin(board, x, y, result):
    if x < 0 or y < 0: #python does work with negative indices. it then starts to count from the right.
        return

    if (x, y) not in result:
        result.append((x,y))
        
        if get_cell(board, x-1, y) != 9:
            checkbasin(board, x-1, y, result)
        if get_cell(board, x+1, y) != 9:
            checkbasin(board, x+1, y, result)
        if get_cell(board, x, y-1) != 9:
            checkbasin(board, x, y-1, result)
        if get_cell(board, x, y+1) != 9:
            checkbasin(board, x, y+1, result)



with open("09-input.txt") as file:

    lines = [x.strip() for x in file.readlines()]
    board = [list(map(int, x)) for x in lines]

    
    lows = []
    for k in range(len(board)):
        for l in range(len(board[k])):
            lowpoint = check_surroundings(board, k, l)
            if lowpoint: 
                lows.append(lowpoint)
    #get the basin for all low points 
    basins = [[] for x in lows]
    for i in range(len(lows)): 
        point = lows[i]
        checkbasin(board, point[0], point[1], basins[i])
    
    result = 1

    basins = sorted(basins, key=len, reverse=True)[:3] #sorts the list by length of the items in descendinf order and return 3 items.

    for x in basins:
        result *= len(x)

    print(result)


    