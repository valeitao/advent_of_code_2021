# ADVENT OF CODE : Day 1
# Vasco Leitão

# Q1
# Example result: 7
# Input result: 1446

count = 0
with open("input1.txt", "r") as f:
	lines = [int(l) for l in f.readlines()]

for i in range(1, len(lines)):
	if(lines[i] > lines[i-1]):
		count+=1

print(count)

# Q2
# Example result: 5
# Input result: 1486

count = 0
for i in range(len(lines) - 3):
	if((lines[i] + lines[i+1] + lines[i+2]) < (lines[i+1] + lines[i+2] + lines[i+3])):
		count+=1

print(count)

