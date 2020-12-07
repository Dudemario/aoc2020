from collections import defaultdict
from functools import reduce
slope = []
with open("aoc3.txt") as fin:
  for line in fin:
    slope.append(line.strip())

width = len(slope[0])
counters = defaultdict(int)
for i in range(len(slope)):
  if slope[i][i % width] == '#':
    counters[1] += 1
  if slope[i][3*i % width] == '#':
    counters[2] += 1
  if slope[i][5*i % width] == '#':
    counters[3] += 1
  if slope[i][7*i % width] == '#':
    counters[4] += 1
  if i % 2 == 0 and slope[i][i//2 % width] == '#':
    counters[5] += 1
print(reduce(lambda x,y: x*y, counters.values()))