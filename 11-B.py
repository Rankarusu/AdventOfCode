
class octopi:

    def __init__(self, board):
        self.board = board
        self.counter= 0
        self.flashed =[]

    def rise(self):
        for i in range(len(self.board)): 
            for j in range(len(self.board[i])):
                self.board[i][j] += 1


    def flash_all(self):
        for i in range(len(self.board)): 
            for j in range(len(self.board[i])):
                if self.board[i][j] > 9 and (i,j) not in self.flashed:
                    self.flashed.append((i,j))
                    self.flash(i, j)


    def reset(self):
        for i in range(len(self.board)): 
            for j in range(len(self.board[i])):
                if self.board[i][j] > 9: 
                    self.board[i][j] = 0 
        self.flashed.clear()

    def flash(self, x,y):
        for i in range(x-1, x+2): 
            for j in range(y-1, y+2):
                if (i < 0 or j < 0) or (x==i and y==j) or i > len(self.board)-1 or j > len(self.board)-1:
                    continue # in case we would go out of bounds, also ignore self.
                else:
                    self.board[i][j] += 1
                    if self.board[i][j] > 9 and (i,j) not in self.flashed: #can only flash once.
                        self.flashed.append((i,j))
                        self.flash(i,j)

    def check_for_simul_flash(self):
        arr = []
        for line in self.board:
            arr.extend(line)
        if len(set(arr)) == 1: # each char only once in a set.
            return True
        return False

with open("11-input.txt") as file:
    lines = [x.strip() for x in file.readlines()]
    board = [list(map(int, x)) for x in lines]


sum = 0
oct = octopi(board)

#TIL: python does not have a do while loop
i = 0
while True:
    i += 1
    oct.rise()
    oct.flash_all()
    oct.reset()
    if oct.check_for_simul_flash():
        print(i)
        break
