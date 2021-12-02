file = open('directions.txt', 'r')
aHoriz, aDepth, bHoriz, bDepth, aim = 0, 0, 0, 0, 0

for line in file.readlines():
  direction, value = line.strip("\n").split(" ")
  value = int(value)
  if(direction == 'forward'):
    aHoriz+=value
    bHoriz+=value
    bDepth+=value*aim
  if(direction == 'down'):
    aDepth+=value
    aim+=value
  if(direction == 'up'):
    aDepth-=value
    aim-=value

print("Part A: " + str(aHoriz*aDepth))
print("Part B: " + str(bHoriz * bDepth))