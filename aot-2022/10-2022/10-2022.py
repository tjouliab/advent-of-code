import os
import numpy as np


def convert_to_image(x):
    return '.' if x == 0 else '*'

class Cycle():
    def __init__(self, signal_strengths: list = []):
        self.__X: int = 1
        self.__loop: int = 0
        self.__strength: int = 0
        self.__signal_strengths: list = signal_strengths

        self.__width = 40
        self.__height = 6
        self.__CRT = np.zeros((self.__height, self.__width), dtype=int)

    def noop(self):
        if self.__loop % self.__width in [i + self.__X for i in range(-1, 2)]:
            self.__CRT[self.__loop // self.__width][self.__loop %
                                                    self.__width] = 1
    
        self.__loop += 1
        if self.__loop in self.__signal_strengths:
            self.__add_strength(self.__X, self.__loop)

    def addx(self, V):
        self.noop()
        self.noop()
        self.__X += V

    def get_strength(self) -> int:
        return self.__strength

    def print_CRT(self):
        CRT_image = np.vectorize(convert_to_image)(self.__CRT)
        for row in CRT_image:
            print(''.join(row))

    def __add_strength(self, X, loop):
        self.__strength += X * loop


def get_signal_strength(file: str) -> int:
    with open(file, 'rt') as f:
        cycle = Cycle([20, 60, 100, 140, 180, 220])

        lines = f.readlines()
        for line in lines:
            if line.startswith('noop'):
                cycle.noop()
            else:
                [_, value] = line.split()
                cycle.addx(int(value))
    return cycle.get_strength()


def get_CRT_image(file: str) -> int:
    with open(file, 'rt') as f:
        cycle = Cycle()

        lines = f.readlines()
        for line in lines:
            if line.startswith('noop'):
                cycle.noop()
            else:
                [_, value] = line.split()
                cycle.addx(int(value))

    cycle.print_CRT()


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = os.path.join(__location__, 'input.txt')

    print(get_signal_strength(file))
    print(get_CRT_image(file))
