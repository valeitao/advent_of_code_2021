# ADVENT OF CODE : Day 8
# Vasco Leitão

import itertools

with open("input8.txt", "r") as f:
	lines = f.read().split("\n")


signals = []
for l in lines:
	signals.append(l.split(" | "))

# Q1
# Example result: 26
# Input result: 530

sum_count = 0
for s in signals:
	sum_count+=sum([1 for el in s[1].split(" ") if len(el) in [2,3,4,7]])

print(sum_count)

# Q2
# Example result: 61229
# Input result: 1051087

decodings = [
	'abcefg',
	'cf',
	'acdeg',
	'acdfg',
	'bcdf',
	'abdfg',
	'abdefg',
	'acf',
	'abcdefg',
	'abcdfg'
]

sum_signals = 0
for s in signals:

	for permutation in itertools.permutations('abcdefg'):

		k = {}
		for el in "abcdefg":
			k[el] = permutation["abcdefg".index(el)]

		decoders = []
		for el in s[0].split(" "):
			new_str = ""
			for char in el:
				new_str += k[char]
			new_str = "".join(sorted(new_str))
			decoders.append(new_str)

		if set(decoders) == set(decodings):
			num = ""
			for el in s[1].split(" "):
				x = ""
				for char in el:
					x += k[char]
				x = "".join(sorted(x))
				num+=(str(decodings.index(x)))
			sum_signals+=int(num)

print(sum_signals)