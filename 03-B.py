from collections import Counter
import collections
		
def get_diagnostic(numbers, fallback, commodity, pos = 0): #yay, recursion!
	"""
	:param numbers: list of numbers
	:param pos: the current cusrion position. increments on recursion
	:param fallback: the fallback to use if both 0 and 1 are equally common
	:param commodity: use 0 for most common or 1 fro least common
	"""

	if len(numbers) == 1:
		return numbers
	newlist = []
	mostcommon = collections.Counter([x[pos] for x in numbers]).most_common()

	if mostcommon[0][1] == mostcommon[1][1]:
		curnum = str(fallback)
	else:
		curnum = mostcommon[commodity][0]

	for x in numbers:
		if x[pos] == curnum:
			newlist.append(x)
	#print(newlist)
	return get_diagnostic(newlist, fallback, commodity, pos+1)

#================================================================

with open("03-input.txt") as file:

	lines = [x.strip("\n") for x in file.readlines()]
	oxygen = get_diagnostic(lines, 1, 0)[0] # get number by most common for oxygen
	co2 = get_diagnostic(lines, 0, 1)[0] # get number by least common for co2
	print(oxygen)
	print(co2)
	print(int(oxygen, 2) * int(co2, 2))
