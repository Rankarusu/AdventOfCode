from collections import Counter
import collections

with open("03-input.txt") as file:
	lines = [x.strip("\n") for x in file.readlines()]
	gamma = ""
	epsilon = ""

	#get most common bits
	for i in range(0, len(lines[0])):
		mostcommon = collections.Counter([x[i] for x in lines]).most_common()[0][0]
		gamma += mostcommon
	

	
	intgamma = int(gamma, 2)
	#invert bits to get the least common bits
	intepsilon = int(format(~intgamma & 0b111111111111, '12b'), 2)

	print(bin(intgamma))
	print(bin(intepsilon))
	print(intepsilon * intgamma)