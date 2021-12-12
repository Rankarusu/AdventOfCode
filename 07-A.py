def shortest_distance(arr):
    middle = len(arr) //2
    meeting_point = arr[middle]
    dist = 0
    for i in arr:
        dist += abs(meeting_point - i)
    
    print(meeting_point)
    print(dist)



with open("07-input.txt") as file:
    crabs = file.read().strip().split(',')
    crabs = sorted(list(map(int, crabs)))
    shortest_distance(crabs)