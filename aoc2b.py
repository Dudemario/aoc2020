from functools import reduce
numValid = 0
with open("aoc2.txt") as fin:
  for line in fin:
    [policy, letter, text] = line.strip().split(" ")
    [policy1, policy2] = policy.split("-")
    letter = letter[:-1]
    numValid += (int(text[int(policy1) - 1] == letter) + int(text[int(policy2) - 1] == letter)) % 2
print(numValid)