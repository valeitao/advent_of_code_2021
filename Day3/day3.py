# ADVENT OF CODE : Day 3
# Vasco Leitão

with open("input3.txt", "r") as f:
	lines = f.readlines()

# Q1
# Example result: 198
# Input result: 3895776

max_bits = ""
min_bits = ""
for i in range(len(lines[0]) - 1):
	ls = [l[i] for l in lines]
	max_freq = max(set(ls), key = ls.count)
	max_bits+=str(max_freq)

	if(max_freq == "1"):
		min_bits+="0"
	else:
		min_bits+="1"

res = int(max_bits, 2) * int(min_bits, 2)
print(res)

# Q2
# Example result: 198
# Input result: 7928162

def recursive_oxygen(ls,i):

	if len(ls) == 1:
		return int(ls[0], 2)

	zero_count = 0
	zero_xs = []
	one_count = 0
	one_xs = []

	for l in ls:
		if l[i] == '0':
			zero_xs.append(l)
			zero_count+=1
		else:
			one_xs.append(l)
			one_count+=1

	if zero_count <= one_count :
		return recursive_oxygen(one_xs, i+1)
	else:
		return recursive_oxygen(zero_xs, i+1)

def recursive_co2(ls,i):

	if len(ls) == 1:
		return int(ls[0], 2)

	zero_count = 0
	zero_xs = []
	one_count = 0
	one_xs = []

	for l in ls:
		if l[i] == '0':
			zero_xs.append(l)
			zero_count+=1
		else:
			one_xs.append(l)
			one_count+=1	
	if zero_count <= one_count :
		return recursive_co2(zero_xs, i+1)
	else:
		return recursive_co2(one_xs, i+1)

res = recursive_oxygen(lines, 0) * recursive_co2(lines, 0)
print(res)

