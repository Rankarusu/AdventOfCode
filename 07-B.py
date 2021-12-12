import math

def shortest_distance(arr):
    middle = len(arr) // 2
    meeting_point = math.floor(sum(arr)/len(arr)) #it's either round or floor. one of them will retunr the solution
    dist = 0
    for i in arr:
        n = abs(meeting_point -i)
        dist += (n*(n + 1)) //2
    
    print(meeting_point)
    print(dist)


with open("07-input.txt") as file:
    crabs = file.read().strip().split(',')
    crabs = list(map(int, crabs))
    crabs.sort()

    shortest_distance(crabs)