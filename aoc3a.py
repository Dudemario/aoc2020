slope = []
with open("aoc3.txt") as fin:
  for line in fin:
    slope.append(line.strip())

width = len(slope[0])
counter = 0
for i in range(len(slope)):
  if slope[i][3*i % width] == '#':
    counter += 1
print(counter)