#I want to use a 2D array and replace called values with something to check for
class Bingo:
    def __init__(self, a, b, c, d, e):
        self.field = []
        self.field.append(a)
        self.field.append(b)
        self.field.append(c)
        self.field.append(d)
        self.field.append(e)

    def trycrossout(self, num):
        for i in range(len(self.field[0])):
            for j in range(len(self.field)):
                if self.field[i][j] == num:
                    self.field[i][j] = "X"
                    return self.checkwin()
        return False

    def checkwin(self):
        if self.checkhor() == True or self.checkvert() == True:
            print("won")
            return self.sum_unmarked()
        return False

    def sum_unmarked(self):
        result = 0
        for i in range(len(self.field[0])):
            for j in range(len(self.field)):
                if self.field[i][j] != "X":
                    result += self.field[i][j]
        return result


    def checkhor(self):
        for x in self.field:
            if len(set(x)) ==1:
                return True
        return False

    def checkvert(self):
        for x in range(0, len(self.field)):
            if len(set([i[x] for i in self.field])) ==1:
                return True
        return False


def check_boards(boards, sequence):
    for x in sequence:
        for board in boards:
            temp = board.trycrossout(int(x)) #returns the sum of the board upon winning or false
            if temp:
                return x, temp

def check_boards2(boards, sequence ):
    for x in sequence:
        for board in list(boards): #iterate over a copy of the list so the iterator is not affected
            temp = board.trycrossout(int(x))#returns the sum of the board upon winning or false
            if temp:
                if len(boards) > 1:
                    boards.remove(board)
                else:
                    return x, temp


boards = []

with open("04-input.txt") as file:
    lines = [x.strip("\n") for x in file.readlines()]
    bingo_sequence = lines[0].split(",")
    #initialize boarads
    for i in range(1, len(lines)-5, 6): #skip first line
        a = [int(x) for x in lines[i+1].split()]
        b = [int(x) for x in lines[i+2].split()]
        c = [int(x) for x in lines[i+3].split()]
        d = [int(x) for x in lines[i+4].split()]
        e = [int(x) for x in lines[i+5].split()]
        obj = Bingo(a, b, c, d, e)
        boards.append(obj)
    
    result = check_boards2(boards, bingo_sequence)
    print(result)
    print(int(result[0]) * result[1])
