from functools import reduce
def getIndexFunc(width):
  def getIndex(x, y):
    return x + y[1] * 2**(width-y[0])
  return getIndex
minId = 806
maxId = 0
sumIds = 0
with open("aoc5.txt") as fIn:
  for line in fIn:
    line = list(map(lambda x:int(x == "B" or x == "R"), list(line.strip())))
    row = reduce(getIndexFunc(6), zip(range(7), line[:-3]), 0)
    col = reduce(getIndexFunc(2), zip(range(3), line[-3:]), 0)
    minId = min(minId, row * 8 + col)
    maxId = max(maxId, row * 8 + col)
    sumIds += row * 8 + col
total = int((maxId + minId) * (maxId - minId + 1) / 2)
print(total - sumIds)