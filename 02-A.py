hor = 0
depth = 0

with open("02-input.txt") as file:
    for line in file:
        linearr = line.strip("\n").split(" ")
        if linearr[0] == "forward":
            hor += int(linearr[1])
        if linearr[0] == "down":
            depth += int(linearr[1])
        if linearr[0] == "up":
            depth -= int(linearr[1])
        print(hor, depth)

print(hor*depth)