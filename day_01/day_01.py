import copy
import csv


def day_1(path: str):
    with open(path, newline='') as csvfile:
        elves_calories = csv.reader(csvfile)
        elves = []
        current_calories = 0
        for row in elves_calories:
            if len(row) != 0:
                current_calories += int(row[0])
            else:
                elves.append(copy.deepcopy(current_calories))
                current_calories = 0
        elves.append(copy.deepcopy(current_calories))
    elves.sort(reverse=True)
    print(f'The Elf of the month has: {elves[0]}')
    print(f'The sum of the top 3 is: {elves[0] + elves[1] + elves[2]}')

print('Test Day 1')
day_1('day_01/test-data.txt')

print('Day 1')
day_1('day_01/data.txt')