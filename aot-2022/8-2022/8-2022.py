import os
import numpy as np


def count_visible_trees(file: str) -> int:
    with open(file, 'rt') as f:
        lines = f.read().split()
        for i, line in enumerate(lines):
            lines[i] = list(map(int, [*line]))

        np_lines = np.array(lines)

        # Count the visible trees on the outside
        height: int = len(lines)
        width: int = len(lines[0])
        counter: int = 2 * (height - 1) + 2 * (width - 1)

        for x in range(1, height - 1):
            for y in range(1, width - 1):
                current_tree = np_lines[x, y]

                left = np_lines[x, :y]
                is_visible_left = current_tree > np.max(left)
                if is_visible_left:
                    counter += 1
                    continue

                right = np_lines[x, y + 1:]
                is_visible_right = current_tree > np.max(right)
                if is_visible_right:
                    counter += 1
                    continue

                up = np_lines[:x, y]
                is_visible_up = current_tree > np.max(up)
                if is_visible_up:
                    counter += 1
                    continue

                down = np_lines[x + 1:, y]
                is_visible_down = current_tree > np.max(down)
                if is_visible_down:
                    counter += 1

    return counter


def get_scenic_score(file: str) -> int:
    with open(file, 'rt') as f:
        lines = f.read().split()
        for i, line in enumerate(lines):
            lines[i] = list(map(int, [*line]))

        np_lines = np.array(lines)

        # Count the visible trees on the outside
        height: int = len(lines)
        width: int = len(lines[0])
        max_scenic_score: int = 0

        for x in range(1, height - 1):
            for y in range(1, width - 1):
                current_tree = np_lines[x, y]

                left = np_lines[x, :y]
                left_score = 0
                for elem in left[::-1]:
                    left_score += 1
                    if elem >= current_tree:
                        break
                    

                right = np_lines[x, y + 1:]
                right_score = 0
                for elem in right:
                    right_score += 1
                    if elem >= current_tree:
                        break

                up = np_lines[:x, y]
                up_score = 0
                for elem in up[::-1]:
                    up_score += 1
                    if elem >= current_tree:
                        break

                down = np_lines[x + 1:, y]
                down_score = 0
                for elem in down:
                    down_score += 1
                    if elem >= current_tree:
                        break
                
                scenic_score = left_score * right_score * up_score * down_score
                max_scenic_score = max(max_scenic_score, scenic_score)

    return max_scenic_score


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = os.path.join(__location__, 'input.txt')

    print(count_visible_trees(file))
    print(get_scenic_score(file))
