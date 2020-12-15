from functools import reduce
d = {}
n = 595
possible = [-1 for _ in range(n)]
adjList = [[] for _ in range(n)]
counter = 0
with open("aoc7.txt") as fIn:
  for line in fIn:
    line = line.strip()[:-1].split(" contain ")
    root = line[0].split(" bag")[0]
    leaves = list(map(lambda x:x.split(' ', 1)[1].split(" bag")[0], line[1].split(", ")))
    for i in [root]+leaves:
      if d.get(i, -1) == -1:
        d[i] = counter
        counter += 1
    adjList[d[root]] = list(map(lambda x:d[x], leaves))
if counter != n:
  print('sdfsdf')
  quit()
k = d['shiny gold']
e = d['other']
def search(curNode):
  possibleFromHere = 0
  for i in adjList[curNode]:
    if i == k or possible[i] == 1:
      possibleFromHere = 1
      break
    # if i == e or possible[i] == 0:
    #   possibleFromHere = 0
    elif possible[i] == -1:
      possibleFromHere = possibleFromHere | search(i)
      if possibleFromHere == 1:
        break
  possible[curNode] = possibleFromHere
  return possibleFromHere
for i in range(n):
  search(i)
print(len([1 for i in possible if i == 1]))