

import heapq 

file = open('day1_input.txt', 'r')

elves = []

current_elf = 0

for line in file.readlines():
    if line == '\n':
        heapq.heappush(elves, -current_elf)
        current_elf = 0
    else:
        cals = int(line.rstrip())
        current_elf += cals

first = -1 * heapq.heappop(elves)
second =-1 * heapq.heappop(elves)
third = -1 * heapq.heappop(elves)

print(first + second + third)
