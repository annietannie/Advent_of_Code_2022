import csv


def day_4(path: str):
    with open(path, newline='') as csvfile:
        pairs = csv.reader(csvfile)
        counter_1 = 0
        counter_2 = 0
        for pair in pairs:
            elf_1 = [int(pair[0].split("-")[0])]
            elf_1.append(int(pair[0].split("-")[1]))
            elf_2 = [int(pair[1].split("-")[0])]
            elf_2.append(int(pair[1].split("-")[1]))
            # part 1
            if (elf_1[0] <= elf_2[0] and elf_1[1] >= elf_2[1]) or (elf_1[0] >= elf_2[0] and elf_1[1] <= elf_2[1]):
                counter_1 += 1
                counter_2 += 1
            # part 2
            elif (elf_1[1] <= elf_2[1] and elf_1[1] >= elf_2[0]) or (elf_2[1] <= elf_1[1] and elf_2[1] >= elf_1[0]):
                counter_2 += 1
        print(f'The number of double cleaners is {counter_1}')
        print(f'The number of overlapping pairs is {counter_2}')


# def day_4_2(path: str):
#     with open(path, newline='') as csvfile:
#         pairs = csv.reader(csvfile)


print('Test Day 4.1')
day_4('test-data.txt')

print('Day 4')
day_4('data.txt')

# print('Day 4.2')
# day_4_2('test-data.txt')