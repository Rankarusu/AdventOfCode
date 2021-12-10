hor = 0
depth = 0
aim = 0

with open("02-input.txt") as file:
    for line in file:
        linearr = line.strip("\n").split(" ")
        command = linearr[0]
        x = int(linearr[1])

        if command == "forward":
            hor += x
            depth += aim * x
        if command == "down":
            aim += x
        if command == "up":
            aim -= x
        print(hor, depth)

print(hor * depth)
