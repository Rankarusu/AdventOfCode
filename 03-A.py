from collections import Counter
import collections

with open("03-input") as file:
	lines = [x.strip("\n") for x in file.readlines()]
	gamma = ""
	epsilon = ""

	for i in range(0, len(lines[0])):
		mostcommon = collections.Counter([x[i] for x in lines]).most_common()[0][0]
		gamma += mostcommon
	intgamma = int(gamma, 2)
	intepsilon = ~int(intgamma)
	
	print(bin(intgamma))
	print(bin(intepsilon))
