"""
ADVENT 2018 - Day 06

https://adventofcode.com/2018/day/6

"""

import time
from typing import List, Tuple
import numpy as np
import operator

def initialize_grid(coords: List[Tuple[int,int]]) -> np.array:
    """
    find the maximum x, y coordinate points to 
    initialize the grid
    x: column
    y = row
    """
    max_row = max(coords, key=operator.itemgetter(1))[1]
    max_col = max(coords, key=operator.itemgetter(0))[0]
    
    grid = np.full((max_row+1, max_col+1), -1, dtype=np.int32)
    
    # NOTE: coords are x,y, which equals col, row
    for i, (c,r) in enumerate(coords):
        grid[r,c] = i

    return grid


def find_nearest(coords: List[Tuple[int,int]]) -> np.array:
    grid = initialize_grid(coords)
    # for each point in grid, find nearest neighbor
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            # compute manhattan distance from each coord
            dist = [abs(r-rp)+abs(c-cp) for cp, rp in coords]
            # find minimum distance
            min_dist = min(dist)
            # if unique value found, then assign
            # cell to coord
            if dist.count(min_dist) == 1:
                grid[r,c] = np.argmin(dist)
            # end if
        # end for cols
    # end for rows
    return grid
# end function

def find_largest_area(coords: List[Tuple[int,int]]) -> np.array:
    # Get the neighbor mapping for each coord
    grid = find_nearest(coords)
    """
    Find infinite coords:
    Any coordinate with a cell on the corner rows,cols will be infinite
    """
    # Dictionary to store size of each coordinate
    # If -1, coordinate is infinite
    coord_area = {}
    # check first and last rows
    infinite = set([c for c in grid[0,:]])
    infinite.update([c for c in grid[-1,:]])
    # check first and last columns
    infinite.update([c for c in grid[:,0]])
    infinite.update([c for c in grid[:,-1]])
    # set infinite coord area to -1
    for c in infinite:
        coord_area[c] = -1
    
    # add -1 to infinite
    infinite.add(-1)

    # for remaining coordinates, check area:
    for r in range(1,grid.shape[0]):
        for c in range(1,grid.shape[1]):
            cell = grid[r,c]
            if cell not in infinite:
                if cell not in coord_area:
                    coord_area[cell] = 1
                else:
                    coord_area[cell] += 1
            # end if else bounded coord
        # end for all cols
    # end for all rows
    max_area = max(coord_area.items(), key=operator.itemgetter(1))
    # print(coord_area)
    # print(max_area, coords[max_area[0]])
    return max_area[1]
# end find_largest_area


def find_safe_area(coords: List[Tuple[int,int]], 
                        MAX_VAL: int) -> np.array:
    grid = initialize_grid(coords)
    # for each point in grid, find nearest neighbor
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            # compute manhattan distance from each coord
            dist = [abs(r-rp)+abs(c-cp) for cp, rp in coords]
            # find minimum distance
            total_dist = sum(dist)
            # if unique value found, then assign
            # cell to coord
            if total_dist < MAX_VAL:
                grid[r,c] = 1
            else:
                grid[r,c] = -1
            # end if
        # end for cols
    # end for rows
    # Set all infinite coords to -1
    grid[0,:] = -1
    grid[-1,:] = -1
    grid[:,0] = -1
    grid[1,0] = -1
    return len(grid[grid == 1])
# end find_safe_area

TEST_INPUT = [(1, 1),
              (1, 6),
              (8, 3),
              (3, 4),
              (5, 5),
              (8, 9)]

assert (find_largest_area(TEST_INPUT) == 17)

assert (find_safe_area(TEST_INPUT, 32) == 16)

if __name__ == "__main__":
    with open("./data/day06_a.txt", "r") as in_f:
        INPUT = [tuple([int(i) for i in line.strip().split(', ')]) 
                               for line in in_f]
    """
    Part One
    Complexity: O(K)
    where K = grid size R * C
    Runtime: 2.5 secs
    """
    START = time.time()
    max_area = find_largest_area(INPUT)
    print("Part 1 solution: {0:d}".format(max_area))
    print("Total time = {0:f} ms".format((time.time()-START)*1000))
    """
    Part Two
    Complexity: O(K)
    where K = grid size R * C
    Runtime: 1.2 secs
    """
    START = time.time()
    safe_area = find_safe_area(INPUT, 10000)
    print("Part 2 solution: {0:d}".format(safe_area))
    print("Total time = {0:f} ms".format((time.time()-START)*1000))
# end main