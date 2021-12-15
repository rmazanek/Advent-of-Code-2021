import numpy as np

input = np.genfromtxt('input.txt', dtype=int, delimiter=1)

#Function that returns only neighbors that exist
def get_neighbors(heightmap, x, y, returnLocationArray=False, maxNeighborValueToKeep=9):
  neighbors = []
  neighborLocations = []
  mapRows, mapCols = heightmap.shape
  if((x-1 >= 0) and (heightmap[x-1, y] <= maxNeighborValueToKeep)):
    neighbors.append(heightmap[x-1, y])           #above
    neighborLocations.append((x-1, y))      
  if((x+1 < mapRows) and (heightmap[x+1, y] <= maxNeighborValueToKeep)):
    neighbors.append(heightmap[x+1, y])           #below
    neighborLocations.append((x+1, y))
  if((y-1 >= 0) and (heightmap[x, y-1] <= maxNeighborValueToKeep)):
    neighbors.append(heightmap[x, y-1])           #left
    neighborLocations.append((x, y-1))
  if((y+1 < mapCols) and (heightmap[x, y+1] <= maxNeighborValueToKeep)):
    neighbors.append(heightmap[x, y+1])           #right
    neighborLocations.append((x, y+1))
  if(returnLocationArray):
    return neighbors, neighborLocations
  else:
    return neighbors

#Function that returns array of lowest points
def get_lowest_points(heightmap, returnLocationArray=False):
  lowestPoints = []
  locationArray = []
  mapRows, mapCols = heightmap.shape
  for i in range(0, mapRows):
    for j in range(0, mapCols):
      neighbors = get_neighbors(heightmap, i, j)
      if(heightmap[i,j] < min(neighbors)):        #check that current point is the lowest
        lowestPoints.append(heightmap[i,j])
        locationArray.append((i,j))
  if(returnLocationArray):
    return np.array(lowestPoints), np.array(locationArray)
  else:
    return np.array(lowestPoints)

lowestPointArray = get_lowest_points(input)
riskLevelArray = lowestPointArray+1               #risk level is 1 + height
riskLevel = sum(riskLevelArray)

print("Part A: " + str(riskLevel))

#For each lowpoint, count points in basin
lowestPointArray, locations = get_lowest_points(input, returnLocationArray=True)

def populate_basin_set(setToPopulate, heightmap, x, y):
  neighbors, neighborLocationsArray = get_neighbors(heightmap, x, y, returnLocationArray=True, maxNeighborValueToKeep=8)
  setToPopulate.add((x,y))
  
  if(len(neighborLocationsArray)>0):
    for i in range(0, len(neighborLocationsArray)):
      xNeighbor = neighborLocationsArray[i][0]
      yNeighbor = neighborLocationsArray[i][1]
      
      if (xNeighbor, yNeighbor) in setToPopulate:
        continue
      else:
        setToPopulate.add((xNeighbor, yNeighbor))
        populate_basin_set(setToPopulate, heightmap, xNeighbor, yNeighbor)

def get_basin_set_counts(heightmap, lowPointLocationsArray):
  basinSetCounts = []
  
  for point in lowPointLocationsArray:
    basinSet = set()
    x = point[0]
    y = point[1]

    populate_basin_set(basinSet, heightmap, x, y)
    basinSetCounts.append(len(basinSet))
  
  return basinSetCounts

basinCounts = get_basin_set_counts(input, locations)
top_3 = sorted(basinCounts)[len(basinCounts)-3:len(basinCounts)]

print("Part B: " + str(np.prod(top_3)))