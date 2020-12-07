from functools import reduce
numValid = 0
with open("aoc2.txt") as fin:
  for line in fin:
    [policy, letter, text] = line.strip().split(" ")
    [policyMin, policyMax] = policy.split("-")
    letter = letter[:-1]
    count = reduce(lambda x,y:(x + 1) if y == letter else x, text, 0)
    numValid += int(count >= int(policyMin) and count <= int(policyMax))
print(numValid)