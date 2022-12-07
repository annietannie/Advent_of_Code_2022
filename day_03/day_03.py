import csv

import itertools
alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = alphabet_lower.upper()
alphabet = alphabet_lower + alphabet_upper


def get_points(pack_1: str, pack_2: str) -> int:
    for item_1, item_2 in itertools.product(pack_1, pack_2):
        if item_1 == item_2:
            return alphabet.index(item_1) + 1


def day_3(path: str):
    with open(path, newline='') as csvfile:
        rucksacks = csv.reader(csvfile)
        points = 0
        for pack in rucksacks:
            pack_str = pack[0]
            pack_1 = pack_str[:len(pack_str) // 2]
            pack_2 = pack_str[len(pack_str) // 2:]
            points += get_points(pack_1, pack_2)
        print(f'Sum of the priorities is {points}')


def get_3_1_points(elf_0: str, elf_1: str, elf_2: str) -> int:
    for char_0, char_1 in itertools.product(elf_0, elf_1):
        if char_0 == char_1:
            for char_2 in elf_2:
                if char_0 == char_2:
                    return alphabet.index(char_0) + 1


def day_3_1(path: str):
    with open(path, newline='') as csvfile:
        rucksacks = list(csv.reader(csvfile))
        points = 0
        for x in range(len(rucksacks)-3):
            elf_0 = rucksacks[x][0]
            elf_1 = rucksacks[x+1][0]
            elf_2 = rucksacks[x+2][0]
            points += get_3_1_points(elf_0, elf_1, elf_2)
            x += 2
        print(f'Sum of the priorities is {points}')


print('Test Day 3.1')
day_3('test-data.txt')

print('Day 3.1')
day_3('data.txt')

print('Test Day 3.2')
day_3_1('test-data.txt')

print('Day 3.2')
day_3_1('data.txt')