import copy
import csv

points_chart = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

equal = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

wins_from = {
    "X": "Z",
    "Y": "X",
    "Z": "Y"
}

loses_from = {
    "X": "Y",
    "Y": "Z",
    "Z": "X"
}


def calculate_points(opponent: str, you: str) -> int:
    if wins_from[you] == equal[opponent]:
        return 6
    elif you == equal[opponent]:
        return 3
    return 0


def set_part_2_move(opponent: str, instruction: str) -> int:
    if instruction == 'X':
        return points_chart[wins_from[equal[opponent]]] + 0
    elif instruction == 'Y':
        return points_chart[equal[opponent]] + 3
    elif instruction == 'Z':
        return points_chart[loses_from[equal[opponent]]] + 6


def day_2(path: str):
    with open(path, newline='') as csvfile:
        rps = csv.reader(csvfile, delimiter=" ")
        points = 0
        points_2 = 0
        for row in rps:
            # part 1
            points += points_chart[row[1]] + calculate_points(opponent=row[0], you=row[1])
            points_2 += set_part_2_move(opponent=row[0], instruction=row[1])

    print(f'You received {points} points for round 1')
    print(f'You received {points_2} points for round 2')


print('Test Day 2')
day_2('day_02/test-data.txt')

print('Day 2')
day_2('day_02/data.txt')