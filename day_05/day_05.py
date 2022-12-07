import csv


def day_5(path: str):
    with open(path, newline='') as csvfile:
        instructions = list(csv.reader(csvfile))
        number_of_crates = int(next((instruction[0][len(instruction[0]) - 1] for instruction in instructions if ' 1' in instruction[0]), 0))
        crates = [[] for _ in range(number_of_crates)]

        for line in instructions:
            if len(line) > 0:
                inst = line[0]
                if inst[0] in [' ', '['] and inst[1] != '1':
                    for crate_line, x in enumerate(range(0, len(inst), 4)):
                        if inst[x + 1] != ' ':
                            crate = inst[x+1]
                            crates[crate_line].append(crate)

                if 'move' in inst:
                    instruction = inst.split()
                    for _ in range(int(instruction[1])):
                        moving_crate = crates[int(instruction[3])-1][0]
                        crates[int(instruction[3])-1].pop(0)
                        crates[int(instruction[5])-1].insert(0, moving_crate)
        crates_on_top = [crate_line[0] for crate_line in crates]
        print(f'The crates on top are {crates_on_top}')

def day_5_2(path: str):
    with open(path, newline='') as csvfile:
        instructions = list(csv.reader(csvfile))
        number_of_crates = int(next((instruction[0][len(instruction[0]) - 1] for instruction in instructions if ' 1' in instruction[0]), 0))
        crates = [[] for _ in range(number_of_crates)]

        for line in instructions:
            if len(line) > 0:
                inst = line[0]
                if inst[0] in [' ', '['] and inst[1] != '1':
                    for crate_line, x in enumerate(range(0, len(inst), 4)):
                        if inst[x + 1] != ' ':
                            crate = inst[x+1]
                            crates[crate_line].append(crate)

                if 'move' in inst:
                    instruction = inst.split()
                    moving_crates = []
                    for _ in range(int(instruction[1])):
                        moving_crates.append(crates[int(instruction[3]) - 1][0])
                        crates[int(instruction[3]) - 1].pop(0)
                    for x in reversed(range(len(moving_crates))):
                        crates[int(instruction[5]) - 1].insert(0, moving_crates[x])
        crates_on_top = [crate_line[0] for crate_line in crates]
        print(f'The crates on top are {crates_on_top}')

print('Test Day 5')
day_5('test-data.txt')

print('Day 5')
day_5('data.txt')

print('Test Day 5.2')
day_5_2('test-data.txt')

print('Day 5.2')
day_5_2('data.txt')