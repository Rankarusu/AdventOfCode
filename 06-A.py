def day(fishes:list, times:int):
    for i in range(times):
        for x in range(len(fishes)): #use a copy of the list since we modify it in the process
            if fishes[x] == 0:
                fishes[x] = 6
                fishes.append(8)
            else:
                fishes[x] -= 1
    print(fishes)



with open("06-input.txt") as file:
    line = file.readline()
    arr = [int(x) for x in line.split(",")]


day(arr, 80)
print(len(arr))

