import math #math please help me
import numpy as np

#2-dimensional vector functions
class Vector2:
  def __init__(self, x, y):
    self.x = int(x)
    self.y = int(y)
  
  def __add__(self, other):
    return Vector2(int(self.x + other.x), int(self.y + other.y))
  
  def __sub__(self, other):
    return Vector2(int(self.x - other.x), int(self.y - other.y))
  
  def __eq__(self, other):
    return (int(self.x) == int(other.x)) and (int(self.y) == int(other.y))
  
  #def __ne__(self, other):
  #  return (int(self.x) != int(other.x)) or (int(self.y) != int(other.y))
  #
  #def __lt__(self, other):
  #  return self.magnitude() < other.magnitude()
  #
  #def __gt__(self, other):
  #  return self.magnitude() > other.magnitude()
  #
  #def magnitude(self):
  #  return math.sqrt(self.x**2 + self.y**2)
  
  def direction(self):
    return Vector2(int(round(self.x/math.sqrt(self.x**2 + self.y**2),0)), int(round(self.y/math.sqrt(self.x**2 + self.y**2),0)))
  
  def get_points_along_line(self, other):
    startPoint = Vector2(int(self.x), int(self.y))
    endPoint = Vector2(int(other.x), int(other.y))
    
    pointsAlongLine = []
    currentPoint = startPoint
    lineVector = endPoint - startPoint
    direction = lineVector.direction()
    
    while(currentPoint != endPoint):
      pointsAlongLine.append(currentPoint)
      currentPoint = currentPoint + direction

    pointsAlongLine.append(endPoint)

    return pointsAlongLine
  
  #def max_axis_value(self):
  #  return max(int(self.x), int(self.y))
  #
  #def compare_to_values(self, x, y):
  #  return (int(self.x) == int(x)) and (int(self.y) == int(y))
  
  def __repr__(self):
    return "(" + str(self.x) + ", " + str(self.y) + ")"
  
  def __str__(self):
    return "(" + str(self.x) + ", " + str(self.y) + ")"

#Function to get all points on all lines
def get_num_overlaps(arrayOfLines):
  pointsOnLines = [x[0].get_points_along_line(x[1]) for x in arrayOfLines]
  pointsOnLinesFlattened = [j for i in pointsOnLines for j in i] #google to the rescue

  npPoints = np.array(pointsOnLinesFlattened, dtype=str)
  unique_elements, counts_elements = np.unique(npPoints, return_counts=True)
  overlaps = len([x for x in counts_elements if x > 1])
  return overlaps 

#Load data
file = open("input.txt", "r")

input = [x.strip("\n").split(" -> ") for x in file.readlines()]

lineArray = []

for unformattedLines in input:
  formattedLine = []
  for unformattedPoint in unformattedLines:
    formattedPoint = Vector2(unformattedPoint.split(",")[0],unformattedPoint.split(",")[1])
    formattedLine.append(formattedPoint)
  lineArray.append(formattedLine)

#Get horizontal and vertical lines
horizAndVertLineArray = []

for line in lineArray:
  if line[0].x == line[1].x or line[0].y == line[1].y:
    horizAndVertLineArray.append(line)

numberOfOverlaps = get_num_overlaps(horizAndVertLineArray)
print("Part A: " + str(numberOfOverlaps))

numberOfOverlaps = get_num_overlaps(lineArray)
print("Part B: " + str(numberOfOverlaps))