import os
import numpy as np
from collections import deque


def Breadth_First_Search(grid, start, end):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)

    while len(queue) > 0:
        (x, y), steps = queue.popleft()

        if (x, y) == end:
            return steps

        current_elevation = ord(grid[x][y])

        for (dx, dy) in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                next_elevation = ord(grid[nx][ny])
                if (nx, ny) not in visited and next_elevation <= current_elevation + 1:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), steps + 1))
    return -1


def find_shortest_path(file: str, start=['S']) -> int:
    with open(file, 'rt') as f:
        lines = f.read().split('\n')
        puzzle = []
        for line in lines:
            puzzle.append([*line])

        np_puzzle = np.array(puzzle)
        found_start = np.where(np.isin(np_puzzle, start))
        start_positions = list(zip(found_start[0], found_start[1]))
        
        E_position = np.where(np_puzzle == 'E')
        end_position = (E_position[0][0], E_position[1][0])
        
        bfs_steps = []
        for pos in start_positions:
            np_puzzle[pos] = 'a'
            steps = Breadth_First_Search(np_puzzle, pos, end_position)
            if steps >= 0:
                bfs_steps.append(steps)
        
    #     np_puzzle[start_position] = 'a'
    #     np_puzzle[end_position] = 'z'
    return min(bfs_steps)


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

    print(find_shortest_path(file))
    print(find_shortest_path(file, start=['a', 'S']))
