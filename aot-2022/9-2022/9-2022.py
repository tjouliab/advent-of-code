import os
import numpy as np


def calculate_grid_height_width(lines):
    current_height = 0
    min_height = 0
    max_height = 0

    current_width = 0
    min_width = 0
    max_width = 0

    for line in lines:
        [direction, value] = line
        match direction:
            case 'U':
                current_height -= int(value)
            case 'D':
                current_height += int(value)
            case 'R':
                current_width += int(value)
            case 'L':
                current_width -= int(value)

        min_height = min(min_height, current_height)
        max_height = max(max_height, current_height)

        min_width = min(min_width, current_width)
        max_width = max(max_width, current_width)

    grid_height = max_height - min_height + 1
    grid_width = max_width - min_width + 1
    starting_height = - min_height
    starting_width = - min_width
    
    return [grid_height, grid_width, starting_height, starting_width]


def count_visited_positions(file: str, tail_length: int = 1) -> int:
    with open(file, 'rt') as f:
        lines = f.read().split('\n')

        lines_formatted = list(map(lambda line: line.split(), lines))
        np_lines = np.array(lines_formatted)
        
        # Init grid and starting point
        [
            grid_height,
            grid_width,
            start_height,
            start_width
        ] = calculate_grid_height_width(np_lines)

        grid = np.zeros((grid_width, grid_height))
        grid[start_width, start_height] = 1

        rope = [[start_width, start_height] for _ in range(tail_length + 1)]

        for line in np_lines:
            [direction, value] = line
            for _ in range(int(value)):
                # Update rope's head
                match direction:
                    case 'U':
                        rope[0][1] -= 1
                    case 'D':
                        rope[0][1] += 1
                    case 'R':
                        rope[0][0] += 1
                    case 'L':
                        rope[0][0] -= 1
            
                for index in range(1, tail_length + 1):
                    # Tail Head vector
                    vector = [
                        rope[index - 1][0] - rope[index][0],
                        rope[index - 1][1] - rope[index][1],
                    ]
                    
                    if abs(vector[0]) <= 1 and abs(vector[1]) <= 1:
                        continue
                    if vector[0] != 0:
                        rope[index][0] += -1 if vector[0] <= -1 else 1
                    if vector[1] != 0:
                        rope[index][1] += -1 if vector[1] <= -1 else 1
                        
                grid[rope[-1][0], rope[-1][1]] = 1

    return int(np.sum(grid))


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

    print(count_visited_positions(file))
    print(count_visited_positions(file, 9))
