ar = []
with open("t.txt") as fin:
  for line in fin:
    n = int(line.strip())
    ar.append(n)
for i in range(len(ar)):
  d = {}
  twoSum = 2020 - ar[i]
  for j in range(i, len(ar)):
    if d.get(ar[j], -1) != -1:
      print(ar[i] * ar[j] * (twoSum - ar[j]))
    else:
      d[twoSum - ar[j]] = 1
