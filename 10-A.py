from collections import Counter

with open("10-input.txt") as file:

    lines = [x.strip() for x in file.readlines()]
    #counter = Counter({'(', ')', '[', ']', '{', '}', '<', '>'})

    values = {')': 3, ']': 57, '}': 1197, '>': 25137}

    sum = 0
    for line in lines:
        stack = []
        for bracket in line:
            if bracket in {'(', '[', '{', '<'}:
                # latest opening bracket is always on top and is the first one to be closed
                stack.append(bracket)
            else:
                if bracket == ')' and stack[-1] == '(':
                    stack.pop()
                elif bracket == ']' and stack[-1] == '[':
                    stack.pop()
                elif bracket == '}' and stack[-1] == '{':
                    stack.pop()
                elif bracket == '>' and stack[-1] == '<':
                    stack.pop()
                else:
                    sum += values[bracket]
                    break

    print(sum)
