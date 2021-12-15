import numpy as np

input = np.genfromtxt('input.txt', dtype=str)
stackLastOpen = []
incompleteLines = []
errorList = []

openers = {"[": "]", "(": ")", "{": "}", "<": ">"}
stackDictionary = {"[": "Square", 
                   "]": "Square", 
                   "(": "Paren",
                   ")": "Paren",
                   "{": "Curly",
                   "}": "Curly",
                   "<": "Angle",
                   ">": "Angle"}
pointDictionary = {")": 3, "]": 57, "}": 1197, ">": 25137}
autocompleteScoreDictionary = {")": 1, "]": 2, "}": 3, ">": 4}

def pop_from_stack_success(item, listOfErrors): 
  if((len(stackDictionary[item]) == 0) or (stackDictionary[item] != stackDictionary[stackLastOpen[-1]])):
    listOfErrors.append(item)
    return False
  else:
    stackLastOpen.pop()
    return True

def score_autocomplete(string):
  score=0
  for char in string:
    score = score * 5 + autocompleteScoreDictionary[char]
  return score

for line in input:
  saveLine = True
  stackLastOpen.clear()
  
  for item in line:
    if item in openers.keys():
      stackLastOpen.append(item)
      continue
    elif pop_from_stack_success(item, errorList):
      continue
    else:
      saveLine = False
      break

  if saveLine:
    incompleteLines.append(stackLastOpen.copy())

score = [pointDictionary[x] for x in errorList]
print("Part A: " + str(sum(score)))

lineScores = []

for incompleteLine in incompleteLines:
  closers = [openers[x] for x in reversed(incompleteLine)]
  lineScores.append(score_autocomplete(closers))

middleIndex = int(len(lineScores)/2)
winningScore = sorted(lineScores)[middleIndex]
print("Part B: " + str(winningScore))