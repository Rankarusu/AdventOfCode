from collections import Counter 

with open("14-input.txt") as file:
    lines = [x.strip() for x in file.readlines()]

poly = lines[0]
dic = {}

for line in lines[2:]: #skip empty line and string
    k,v = line.split(" -> ")
    dic[k] = v


def polymerize(poly):
    res = []
    for i in range(0, len(poly)-1):
        temp = str(poly[i])+str(poly[i+1])
        insert = dic[temp]
        res.append(poly[i])
        res.append(insert)

    res.append(poly[-1])
    return "".join(res)

def compute_output(input): #
    counter = Counter(input).most_common()
    return counter[0][1] - counter[-1][1]



for x in range(40):
    poly = polymerize(poly)
    print(x)

print(compute_output(poly))
