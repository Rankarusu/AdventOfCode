from collections import deque

def fishgrowth(fishes, days:int):
    totals = deque(fishes.count(i) for i in range(9)) #count the fishes and create a new deque
    for x in range(days):
        totals.rotate(-1) # decrement every number and add 0s to 8s
        totals[6] += totals[8] #also spawn as many new 8s as 6s
    return sum(totals)



with open("06-input.txt") as file:
    fishes = file.read().strip().split(',')
    fishes = list(map(int, fishes))
    result = fishgrowth(fishes, 256)
    print(result)