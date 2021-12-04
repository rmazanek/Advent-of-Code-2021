from statistics import mode, multimode
import numpy as np

file = open('input.txt', 'r')
readings = [x.strip("\n") for x in file.readlines()]

readingsMode = []

for i in range(0,len(readings[0])):
  readingsMode.append(mode([int(x[i]) for x in readings]))

readingsAntiMode = [int(not x) for x in readingsMode]

gamma = int(''.join([str(x) for x in readingsMode]),2)
epsilon = int(''.join([str(x) for x in readingsAntiMode]),2)

print('Part A: ' + str(gamma*epsilon))

modeMatches = []

#Get Oxygen Rating
remainingReadings = [x for x in readings]
  
for i in range(0,len(readings[0])):
  iBitOfRemainingReadings = [int(x[i]) for x in remainingReadings]
  print(iBitOfRemainingReadings)
  modeForFirstBit = max(multimode(iBitOfRemainingReadings))   #Uses maximum of modes returned
  print(modeForFirstBit)
  remainingReadings = [x for x in remainingReadings if int(x[i])==modeForFirstBit]
  print(remainingReadings)
  if(len(remainingReadings)==1):
    oxygenRating = remainingReadings[0] #Sets oxygen rating
    break

#Get CO2 Rating
remainingReadings = [x for x in readings] #Reset set of readings

for i in range(0,len(readings[0])):
  iBitOfRemainingReadings = [int(x[i]) for x in remainingReadings]
  print(iBitOfRemainingReadings)
  modeForFirstBit = int(not(max(multimode(iBitOfRemainingReadings))))  #Flips the bit from 0 to 1 (or vice versa) compared to oxygen method above
  print(modeForFirstBit)
  remainingReadings = [x for x in remainingReadings if int(x[i])==modeForFirstBit]
  print(remainingReadings)
  if(len(remainingReadings)==1):
    co2Rating = remainingReadings[0]  #Sets CO2 rating
    break

oxygenRating = int(oxygenRating,2)
co2Rating = int(co2Rating,2)

print(oxygenRating)
print(co2Rating)
print('Part B: ' + str(oxygenRating*co2Rating))

