def fold_up(grid, index):
    upper = grid[:index]
    lower = grid[index+1:] #make sure to cut the middle line
    lower.reverse()

    for i in range(len(upper)):
        for j in range(len(upper[i])):
            if lower[i][j]:
                upper[i][j] = True

    return upper

def fold_left(grid, index):
    left = [line[:index] for line in grid]
    right = [line[index+1:] for line in grid]

    right = [list(reversed(line)) for line in right]
    
    for i in range(len(left)):
        for j in range(len(left[i])):
            if right[i][j]:
                left[i][j] = True
    return left

def count_dots(grid):
    sum = 0
    for line in grid:
        sum += line.count(True)
    return sum


with open("13-input.txt") as file:
    lines = [x.strip() for x in file.readlines()]


highestx, highesty = 0,0
cords = []
instructions = []
#one could probably just use binary AND for this
#read file and create grid
for line in lines:
    if not line.startswith("fold") and not line == '':
        x,y = line.split(',')
        x,y = int(x), int(y)

        if x > highestx:
            highestx = x
        if y > highesty:
            highesty = y

        cords.append((x,y))
    elif line.startswith("fold"):
        x,y = line.strip("fold along").split('=')
        instructions.append((x,int(y)))


grid = [[False for x in range(highestx+1)] for y in range(highesty+1)]

#fill grid with data
for cord in cords:
    x,y = cord[0], cord[1]
    grid[y][x] = True



for instruction in instructions:
    if instruction[0] == 'x':
        grid = fold_left(grid, instruction[1])
    if instruction[0] == 'y':
        grid = fold_up(grid, instruction[1])
    break
    print(count_dots(grid))
