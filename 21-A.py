with open("21-input.txt") as file:
    lines = [x.strip() for x in file.readlines()]

player_one_pos = int(lines[0][-1])
player_one_score = 0
player_two_pos = int(lines[1][-1])
player_two_score = 0

class DiracDie:
    def __init__(self, max=100):
        self.max = max
        self.cur = 1
        self.min = 1
        self.counter = 0 

    def roll(self):
        returnval = self.cur
        self.cur += 1
        if self.cur > self.max: 
            cur = self.min
        self.counter += 1
        return returnval
    
    def roll_thrice(self, times):
        sum = 0
        for i in range(times):
            sum += self.roll()
        return sum



token = True
i = 2 #start at 2 so we can use the middle value
j = 0
die = DiracDie(100)
while player_one_score < 1000 and player_two_score < 1000:

    if token:
        player_one_pos += die.roll_thrice(3)
        if player_one_pos % 10 == 0:
            player_one_pos = 10
        else:
            player_one_pos %= 10
        player_one_score += player_one_pos 
        token = False
    else:
        player_two_pos += die.roll_thrice(3)
        if player_two_pos % 10 == 0:
            player_two_pos = 10
        else:
            player_two_pos %= 10

        player_two_score += player_two_pos 
        token = True
    i += 3
    if i >= 100:
        i = 2
    print(f"player_one: {player_one_pos} - {player_one_score} player_two: {player_two_pos} - {player_two_score}")



print(f"player_one: {player_one_pos} - {player_one_score} player_two: {player_two_pos} - {player_two_score}")
result = min(player_one_score, player_two_score) * die.counter


print(result)
