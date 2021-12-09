counter = 0 # first one will always increase, so we start counting at -1

prev = 0

lines = [int(i) for i in open("01-input").readlines()]

prevsum = lines[0] + lines[1] + lines[2]

for i in range(1, len(lines)-1):
    sum = lines[i-1] + lines[i] + lines[i+1]
    if sum > prevsum:
        counter +=1
        print(f"{prevsum} -> {sum}, increased")
    else:
        print(f"{prevsum} -> {sum} decreased or no change")
    prevsum = sum
print(counter)