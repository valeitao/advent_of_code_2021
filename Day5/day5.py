# ADVENT OF CODE : Day 5
# Vasco Leitão

import re
with open("input5.txt", "r") as f:
	lines = f.read().split("\n")

# Q1
# Example result: 5
# Input result: 7380

def get_vents(vents):
	i=0
	max_num = 0
	while i < len(vents):
		vents[i] = [int(s) for s in re.findall(r'\b\d+\b', vents[i])]
		if (vents[i][0] != vents[i][2]) and (vents[i][1] != vents[i][3]) :
			vents.remove(vents[i])
		else:
			max_num = max(max_num, max(vents[i]))
			i+=1
	return vents, max_num

def get_matrix(limit):
	return [[0 for x in range(limit+1)] for y in range(limit+1)] 

def get_points(p1, p2):
	points = []
	if p1[0] != p2[0]:
		min_x = min(p1[0], p2[0])
		max_x = max(p1[0], p2[0])
		for i in range(min_x, max_x+1):
			points.append((i, p1[1]))
	else:
		min_y = min(p1[1], p2[1])
		max_y = max(p1[1], p2[1])
		for i in range(min_y, max_y+1):
			points.append((p1[0], i))
	return points

vents = lines.copy()
vents, max_num = get_vents(vents)
matrix = get_matrix(max_num)

for l in vents:
	points = [(l[0], l[1]), (l[2], l[3])]
	for p in get_points(points[0], points[1]):
		matrix[p[1]][p[0]]+=1

count = 0
for m in matrix:
	for num in m:
		if num > 1:
			count+=1

print(count)


# Q2
# Example result: 12
# Input result: 21373

def get_vents_diagonal(vents):

	def check_diagonal(p1, p2):
		return ((p1[0] - p1[1]) == (p2[0] - p2[1])) or ((p1[0] + p1[1]) == (p2[0] + p2[1]))

	i=0
	max_num = 0
	new_vents = []
	for i in range(len(vents)):
		vents[i] = [int(s) for s in re.findall(r'\b\d+\b', vents[i])]
		if ((vents[i][0] == vents[i][2]) or
		   (vents[i][1] == vents[i][3]) or
		   check_diagonal((vents[i][0], vents[i][1]), (vents[i][2], vents[i][3]))) :
		   new_vents.append(vents[i])
		   max_num = max(max_num, max(vents[i]))
		   i+=1
	return new_vents, max_num

def get_points(p1, p2):
	points = []
	x1, y1 = p1[0], p1[1]
	x2, y2 = p2[0], p2[1]

	if x2 >= x1: 
		dx = 1 
	else:
		dx = -1

	if y2 >= y1:
		dy = 1  
	else:
		dy = -1

	if y1 == y2:
		min_x = min(p1[0], p2[0])
		max_x = max(p1[0], p2[0])
		for i in range(min_x, max_x+1):
			points.append((i, p1[1]))
	elif x1 == x2:
		min_y = min(p1[1], p2[1])
		max_y = max(p1[1], p2[1])
		for i in range(min_y, max_y+1):
			points.append((p1[0], i))
	else:
		y = y1
		for x in range(x1, x2+dx, dx):
			points.append((x,y))
			y += dy

	return points	

vents = lines.copy()
vents, max_num = get_vents_diagonal(lines)
matrix = get_matrix(max_num)

for l in vents:
	points = [(l[0], l[1]), (l[2], l[3])]
	for p in get_points(points[0], points[1]):
		matrix[p[1]][p[0]]+=1

count = 0
for m in matrix:
	for num in m:
		if num > 1:
			count+=1

print(count)