answered = [0 for _ in range(26)]
members = 0
total = 0
with open("aoc6.txt") as fIn:
  for line in fIn:
    if len(line.strip()) == 0:
      s = 0
      for i in answered:
        if i == members:
          s += 1
      total += s
      answered = [0 for _ in range(26)]
      members = 0
      continue
    for c in line.strip():
      answered[ord(c) - ord('a')] += 1
    members += 1
print(total)