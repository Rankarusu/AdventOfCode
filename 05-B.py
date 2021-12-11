
def mark(board, start:tuple, end:tuple):
    """
    marks horizontal, vertical and diagonal lines in the board
    """
    if start[0] == end[0]:
        low, high = sorted([start[1], end[1]]) # make sure to use the right range
        y = start[0]
        for i in range(low, high+1):
            board[i][y] += 1

    elif start[1] == end[1]:
        low, high = sorted([start[0], end[0]])
        x = start[1]
        for i in range(low, high+1):
            board[x][i] += 1

    elif abs(start[0] - end[0]) == abs(start[1] - end[1]):
        a,b = start[0], start[1]
        board[b][a] += 1  
        while a != end[0] and b != end[1]:
            
            if a < end[0]:
                a +=1
            else:
                a -= 1
        
            if b < end[1]:
                b +=1
            else:
                b -= 1  
            
            board[b][a] += 1
          #i hate my life
          #but i hate math more
        

def count_danger(board):
    """
    count all fields with 2 or more overlapping lines.
    """
    counter = 0
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] >= 2:
                counter += 1
    return counter

board = [[0 for x in range(1000)] for y in range(1000)] # just use 1000 here. we could technically calculate this. but there is no need to.

with open("05-input.txt") as file:
    lines = [x.strip("\n") for x in file.readlines()]
    for line in lines:
        splitline = line.split("->")
        x = tuple(map(int, splitline[0].split(",")))
        y = tuple(map(int, splitline[1].split(",")))
        mark(board, x, y)

print(count_danger(board))
