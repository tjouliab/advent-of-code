import os


def count_fully_contains(file) -> int:
    with open(file, 'rt') as f:
        counter = 0

        lines = f.readlines()
        for line in lines:
            [assignment1, assignment2] = line.split(',')
            [min1, max1] = assignment1.split('-')
            [min2, max2] = assignment2.split('-')
        
            if int(min2) <= int(min1) and int(max1) <= int(max2):
                counter += 1
            elif int(min1) <= int(min2) and int(max2) <= int(max1):
                counter += 1
    return counter


def count_overlaps(file):
    with open(file, 'rt') as f:
        counter = 0

        lines = f.readlines()
        for line in lines:
            [assignment1, assignment2] = line.split(',')
            [min1, max1] = assignment1.split('-')
            [min2, max2] = assignment2.split('-')

            if int(min1) <= int(max2) and int(min2) <= int(max1):
                counter += 1

    return counter

if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = os.path.join(__location__, 'input.txt')

    print(count_fully_contains(file))
    print(count_overlaps(file))
