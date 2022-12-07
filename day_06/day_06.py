import csv
from typing import List


def check_if_unique_characters(sample: [str]) -> bool:
    for x in range(len(sample)-1):
        for y in range(x+1,len(sample)):
            if sample[x] == sample[y]:
                return False
    return True


def day_6(path: str, number: int):
    with open(path, newline='') as csvfile:
        line = list(csv.reader(csvfile))[0]
        code = [*line[0]]
        sample = [code[x] for x in range(number-1)]
        for x in range(number-1, len(code)):
            sample.append(code[x])
            if check_if_unique_characters(sample):
                print(f'First marker found after character {x+1}')
                break
            else:
                sample.pop(0)

print('Test Day 6.1')
day_6('test-data.txt', 4)

print('Day 6.1')
day_6('data.txt', 4)

print('Test Day 6.2')
day_6('test-data.txt', 14)

print('Day 6.2')
day_6('data.txt', 14)