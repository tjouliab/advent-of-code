import os
import sys


def access_directory(directory: dict, path: list, dir: str) -> None:
    if len(path) == 0:
        if dir not in directory:
            directory[dir] = {'size': 0, 'next': {}}
    else:
        route = path[0]
        if route not in directory:
            directory[route] = {'size': 0, 'next': {}}
        access_directory(directory[route]['next'], path[1:], dir)


def add_directory_element(directory: dict, path: list, size: int, file: str) -> None:
    if len(path) == 0:
        directory[file] = size
    else:
        route = path[0]
        directory[route]['size'] += size
        add_directory_element(directory[route]['next'], path[1:], size, file)


def recursive_directory_size(directory: dict, threshold: int) -> int:
    size = 0
    for key in directory.keys():
        dir = directory[key]
        if isinstance(dir, int):
            continue
        else:
            size += recursive_directory_size(dir['next'], threshold)
            val = int(dir['size'])
            if val <= threshold:
                size += val
    return size


def recursive_smallest_directory(directory: dict, size_to_delete: int) -> int:
    smallest_size = sys.maxsize
    for key in directory.keys():
        dir = directory[key]
        if isinstance(dir, int):
            continue
        else:
            size = recursive_smallest_directory(dir['next'], size_to_delete)
            val = int(dir['size'])
            if val < size_to_delete:
                smallest_size = min(smallest_size, size)
            else:
                smallest_size = min(smallest_size, size, val)
    return smallest_size


def read_dir_from_file(file: str) -> dict:
    current_path = []
    directory = {}
    with open(file, 'rt') as f:

        lines = f.readlines()
        for line in lines:
            if line.startswith('$ ls'):
                continue
            elif line.startswith('$ cd'):
                path = line[4:].strip()
                if (path == '..'):
                    current_path.pop()
                else:
                    access_directory(directory, current_path, path)
                    current_path.append(path)
            elif line.startswith('dir'):
                dir = line[3:].strip()
                access_directory(directory, current_path, dir)
            else:
                [size, file_name] = line.split()
                add_directory_element(
                    directory, current_path, int(size), file_name)
    return directory


def count_dir_size(file: str) -> int:
    threshold = 100_000
    directory = read_dir_from_file(file)

    return recursive_directory_size(directory, threshold)


def delete_smallest_dir(file: str, system_size=70_000_000, threshold=30_000_000) -> int:
    directory = read_dir_from_file(file)
    directory_size: int = directory['/']['size']
    size_to_delete: int = threshold + directory_size - system_size

    return recursive_smallest_directory(directory, size_to_delete)


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = os.path.join(__location__, 'input.txt')

    print(count_dir_size(file))
    print(delete_smallest_dir(file))
