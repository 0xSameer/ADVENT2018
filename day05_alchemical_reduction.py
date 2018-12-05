"""
ADVENT 2018 - Day 05

https://adventofcode.com/2018/day/5

""" 

import time
import re

def check_polymer(s: str) -> str:
    """
    We use a Stack data structure.
    For each character in the input string,
    we compare against the last seen character. If they react,
    then we "pop" out the last character as well.
    If not, we add the new character into the stack
    """
    stack = []
    """
    for a polar pair of chars:
        a, A
        ord('a')-ord('A') == 32
        ord('A')-ord('a') == -32
        Therefore, we can check for absolute diff
        of 32
    """
    for c in s:
        if (len(stack) > 0) and (abs(ord(stack[-1])-ord(c))==32):
            stack.pop()
        else:
            stack.append(c)
        # end if-else polar pair check
    # end for char in s
    stack = "".join(stack)
    return stack


TEST_INPUT = "dabAcCaCBAcCcaDA"
assert check_polymer(TEST_INPUT) == 'dabCBAcaDA'

if __name__ == "__main__":
    with open("./data/day05_a.txt", "r") as in_f:
        INPUT = in_f.read()

    print("Input string length: {0:d}".format(len(INPUT)))

    """
    Part One
    Complexity: O(N)
    Runtime: 35 ms
    """
    START = time.time()
    remaining_str = check_polymer(INPUT)
    print("Part 1 solution: {0:d}".format(len(remaining_str)))
    print("Total time = {0:f} ms".format((time.time()-START)*1000))

    """
    Part Two
    Remove each character type, and compute remaining string
    length
    We have 26 character types: aA-zZ
    Complexity: 26*O(N) = O(N)
    Runtime:    360 ms
    """
    START = time.time()
    min_len = len(INPUT)
    min_char = ''
    for i in range(ord('a'),ord('z')+1):
        c = chr(i)
        rx = r"[{0:s}{1:s}]+".format(c,c.upper())
        new_str = re.sub(rx, '', INPUT)
        curr_len = len(check_polymer(new_str))
        if curr_len < min_len:
            min_len = curr_len
            min_char = c
    # end for

    print("Part 2 solution")
    print("min len: {0:d}, if char: {1:s} removed".format(min_len, min_char))
    print("Total time = {0:f} ms".format((time.time()-START)*1000))
# end main

