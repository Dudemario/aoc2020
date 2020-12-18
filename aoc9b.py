queue, total, target = [], 0, 776203571
with open("aoc9.txt") as fin:
  for line in fin:
    end = int(line.strip())
    queue.append(end)
    total += end
    while total > target:
      total -= queue[0]
      queue = queue[1:]
    if total == target:
      print(queue,end=" ")
      print(min(queue) + max(queue))
