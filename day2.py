rock = ['A', 'X']
paper = ['B', 'Y']
scissors = ['C', 'Z']

def determine_move(their_move: str, outcome: str):
    if outcome == 'X':
        if their_move in rock:
            return 'C'
        if their_move in paper:
            return 'A'
        if their_move in scissors:
            return 'B'
    if outcome == 'Y':
        return their_move
    if outcome == 'Z':
        if their_move in rock:
            return 'B'
        if their_move in paper:
            return 'C'
        if their_move in scissors:
            return 'A'



def shape_score(shape: str):
    if shape in rock:
        return 1
    if shape in paper:
        return 2
    if shape in scissors:
        return 3
    return 0

def is_draw(your_move:str, opp_move:str):
    rock_draw = your_move in rock and opp_move in rock
    paper_draw = your_move in paper and opp_move in paper
    scissors_draw = your_move in scissors and opp_move in scissors
    return rock_draw or paper_draw or scissors_draw

def beats(your_move: str, opp_move:str):
    rock_win = your_move in rock and opp_move in scissors
    paper_win = your_move in paper and opp_move in rock
    scissors_win = your_move in scissors and opp_move in paper
    return rock_win or paper_win or scissors_win


def round_outcome(your_move: str, opp_move: str):
    if is_draw(your_move, opp_move):
        return 3
    win = beats(your_move, opp_move)
    if win:
        return 6
    else:
        return 0

total = 0

file = open("day2_input.txt", 'r')

for line in file.readlines():
    moves = line.split(" ")
    their_move = moves[0]
    your_move = moves[1].rstrip()
    outcome = moves[1].rstrip()
    your_move = determine_move(their_move, outcome)
    round_score = round_outcome(your_move, their_move) + shape_score(your_move)
    total += round_score

print(total)