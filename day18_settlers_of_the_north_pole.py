"""
ADVENT 2018 - Day 18

https://adventofcode.com/2018/day/18

"""

from enum import Enum
import time

class State(Enum):
    TREE = "|"
    OPEN = "."
    LUMBER = "#"


TEST_STATE = """.#.#...|#.
                .....#|##|
                .|..|...#.
                ..|#.....#
                #.#|||#|#|
                ...#.||...
                .|....|...
                ||...#|.#|
                |.||||..|.
                ...#.|..|."""

def get_neighbors(x,y, grid):
    counts = {".":0, "|": 0, "#": 0, "-": 0}
    for i in [x-1,x,x+1]:
        for j in [y-1,y+1]:
            counts[grid[i][j]] += 1
    for i in [x-1, x+1]:
        counts[grid[i][y]] += 1
    return counts

def step(state):
    N = len(state)
    new_grid = [list(line) for line in state]
    for x in range(1,N-1):
        for y in range(1,N-1):
            counts = get_neighbors(x,y, state)
            if state[x][y] == "." and counts["|"] >= 3:
                new_grid[x][y] = "|"
            elif state[x][y] == "|" and counts["#"] >= 3:
                new_grid[x][y] = "#"
            elif state[x][y] == "#" and (counts["|"] == 0 or counts["#"] == 0):
                new_grid[x][y] = "."
        # end for y
    # end for x
    new_grid = ["".join(line) for line in new_grid]
    return new_grid

def read_initial_state(state_str: str):
    grid = []
    for line in state_str.split("\n"):
        row = []
        for c in line.strip():
            row.append(c)
        grid.append("".join(row))
    return grid

test_grid = ["-" + line.strip() + "-" for line in TEST_STATE.split("\n")]
test_grid = ["-" * (len(test_grid)+2)] + test_grid + ["-" * (len(test_grid)+2)]

with open("./data/day18.txt", "r") as in_f:
    INPUT = in_f.read()

part1_grid = ["-" + line.strip() + "-" for line in INPUT.split("\n")]
part1_grid = ["-" * (len(part1_grid)+2)] + part1_grid + ["-" * (len(part1_grid)+2)]

part2_grid = part1_grid[:]

for i in range(10):
    test_grid = step(test_grid)
    print("\n".join(test_grid))

test_grid = "\n".join(test_grid)
print(test_grid.count("|") * test_grid.count("#"))

"""
Part 1 Total time: 75 ms
"""
START = time.time()
for i in range(10):
    part1_grid = step(part1_grid)
    print("\n".join(part1_grid))

part1_grid = "\n".join(part1_grid)
print(part1_grid.count("|") * part1_grid.count("#"))
print("Total time = {0:f} ms".format((time.time()-START)*1000))

"""
Part 2
"""
prev_count = 0
START = time.time()
for i in range(1,1001):
    part2_grid = step(part2_grid)
    # print("\n".join(part2_grid))
    part2_str = "\n".join(part2_grid)
    curr_count = part2_str.count("|") * part2_str.count("#")
    print(i, curr_count, curr_count - prev_count)
    prev_count = curr_count
print("Total time = {0:f} ms".format((time.time()-START)*1000))

"""
After 412, the value 196310 occurs every 28 steps.
(1000000000 - 412) is divisible by 28, and therefore, the answer is 196310.

"""

