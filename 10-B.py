from collections import Counter

def process_brackets(brackets:list, stack:list ):
    for bracket in brackets:
        if bracket in {'(', '[', '{', '<'}:
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
                return None # go to next line if corrupted
    return stack


with open("10-input.txt") as file:

    lines = [x.strip() for x in file.readlines()]

sum = 0
scores = []
for line in lines:
    stack = []
    sum = 0
    stack = process_brackets(line, stack)
    if stack is not None:
        stack.reverse() #there are no real stacks in python
        for remainder in stack: 
            sum *= 5
            if remainder == '(': 
                sum += 1 
            elif remainder == '[': 
                sum += 2 
            elif remainder == '{': 
                sum += 3 
            elif remainder == '<': 
                sum += 4 
        scores.append(sum)
scores.sort()
median = int((len(scores))/2)
print(scores[median])
