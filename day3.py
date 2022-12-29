
from typing import List


value = 1
priority_map = dict()
for i in range(ord('a'), ord('z')+1):
    priority_map[chr(i)] = value
    value += 1

for i in range(ord('A'), ord('Z')+1):
    priority_map[chr(i)] = value
    value += 1

print(priority_map)

file = open("day3_input.txt", 'r')
total = 0


def find_duplicate_letter(letters:List[str]):
    first_elf = letters[0]
    first_comp = {}
    second_elf = letters[1]
    second_comp = {}
    third_elf = letters[2]
    for letter in first_elf:
        if not(letter in first_comp):
            first_comp[letter] = True
    for letter in second_elf:
        if not(letter in second_comp):
            second_comp[letter] = True
    for letter in third_elf:
        if letter in first_comp and letter in second_comp:
            return letter
    return None

## part 1
# for line in file.readlines():
#     n = len(line.rstrip())
#     first_comp = {}
#     for i in range(0, n//2):
#         first_comp[line[i]] = priority_map[line[i]]
#     second_comp = {}
#     for i in range(n//2, n):
#         letter = line[i]
#         if letter in first_comp.keys() and not(letter in second_comp):
#             print(letter, priority_map[letter])
#             total += priority_map[letter]
#         second_comp[letter] = priority_map[letter]

counter = 0
groups = []

for line in file.readlines():
    if counter > 0 and counter % 3 == 0:
        print(groups)
        total += priority_map[find_duplicate_letter(groups)]
        groups = []
    groups.append(line.rstrip())
    counter += 1
total += priority_map[find_duplicate_letter(groups)]
print(total)