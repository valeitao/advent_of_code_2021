# ADVENT OF CODE : Day 6
# Vasco Leitão

from collections import Counter, defaultdict

with open("input6.txt", "r") as f:
	fishes = [int(s) for s in f.read().split(",")]

# Q1
# Example result: 5934
# Input result: 394994

def create_lanterns(fishes, days):
	new_fishes = fishes.copy()
	for j in range(days):
		i = 0
		day_fishes = len(new_fishes)
		for i in range(day_fishes):
			if new_fishes[i] == 0:
				new_fishes[i] = 6
				new_fishes.append(8)
			else:
				new_fishes[i] -= 1
			i+=1
	return new_fishes

new_fishes = create_lanterns(fishes, 80)
print(len(new_fishes))

# Q2
# Example result: 26984457539
# Input result: 1765974267455

count_fishes = Counter(fishes)

def create_lanterns(fishes, days):
	count_fishes = fishes
	for j in range(days):
		num_dict = defaultdict(int)
		for d, fishes in count_fishes.items():
			if d == 0:
				num_dict[8] += fishes
				num_dict[6] += fishes
			else:
				num_dict[d-1] += fishes
		count_fishes = num_dict
	return sum(count_fishes.values())

new_fishes = create_lanterns(count_fishes, 256)
print(new_fishes)