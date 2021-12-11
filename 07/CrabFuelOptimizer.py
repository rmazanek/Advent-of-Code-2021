import numpy as np

file = open('input.txt', 'r')

input = np.genfromtxt(file,dtype=int,delimiter=',')

minX, maxX = min(input), max(input)

def increasing_sum(number):
  return sum([i for i in range(0, number+1)])

def get_fuel_cost_dict(use_increasing_sum=False):
  fuelCostDict = {horiz: None for horiz in range(minX, maxX+1)}
  for i in range(minX, maxX+1):
    testHoriz = np.array([i] * len(input))
    if use_increasing_sum:
      distanceToHorizontal = abs(testHoriz - input)
      fuelCost = sum(np.array([increasing_sum(x) for x in distanceToHorizontal]))
    else:
      fuelCost = sum(abs(testHoriz - input))
    
    fuelCostDict[i] = fuelCost
  return fuelCostDict

print("Part A: " + str(min(get_fuel_cost_dict().values())))
print("Part B: " + str(min(get_fuel_cost_dict(True).values())))