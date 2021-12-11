from os import times
import numpy as np
import time
import math

file = open('input.txt', 'r')

input = [int(x) for x in file.read().split(',')]
projectionDays = 80
fishToday = np.array(input)

totalProjectionDays = projectionDays
fishRegister = {key: 0 for key in range(0, projectionDays+1)}

print(fishRegister)

#3   10  
#2   9
#1   8
#0   7
#6 1 6
#5   5
#4   4
#3   3
#2   2
#1   1
#0   0
#6 2 
class Fish:
  regularDaysBeforeBirth = 6

  def __init__(self, birthday, initialDaysBeforeBirth=8):
      fishRegister[birthday]+=1
      self.birthday = birthday
      self.internalTimer = initialDaysBeforeBirth
  
  def start_having_children():
    while(projectionDay < totalProjectionDays):
      have_a_child()
      projectionDay+=
  
  def have_a_child():
    childFish = Fish(projectionDaysRemaining - )  


def get_birth_days(fishTimer, projectionDaysRemaining):
  headstartDays = 7 - fishTimer - 1
  birth_days = np.zeros(range(0,projectionDaysRemaining), dtype=int)
  
  return(birth_days)
  #headstartDays = 7 - fishTimer - 1
  
  #return max(0, math.floor((headstartDays+projectionDaysRemaining) / 7))

print(get_birth_days(8, projectionDays))

#def how_many_children(fishTimer, projectionDaysRemaining):
#  headstartDays = 7 - fishTimer - 1
#  return max(0, math.floor((headstartDays+projectionDaysRemaining) / 7))
#
#def children_by_day_table_for_new_fish(projectionPeriod):
#  childrenByDayNewFish = {}
#  projectionDay=projectionPeriod
#  while(projectionDay >= 0):
#    childrenByDayNewFish[projectionDay] = how_many_children(8, projectionDay)
#    projectionDay-=1
#  return childrenByDayNewFish
#
#childrenByDayDict = children_by_day_table_for_new_fish(projectionDays)
#childrenByDayDict2 = children_by_day_table_for_new_fish(projectionDays-70)
#print(childrenByDayDict)
#print(childrenByDayDict2)
#
#print(childrenByDayDict- childrenByDayDict2)

#totalFishOnProjectionDay = 0
#futureChildren = sum(np.array(map(how_many_children, fishToday)))
#totalFishOnProjectionDay+=futureChildren
#
#projectionDaysRemaining = projectionDays
#while(projectionDaysRemaining != 0):
#  timeStarted = time.perf_counter()
#  fishToday = decrement_fish_timer(fishToday)
#  totalFishOnProjectionDay+=
#  timeElapsed = time.perf_counter() - timeStarted
#  print("Day " + str(projectionDaysRemaining) + ": " + str(len(fishToday)) + " in " + str(round(timeElapsed,4)) + "s")
#  projectionDaysRemaining-=1

#########################
def decrement_fish_timer(npFishArray):
  npFishArray-=1
  npFishArray = np.append(npFishArray, [8] * sum(npFishArray<0))
  npFishArray = np.where(npFishArray == -1, 6, npFishArray)
  return npFishArray

projectionDaysRemaining = projectionDays
while(projectionDaysRemaining != 0):
  timeStarted = time.perf_counter()
  fishToday = decrement_fish_timer(fishToday)
  timeElapsed = time.perf_counter() - timeStarted
  print("Day " + str(projectionDaysRemaining) + ": " + str(len(fishToday)) + " in " + str(round(timeElapsed,4)) + "s")
  projectionDaysRemaining-=1
