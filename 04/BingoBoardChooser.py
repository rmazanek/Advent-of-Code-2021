import numpy as np

file = open('input.txt', 'r')

numbers, *boards = [x.strip('\n') for x in file.readlines() if x != '\n']
numbers = [int(x) for x in numbers.split(',')]
boards = [boards[n:n+5] for n in range(0,len(boards),5)]

formattedBoards = []

for board in boards:  
  newBoard = []
  for line in board:
    formattedLine = [line[n:n+2].strip() for n in range(0,len(line),3)]
    newBoard.append(formattedLine)
  formattedBoards.append(newBoard)

boardsToLoad = np.array(formattedBoards, dtype=int)

def get_winning_board(bingoBoards, numbersCalled):
  dummyBoards=np.copy(bingoBoards)
  for i in range(0,len(numbersCalled)):
    for j in range(0,len(dummyBoards)):
      for k in range(0,len(dummyBoards[0])):
        for l in range(0,len(dummyBoards[0][0])):
          if dummyBoards[j][k][l] == numbersCalled[i]:
            dummyBoards[j][k][l] = -1
      for m in range(0, 5):
        if (sum(dummyBoards[j][m,:]) == -5) or (sum(dummyBoards[j][:,m]) == -5):
          winningBoardForSum = np.where(dummyBoards[j] < 0, 0, dummyBoards[j])
          return int(numbersCalled[i]), sum(sum(winningBoardForSum)), np.array([bingoBoards[j]])
      else:
        continue
    else:
      continue

def get_last_winning_board(bingoBoards, numbersCalled):
  dummyBoards=np.copy(bingoBoards)
  winningBoardIndices=[]
  for i in range(0,len(numbersCalled)):
    for j in range(0,len(dummyBoards)):
      for k in range(0,len(dummyBoards[0])):
        for l in range(0,len(dummyBoards[0][0])):
          if dummyBoards[j][k][l] == numbersCalled[i]:
            dummyBoards[j][k][l] = -1
      for m in range(0, 5):
        if (sum(dummyBoards[j][m,:]) == -5) or (sum(dummyBoards[j][:,m]) == -5):
          if(j not in winningBoardIndices) and (len(winningBoardIndices) < len(bingoBoards)-1):
            winningBoardIndices.append(j)
          elif (len(winningBoardIndices) < len(bingoBoards)-1):
            continue
          else:
            winningBoard = np.delete(bingoBoards, winningBoardIndices, axis=0)
            return winningBoard
      else:
        continue
    else:
      continue

lastNumber, boardSum, winningBoard = get_winning_board(boardsToLoad, numbers)
print("Part A: " + str(lastNumber*boardSum))

lastWinningBoard = get_last_winning_board(boardsToLoad, numbers)
lastNumber, boardSum, sameBoard = get_winning_board(lastWinningBoard, numbers)
print("Part B: " + str(lastNumber*boardSum))