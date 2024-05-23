import array
import os


def move_crates_9000(file):
    with open(file, 'rt') as f:
        piles = [[] for _ in range(9)]
        lines = f.readlines()
        for line in lines:
            if line.startswith('move'):
                from_index = line.index('from')
                to_index = line.index('to')

                count = int(line[5: from_index - 1])
                from_pile = int(line[from_index + 5: to_index - 1]) - 1
                to_pile = int(line[-2]) - 1

                for _ in range(count):
                    piles[to_pile].append(piles[from_pile].pop())

            elif line.startswith('['):
                for i in range(9):
                    item = line[3 * i + i: 3 * (i + 1) + i]
                    if len(item.strip()) == 3:
                        piles[i].insert(0, item[1])

    return ''.join([pile[-1] for pile in piles])


def move_crates_9001(file):
    with open(file, 'rt') as f:
        piles = [[] for _ in range(9)]
        lines = f.readlines()
        for line in lines:
            if line.startswith('move'):
                from_index = line.index('from')
                to_index = line.index('to')

                count = int(line[5: from_index - 1])
                from_pile = int(line[from_index + 5: to_index - 1]) - 1
                to_pile = int(line[-2]) - 1

                piles[to_pile] += piles[from_pile][-count:]
                for _ in range(count):
                    del piles[from_pile][-1]
                
            elif line.startswith('['):
                for i in range(9):
                    item = line[3 * i + i: 3 * (i + 1) + i]
                    if len(item.strip()) == 3:
                        piles[i].insert(0, item[1])

    return ''.join([pile[-1] for pile in piles])


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = os.path.join(__location__, 'input.txt')

    print(move_crates_9000(file))
    print(move_crates_9001(file))
