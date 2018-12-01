"""
ADVENT 2018 - Day 01

https://adventofcode.com/2018/day/1

"""

import itertools
from typing import List

def apply_changes(freq_deltas: List[int]) -> int:
    freq = sum(freq_deltas)
    return freq

def find_repeat(freq_deltas: List[int]) -> int:
    curr = 0
    freqs = set([0])
    N = len(freq_deltas)
    if N == 0:
        return 0
    
    running_sum = 0
    found = False
    while not found:
        running_sum += freq_deltas[curr]
        if running_sum in freqs:
            return running_sum
        freqs.add(running_sum)
        curr += 1
        curr = curr % N
        # end if
    # end continue sum

TEST_INPUT = [+1, -2, +3, +1]

assert apply_changes(TEST_INPUT) == 3

assert find_repeat([+1, -2, +3, +1]) == 2
assert find_repeat([+1, -1]) == 0
assert find_repeat([+3, +3, +4, -2, -4]) == 10
assert find_repeat([-6, +3, +8, +5, -6]) == 5
assert find_repeat([+7, +7, -2, -7, -4]) == 14


if __name__ == "__main__":
    INPUT = []
    with open("./data/day01_a.txt", "r") as in_f:
        INPUT = [int(line.strip()) for line in in_f]
        print(INPUT[:5])
        print(apply_changes(INPUT))
        print(find_repeat(INPUT))
