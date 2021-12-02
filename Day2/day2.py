# ADVENT OF CODE : Day 2
# Vasco Leitão

with open("input2.txt", "r") as f:
	lines = [l.split(" ") for l in f.readlines()]

# Q1
# Example result: 150
# Input result: 1660158

position = [0, 0]

for l in lines:
	if l[0] == "forward":
		position[0] += int(l[1])
	if l[0] == "down":
		position[1] += int(l[1])
	if l[0] == "up":
		position[1] -= int(l[1])

print(position[0] * position[1])

# Q2
# Example result: 900
# Input result: 16604592846

aim = 0
position = [0, 0]

for l in lines:
	if l[0] == "down":
		aim += int(l[1])
	if l[0] == "up":
		aim -= int(l[1])
	if l[0] == "forward":
		position[0] += int(l[1])
		position[1] += (int(l[1]) * aim)

print(position[0] * position[1])