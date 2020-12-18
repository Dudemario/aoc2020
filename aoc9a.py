def twoSum(l, n):
  d = {}
  for i in l:
    if d.get(i, -1) != -1:
      return True
    d[n-i] = True
  return False

l = []
buffer = []
with open("aoc9.txt") as fin:
  for line in fin:
    if len(buffer) < 25:
      buffer.append(int(line.strip()))
    else:
      l.append((buffer, int(line.strip())))
      buffer = buffer[1:] + [int(line.strip())]

for preamble, total in l:
  if twoSum(preamble, total) == False:
    print(total)
    break
