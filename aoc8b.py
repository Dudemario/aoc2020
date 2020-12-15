ar = []
counter = 0
with open("aoc8.txt") as fin:
  for line in fin:
    line = line.strip().split(' ')
    instr = line[0]
    sign = 1 if line[1][0] == '+' else -1
    value = sign * int(line[1][1:])
    if instr == "nop":
      ar.append((1,value,-1))
    elif instr == "acc":
      ar.append((1,value,0))
    else:
      ar.append((value, value,1))
    counter += 1
visited = [False for _ in range(counter)]
visited2 = [False for _ in range(counter)]
visited3 = [False for _ in range(counter)]
i = 0
accum = 0
while not visited[i]:
  visited[i] = True
  instr = ar[i]
  if instr[2] == 0:
    accum += instr[1]
  i += instr[0]
i = 0
accum = 0
while not visited2[i]:
  visited2[i] = True
  instr = ar[i]
  if instr[2] == -1:
    if visited2[i+instr[1]] == False:
      newI = i+instr[1]
      accum2 = 0
      while not visited3[newI] and not newI >= counter:
        visited3[newI] = True
        instr = ar[newI]
        if instr[2] == 0:
          accum2 += instr[1]
        newI += instr[0]
      if newI >= counter:
        print(accum2)
        break
  if instr[2] == 1:
    if visited2[i+1] == False:
      newI = i+1
      accum2 = 0
      while not visited3[newI] and not newI >= counter:
        visited3[newI] = True
        instr = ar[newI]
        if instr[2] == 0:
          accum2 += instr[1]
        newI += instr[0]
      if newI >= counter:
        print(accum2)
        break
  visited3[i] = True
  accum += instr[1]
  i += instr[0]

