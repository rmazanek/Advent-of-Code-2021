import numpy as np

dumboInitialState = np.genfromtxt('input.txt', dtype=int, delimiter=1)
initRows, initCols = dumboInitialState.shape
dayToCountFlashes = 100
days = 400
flashCounter=0

class DumboGrid:
  def __init__(self, input):
    self.mapRows = input.shape[0]
    self.mapCols = input.shape[1]
    self.dumboList = []
    for i in range(0, self.mapRows):
      for j in range(0, self.mapCols):
        newDumbo = Dumbo(i, j, self.mapRows, self.mapCols, input[i,j])
        self.dumboList.append(newDumbo)
  
  def get_all_dumbos(self):
    return self.dumboList
  
  def get_all_dumbos_flashing(self):
    flashingDumbos = []
    
    for dumbo in self.dumboList:
      if dumbo.hasFlashed:
        flashingDumbos.append(dumbo)

    return flashingDumbos
  
  def get_dumbo_by_x_y(self, x, y):
    dumbo = next(filter(lambda a: (a.x==x and a.y==y), self.dumboList))
    return dumbo
  
  def __repr__(self):
    formattedDumboList = np.reshape([str(x) for x in self.dumboList], (self.mapRows, self.mapCols))
    return str(formattedDumboList)

  def __iter__(self):
    return GridIterator(self)

class Dumbo:
  def __init__(self, x, y, maxRows, maxCols, energyLevel=0):
    self.hasFlashed=False
    self.x = x
    self.y = y
    self.maxRows = maxRows
    self.maxCols = maxCols
    self.energyLevel = energyLevel
    self.dumboGrid = []
  
  def reset_flash(self):
    self.hasFlashed=False
    
  def flash(self):
    global flashCounter
    self.energyLevel=0
    self.hasFlashed=True
    flashCounter+=1
    self.energize_neighbors()
  
  def increment_energy(self):
    if self.hasFlashed == False:
      if self.energyLevel == 9:
        self.flash()
        self.energyLevel=0
      else:
        self.energyLevel+=1
  
  def get_neighbor_locations(self):
    neighbors = []
    for i in range(-1,2):
      for j in range(-1,2):
        if (i==0 and j==0):
          continue #skip self
        elif (self.x+i < 0) or (self.y+j < 0) or (self.x+i >= self.maxRows) or (self.y+j >= self.maxCols):
          continue #skip outside of array bounds
        else:
          neighbors.append((self.x+i, self.y+j))
    return neighbors
  
  def get_neighbor_dumbos(self):
    neighborLocs = self.get_neighbor_locations()
    neighborDumbos = []
    for neighborLoc in neighborLocs:
      dumbo = self.dumboGrid.get_dumbo_by_x_y(neighborLoc[0], neighborLoc[1])
      neighborDumbos.append(dumbo)
    return neighborDumbos

  def store_grid_state(self, dumbos):
    self.dumboGrid = dumbos
  
  def energize_neighbors(self):
    neighbors = self.get_neighbor_dumbos()
    for dumbo in neighbors:
      dumbo.increment_energy()
    
  def __repr__(self):
    return str(self.energyLevel)

class GridIterator:
  ''' Iterator class '''
  def __init__(self, grid):
    # Grid object reference
    self._grid = grid
    # member variable to keep track of current index
    self._index = 0
  def __next__(self):
    ''''Returns the next value from grid object's lists '''
    if self._index < len(self._grid.dumboList):
      dumbo = self._grid.dumboList[self._index]
      self._index +=1
      return dumbo
    # End of Iteration
    raise StopIteration  

def main():
  #Initialize grid and message
  dumboGrid = DumboGrid(dumboInitialState)
  dayAllFlashingMessage = "No day where all are flashing. Add more days."
  waitingForFlash = True
  
  #Show day 0 grid
  #print("Day 0: " + str(flashCounter) + " flashes")
  #print(dumboGrid)
  
  #Iterate over days
  for i in range(0, days):
    dayNumber = i+1
    
    for dumbo in dumboGrid:
      dumbo.reset_flash()

    for dumbo in dumboGrid:
      dumbo.store_grid_state(dumboGrid)
      dumbo.increment_energy()
    
    #print("Day " + str(dayNumber) + ": " + str(flashCounter) + " flashes")
    #print(dumboGrid)
    
    if(dayNumber == dayToCountFlashes):
      print("Part A: " + str(flashCounter))
    
    if waitingForFlash:
      if(len(dumboGrid.get_all_dumbos_flashing()) == len(dumboGrid.dumboList)):
        dayAllFlashingMessage = "First day all flashing: " + str(dayNumber)
        waitingForFlash=False

  print("Part B: " + dayAllFlashingMessage)

if __name__ == "__main__":
  main()