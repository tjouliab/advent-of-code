import os


def count_markers(file: str, distinct: int) -> int:
    with open(file, 'rt') as f:

        count = 0
        last_letters = []
        char = f.read(1)
        while char != '' and len(set(last_letters)) < distinct:
            count += 1
            last_letters.append(char)
            if len(last_letters) > distinct:
                del last_letters[0]
                
            char = f.read(1)
    return count


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = os.path.join(__location__, 'input.txt')

    print(count_markers(file, 4))
    print(count_markers(file, 14))
