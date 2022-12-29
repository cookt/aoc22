
class ARange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def size(self):
        return self.end - self.start

    def contains(self, other: 'ARange') -> bool:
        return self.start <= other.start and other.end <= self.end

    def overlaps(self, other: 'ARange') -> bool:
        left_side = self.start <= other.end and self.end >= other.start
        return left_side

def parse_assignment_ranges(line:str):
    aranges = line.split(',')
    rangeA = aranges[0]
    pointsA = rangeA.split('-')
    rangeB = aranges[1]
    pointsB = rangeB.split('-')
    return (ARange(int(pointsA[0]), int(pointsA[1])), ARange(int(pointsB[0]), int(pointsB[1])))


file = open('day4_input.txt','r')
## part 1
# containing = 0
# for line in file.readlines():
#     rangeA, rangeB = parse_assignment_ranges(line)
#     if rangeA.size() >= rangeB.size():
#         containing += rangeA.contains(rangeB)
#     else:
#         containing += rangeB.contains(rangeA)

## print(containing)

overlaps = 0
for line in file.readlines():
    rangeA, rangeB = parse_assignment_ranges(line)
    overlaps += rangeA.overlaps(rangeB)
print(overlaps)
