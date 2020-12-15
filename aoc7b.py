from functools import reduce
d = {}
n = 595
counts = [-1 for _ in range(n)]
adjList = [[] for _ in range(n)]
counter = 0
with open("aoc7.txt") as fIn:
  for line in fIn:
    line = line.strip()[:-1].split(" contain ")
    root = line[0].split(" bag")[0]
    leaves = list(map(lambda x:x.split(' ', 1)[1].split(" bag")[0], line[1].split(", ")))
    leaveCounts = list(map(lambda x:x.split(' ', 1)[0], line[1].split(", ")))
    leaveCounts = list(map(lambda x:int(x) if x.isdigit() else 0,leaveCounts))
    for i in [root]+leaves:
      if d.get(i, -1) == -1:
        d[i] = counter
        counter += 1
    adjList[d[root]] = zip(list(map(lambda x:d[x], leaves)), leaveCounts)
if counter != n:
  print('sdfsdf')
  quit()
k = d['shiny gold']
e = d['other']
def search(curNode):
  bagsInHere = 0
  for i,count in adjList[curNode]:
    if i == e:
      continue
    if counts[i] == -1:
      search(i)
    bagsInHere += count * (1+counts[i])
  counts[curNode] = bagsInHere
search(k)
print(counts[k])