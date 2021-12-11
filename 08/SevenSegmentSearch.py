import numpy as np

file = open('input.txt', 'r')
input = np.array([x.replace('|','\n').strip('\n').split() for x in file.readlines()])
dataRows, dataCols = input.shape
numSignals, numDigitalOutputs = 10, 4
signalPatterns = np.array(input[:,:numSignals])
digitalOutputs = np.array(input[:,numSignals:dataCols])

lenVectorized = np.vectorize(len)

lengthOfOutputArray = np.array(lenVectorized(digitalOutputs))

uniqueDigitOutputLengths = np.array([2, 4, 3, 7])

uniqueDigitsFound = [x for x in lengthOfOutputArray.flatten() if x in uniqueDigitOutputLengths]

print("Part A: " + str(len(uniqueDigitsFound)))

#New functions needed for Part B
def all_chars_in_item(item, findChars):
  for i in range(0, len(findChars)):
    if findChars[i] not in item:
      return False
  return True

def all_chars_in_array_items(array, findChars):
  truthArray = []
  for i in range(0, len(array)):
    truthArray.append(all_chars_in_item(array[i], findChars))
  return truthArray

def get_dictionary(listOfTenSignals):
  newDict = {}
  lengthOfSignals = lenVectorized(listOfTenSignals)
  
  #Uniquely mappable numerals
  mask_1 = (lengthOfSignals == 2)
  mask_4 = (lengthOfSignals == 4)
  mask_7 = (lengthOfSignals == 3)
  mask_8 = (lengthOfSignals == 7)
  
  oneString = str(listOfTenSignals[np.where(mask_1)][0]) #Str with length 2 is 1
  fourString = str(listOfTenSignals[np.where(mask_4)][0]) #Str with length 4 is 4
  sevenString = str(listOfTenSignals[np.where(mask_7)][0]) #Str with length 3 is 7
  eightString = str(listOfTenSignals[np.where(mask_8)][0]) #Str with length 7 is 8
  
  #Deduction mappable numerals
  mask_3 = (lengthOfSignals == 5) & (all_chars_in_array_items(listOfTenSignals, oneString)) #Str with length 5 and has all chars from the 1 string is 3
  mask_9 = (lengthOfSignals == 6) & (all_chars_in_array_items(listOfTenSignals, fourString)) #Str with length 6 and has all chars from the 4 string is 9
  mask_0 = (lengthOfSignals == 6) & (all_chars_in_array_items(listOfTenSignals, oneString)) & (~mask_9) #Str with length 6 and has all chars from the 1 (or 7) string but is not 9 is 0
  mask_6 = (lengthOfSignals == 6) & ~mask_9 & ~mask_0
  
  threeString = str(listOfTenSignals[np.where(mask_3)][0]) #Str with length 5 and has all chars from the 1 string is 3
  nineString = str(listOfTenSignals[np.where(mask_9)][0]) #Str with length 6 and has all chars from the 4 string is 9 
  zeroString = str(listOfTenSignals[np.where(mask_0)][0]) #Str with length 6 and has all chars from the 4 string is 9
  sixString = str(listOfTenSignals[np.where(mask_6)][0]) #Str with length 6 and not already found is 6
  
  #Setup argument for finding the number 2
  setInEightButNotNine = set(eightString) - set(nineString)
  stringInEightButNotNine = list(setInEightButNotNine).pop()

  mask_2 = (lengthOfSignals == 5) & (all_chars_in_array_items(listOfTenSignals, stringInEightButNotNine))
  mask_5 = (lengthOfSignals == 5) & ~mask_2 & ~mask_3 #Str with length 5 and not already found is 5
  
  twoString = str(listOfTenSignals[np.where(mask_2)][0]) #Str with length 5 and has string that's in 8 but not in 9 is 2
  fiveString = str(listOfTenSignals[np.where(mask_5)][0]) #Str with length 5 and not already found is 5
  
  #Add all numerals to the dictionary
  newDict[oneString] = 1
  newDict[fourString] = 4
  newDict[sevenString] = 7
  newDict[eightString] = 8
  newDict[threeString] = 3
  newDict[nineString] = 9
  newDict[zeroString] = 0
  newDict[sixString] = 6
  newDict[twoString] = 2
  newDict[fiveString] = 5

  return newDict

def get_decoded_digits(digitsArray, dictionary):
  decodedDigits = []
  
  for i in range(0, len(digitsArray)):
    for k, v in dictionary.items():
      if len(set(digitsArray[i])^set(k)) == 0:
        decodedDigits.append(v)
        break
      else:
        continue

  return decodedDigits

def get_decoded_digits_in_array_of_readings(signalArray, digitsArray):
  allDecodedDigits = []
  
  for i in range(0,len(signalArray)):
    newDictionary = get_dictionary(signalArray[i])
    allDecodedDigits.append(get_decoded_digits(digitsArray[i], newDictionary))
  return allDecodedDigits

#Part B solution
decodedDigits = get_decoded_digits_in_array_of_readings(signalPatterns, digitalOutputs)

concatenatedOutput = []

for i in range(0, len(decodedDigits)):
  item = int(''.join([str(x) for x in decodedDigits[i]]))
  concatenatedOutput.append(item)

print("Part B: " + str(sum(concatenatedOutput)))