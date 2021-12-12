from collections import Counter

with open("08-input.txt") as file:
    lines = file.readlines()
    lines = [x.split("|")[1].strip() for x in lines]
    counters = Counter({x: 0 for x in range(8)})
    for line in lines:
        for x in line.split():
            a = len(x)
            counters[len(x)] +=1

    print(counters)
    print(counters[2]+ counters[3] + counters[4] + counters[7])
 