import csv


class Directory:
    def __init__(self, name: str, parent: 'Directory'):
        self.name = name
        self.parent = parent
        self.sub_dir = []
        self.total_size = 0

    def __str__(self):
        return self.name

    def add_sub_dir(self, sub_dir_object: 'Directory'):
        self.sub_dir.append(sub_dir_object)

    def add_file(self, size: int):
        self.total_size += size

    def get_sub_dir(self, sub_dir_name: str):
        for dir in self.sub_dir:
            if dir.name == sub_dir_name:
                return dir

    def get_parent(self):
        return self.parent

    def calculate_total_size(self):
        for dir in self.sub_dir:
            self.total_size += dir.calculate_total_size()
        return self.total_size

    def get_points_under_10000(self, total: int):
        for dir in self.sub_dir:
            total += dir.get_points_under_10000(total=0)
        if self.total_size < 100000:
            total += self.total_size
        return total

    def get_list_of_sizes(self, sizes: [], min: int):
        if self.total_size >= min:
            sizes.append(self.total_size)
        for dir in self.sub_dir:
            sizes += dir.get_list_of_sizes(sizes=[], min=min)
        return sizes


def day_7(path: str):
    with open(path, newline='') as csvfile:
        filesystem = csv.reader(csvfile)
        root_folder = Directory(name='/', parent=None)
        current_dir = root_folder
        for line in filesystem:
            instr = line[0]
            if 'dir' in instr:
                new_dir_name = instr.split()[1]
                new_dir = Directory(name=new_dir_name, parent=current_dir)
                current_dir.add_sub_dir(new_dir)
            elif '$ cd' in instr:
                if '/' not in instr:
                    new_dir_name = instr.split()[2]
                    if new_dir_name == '..':
                        current_dir = current_dir.get_parent()
                    else:
                        current_dir = current_dir.get_sub_dir(sub_dir_name=new_dir_name)
            elif '$ ls' not in instr:
                file_size = int(instr.split()[0])
                current_dir.add_file(size=file_size)
    root_folder.calculate_total_size()
    total_size = root_folder.get_points_under_10000(total=0)
    print(f'Total size of directories under 100000 is {total_size}')
    required_size = 30000000 - (70000000 - root_folder.total_size)
    sizes = root_folder.get_list_of_sizes(sizes=[], min=required_size)
    sizes.sort()
    print(f'Minimal size of the directory to remove is {sizes[0]}')


print('Test Day 7.1')
day_7('test-data.txt')

print('Day 7.1')
day_7('data.txt')
