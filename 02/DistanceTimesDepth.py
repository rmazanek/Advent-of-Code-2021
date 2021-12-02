file = open('directions.txt', 'r')
aHoriz, aDepth, bHoriz, bDepth = 0, 0, 0, 0

for line in file.readlines():
  direction, value = line.strip("\n").split(" ")
  value = int(value)
  if(direction == 'forward'):
    aHoriz+=value
    bHoriz+=value
    bDepth+=value*aDepth #aim is depth from part A
  elif(direction == 'down'):
    aDepth+=value
  else:
    aDepth-=value

print("Part A: " + str(aHoriz*aDepth))
print("Part B: " + str(bHoriz*bDepth))