import re
passport = {}
counter = 0
with open("aoc4.txt") as fin:
  for line in fin:
    if len(line.strip()) == 0:
      valid = 1
      for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if passport.get(key, None) is None:
          valid = 0
      if valid != 0:
        if not passport["byr"].isdigit() or int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002: valid = 0
        elif not passport["iyr"].isdigit() or int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020: valid = 0
        elif not passport["eyr"].isdigit() or int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030: valid = 0
        elif not passport["hgt"][:-2].isdigit() or (passport["hgt"][-2:] != "cm" and passport["hgt"][-2:] != "in"): valid = 0
        elif passport["hgt"][-2:] == "cm" and (int(passport["hgt"][:-2]) < 150 or int(passport["hgt"][:-2]) > 193): valid = 0
        elif passport["hgt"][-2:] == "in" and (int(passport["hgt"][:-2]) < 59 or int(passport["hgt"][:-2]) > 76): valid = 0
        elif re.search("^#[0-9a-f]{6}$", passport["hcl"]) is None: valid = 0
        elif re.search("^(amb|blu|brn|gry|grn|hzl|oth)$", passport["ecl"]) is None: valid = 0
        elif re.search("^[0-9]{9}$", passport["pid"]) is None: valid = 0
      counter += valid
      passport = {}
      continue
    passport.update({pair.split(':')[0]:pair.split(':')[1] for pair in line.strip().split(" ")})
print(counter)