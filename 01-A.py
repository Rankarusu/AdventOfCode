counter = -1 # first one will always increase, so we start counting at -1

prev = 0

with open("01-input") as file:
    for line in file:
        lineint = int(line.strip("\n"))
        if lineint > prev:
            counter+=1
            print(f"{prev} -> {lineint}, increased")
        else:
            print(f"{prev} -> {lineint} decreased")
        prev = lineint

print(counter)