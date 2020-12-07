passport = {}
counter = 0
with open("aoc4.txt") as fin:
  for line in fin:
    if len(line.strip()) == 0:
      valid = 1
      for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if passport.get(key, None) is None:
          valid = 0
      counter += valid
      passport = {}
      continue
    passport.update({pair.split(':')[0]:pair.split(':')[1] for pair in line.strip().split(" ")})
print(counter)