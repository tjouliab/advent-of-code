import os


def func_part1(file: str) -> int:
    with open(file, 'rt') as f:
        lines = f.readlines()
        for line in lines:
            pass
    return


def func_part2(file: str) -> int:
    with open(file, 'rt') as f:
        char = f.read(1)
        while char != '':
            char = f.read(1)

    return


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = os.path.join(__location__, 'input.txt')

    print(func_part1(file))
    print(func_part2(file))
