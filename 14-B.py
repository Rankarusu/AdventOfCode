from collections import Counter
import itertools

with open("14-input.txt") as file:
    lines = [x.strip() for x in file.readlines()]

poly = lines[0]
dic = {}

for line in lines[2:]:  # skip empty line and string
    k, v = line.split(" -> ")
    dic[k] = v

pairs = Counter(map(''.join, itertools.pairwise(poly)))
elements = Counter(poly)


def polymerize(poly, elements):
    copy = poly.copy()
    for x in copy:
        middle = dic[x]

        left = x[0]  # first char
        right = x[1]  # second char

        num = copy[x]
        a = str(left + middle)
        b = str(middle+right)

        if poly[x] > 0:
            poly.update({a: num, b: num})
            poly[x] -= num
            elements.update({middle: num})

    return (poly, elements)


def compute_output(poly):
    counter = poly.most_common()
    return counter[0][1] - counter[-1][1]


for x in range(40):
    pairs, elements = polymerize(pairs, elements)


print(compute_output(elements))
