ar = []
counter = 0
with open("aoc8.txt") as fin:
  for line in fin:
    line = line.strip().split(' ')
    instr = line[0]
    sign = 1 if line[1][0] == '+' else -1
    value = sign * int(line[1][1:])
    if instr == "nop":
      ar.append((1,0))
    elif instr == "acc":
      ar.append((1,value))
    else:
      ar.append((value, 0))
    counter += 1
visited = [False for _ in range(counter)]
i = 0
accum = 0
while not visited[i]:
  visited[i] = True
  instr = ar[i]
  accum += instr[1]
  i += instr[0]
print(accum)
