# ADVENT OF CODE : Day 9
# Vasco Leitão

with open("example9.txt", "r") as f:
	lines = f.read().split("\n")

# Q1
# Example result: 15
# Input result: 570

def get_low_points(grid):
	low_points = 0
	low_coordinates = []
	for i in range(len(lines)):
		for j in range(len(lines[i])):
			val = lines[i][j]
			if i != 0:
				if lines[i-1][j] <= val:
					continue
			if i != len(lines) - 1:
				if lines[i+1][j] <= val:
					continue
			if j != 0:
				if lines[i][j-1] <= val:
					continue
			if j != len(lines[i]) - 1:
				if lines[i][j+1] <= val:
					continue
			low_points += int(val) + 1
			low_coordinates.append([i, j])
	return low_points, low_coordinates

low_points, low_coordinates = get_low_points(lines)
print(low_points)

