"""
ADVENT 2018 - Day 11

https://adventofcode.com/2018/day/10

"""
from typing import List, Tuple
import time
import math
from tqdm import tqdm

import numpy as np

def calc_power(x: int, y: int, grid_sn: int) -> int:
    rack = x+10
    power = ((rack * y) + grid_sn) * rack
    power = (power // 100) % 10
    power -= 5
    return power


print(calc_power(122,79,57) == -5)
print(calc_power(217,196,39) == 0)
print(calc_power(101,153,71) == 4)


def make_grid(size: int, grid_sn: int) -> np.ndarray:
    grid = np.zeros((size,size), dtype=np.int32)

    for x in range(size):
        for y in range(size):
            grid[y,x] = calc_power(x+1, y+1, grid_sn)
    # end for

    return grid

def max_square_power(grid: np.ndarray) -> Tuple[int,int]:
    size = len(grid)
    max_power = -math.inf
    max_x = 0
    max_y = 0
    for x in range(0, size):
        for y in range(0, size):
            square_power = np.sum(grid[y:y+3, x:x+3])
            if square_power > max_power:
                max_power = square_power
                max_x = x
                max_y = y
            # end if
        # end for y
    # end for x
    return (max_x+1,max_y+1, max_power)


def max_square_power_size(grid: np.ndarray):
    size = len(grid)
    max_power = -math.inf
    max_x = 0
    max_y = 0
    max_s = 0
    for x in tqdm(range(0, size), ncols=80):
        for y in range(0, size):
            square_power = grid[y,x]
            max_size = size-max(x,y)
            for s in range(1,max_size):
                """
                x,y = 1,1
                grid size 1: sum(y,x)
                grid size 2: g(y,x) + g(y+1,x), g(y+1,x+1), g(y, x+1)

                grid size 2: g()
                """
                square_power += np.sum(grid[y:y+s+1,x+s])
                square_power += np.sum(grid[y+s,x:x+s+1])
                square_power -= grid[y+s,x+s]
                if square_power > max_power:
                    max_power = square_power
                    max_x = x
                    max_y = y
                    max_s = s
            # end if
        # end for y
    # end for x
    return (max_x+1,max_y+1, max_power, max_s+1)



grid = make_grid(300, 18)
assert (max_square_power(grid) == (33,45,29))
grid = make_grid(300, 42)
assert (max_square_power(grid) == (21,61,30))
grid = make_grid(300, 18)
# print(max_square_power(grid))
# print(max_square_power_size(grid))


"""
Part One
500ms
"""
START = time.time()
grid = make_grid(300, 7857)
print(max_square_power(grid))
print("Total time = {0:f} ms".format((time.time()-START)*1000))

"""
Part Two
72 seconds
"""
START = time.time()
grid = make_grid(300, 7857)
print(max_square_power_size(grid))
print("Total time = {0:f} ms".format((time.time()-START)*1000))
