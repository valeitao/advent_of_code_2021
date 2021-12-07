# ADVENT OF CODE : Day 7
# Vasco Leitão

with open("input7.txt", "r") as f:
	positions = [int(s) for s in f.read().split(",")]

# Q1
# Example result: 37
# Input result: 328187

def shift_position(positions, spot):
	fuel = 0
	for p in positions:
		fuel += abs(spot-p)
	return fuel

def optimal_shift(positions):
	max_fuel = shift_position(positions,1)
	for s in range(2, max(positions)):
		fuel = shift_position(positions,s)
		if fuel < max_fuel:
			max_fuel = fuel
		else:
			break
	return max_fuel

print(optimal_shift(positions))

# Q2
# Example result: 168
# Input result: 91257582

def shift_position(positions, spot):
	fuel = 0
	for p in positions:
		fuel += sum(list(range(1, abs(spot-p)+1)))
	return fuel

print(optimal_shift(positions))