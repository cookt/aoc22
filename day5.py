from typing import List

class CrateBoard:
    def __init__(self):
        self.columns = {}

    def move(self, count: int, src: int, destination: int):
        srcIndex = src - 1
        dstIndex = destination - 1
        for i in range(count):
            item = self.columns[srcIndex].pop()
            self.columns[dstIndex].append(item)

    def move_multiple(self, count: int, src: int, destination: int):
        srcIndex = src - 1
        dstIndex = destination - 1
        n = len(self.columns[srcIndex])
        backSlice = self.columns[srcIndex][n-count:n]
        self.columns[srcIndex] = self.columns[srcIndex][0:n-count]
        self.columns[dstIndex].extend(backSlice)

    def __str__(self) -> str:
        s = ""
        for i in self.columns.keys():
            s+= str(i+1) + ":" + ','.join(self.columns[i]) + "\n"
        return s

    def tops(self) -> str:
        letters = ""
        for i in self.columns.keys():
            n = len(self.columns[i])
            letters += self.columns[i][n - 1]
        return letters


def parse_board(lines:List[str]) -> CrateBoard:
    columns = lines[len(lines) - 1]
    b = CrateBoard()
    for i in range(len(columns)):
        if columns[i].strip() == "":
            continue
        if columns[i].isnumeric():
            colIndex = int(columns[i]) - 1
            for j in range(len(lines) - 2, -1, -1):
                if not colIndex in b.columns:
                    b.columns[colIndex] = []
                if lines[j][i].strip() != "":
                    b.columns[colIndex].append(lines[j][i])
                else:
                    break
    return b

def parse_move(line: str):
    tokens = line.split(' ')
    count = int(tokens[1])
    source = int(tokens[3])
    dest = int(tokens[5])
    return count,source,dest


board_lines = []
board = None
file = open("day5_input.txt", 'r')

for line in file.readlines():
    value = line.rstrip()
    if value.startswith("move"):
        count, src, dst = parse_move(value)
        board.move_multiple(count, src, dst)
    elif value == "":
        board = parse_board(board_lines)
    else:
        board_lines.append(line.rstrip())

print(board.tops())