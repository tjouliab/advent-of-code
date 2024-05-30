import os
import re
import math


def extract_monkey_info(monkey_info: str) -> list:
    infos = monkey_info.split('\n')

    # Extract starting items
    starting_items = [int(num) for num in re.findall(r'\d+', infos[1])]

    # Extract operation
    operation = infos[2][19:]

    # Extract test
    test = re.search(pattern=r'\d+', string=infos[3]).group(0)
    # Extract true throw
    true_throw = re.search(pattern=r'\d+', string=infos[4]).group(0)
    # Extract false throw
    false_throw = re.search(pattern=r'\d+', string=infos[5]).group(0)

    return [starting_items, operation, int(test), int(true_throw), int(false_throw)]


class Monkey():
    def __init__(self, starting_items: list[int], operation: str, test: int, true_throw: int, false_throw: int) -> None:
        self.__starting_items: list[int] = starting_items
        self.__operation: str = operation
        self.__test: int = test
        self.__true_throw: int = true_throw
        self.__false_throw: int = false_throw

        self.__inspected_items = 0

    def __str__(self) -> str:
        return f'\n  Inspected Items: {self.__inspected_items}\n'

    def __repr__(self):
        return self.__str__()

    def number_of_rounds(self) -> int:
        return len(self.__starting_items)

    def round(self, worried: bool, test_product: int) -> list[int]:
        old: int = self.__starting_items[0]
        del self.__starting_items[0]
        self.__inspected_items += 1

        # Eval new value based on old
        new = eval(self.__operation, {'old': old})
        bored = math.floor(new / 3) if not worried else new

        if bored % self.__test == 0:
            return [self.__true_throw, bored % test_product]
        return [self.__false_throw, bored % test_product]

    def add_received_item(self, item) -> None:
        self.__starting_items.append(item)

    def get_inspected_items(self) -> int:
        return self.__inspected_items

    def get_test(self) -> int:
        return self.__test


def calculate_worry_level(file: str, rounds=20, worried=False) -> int:
    with open(file, 'rt') as f:
        monkeys: list[Monkey] = []

        file_content = f.read()
        monkeys_info = file_content.split('\n\n')

        test_product = 1
        for info in monkeys_info:
            monkeys.append(Monkey(*extract_monkey_info(info)))
            test_product *= monkeys[-1].get_test()

        for _ in range(rounds):
            for monkey in monkeys:
                for _ in range(monkey.number_of_rounds()):
                    [index, item] = monkey.round(worried, test_product)
                    monkeys[index].add_received_item(item)
    inspected_items = list(
        map(lambda monkey: monkey.get_inspected_items(), monkeys))
    inspected_items.sort(reverse=True)
    return math.prod(inspected_items[:2])


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = os.path.join(__location__, 'input.txt')

    print(calculate_worry_level(file))
    print(calculate_worry_level(file, rounds=10_000, worried=True))
