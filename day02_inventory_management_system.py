"""
ADVENT 2018 - Day 02

https://adventofcode.com/2018/day/2

"""

from typing import Tuple
import time

def check_id(s: str) -> Tuple[int, int]:
    counts = {}
    for c in s:
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1
        # end if-else
    # end for
    twos, threes = 0, 0
    for c in counts:
        if counts[c] == 2:
            twos = 1
        elif counts[c] == 3:
            threes = 1
        # end if-else
    # end for
    return (twos, threes)

def check_id_pair(id1: str, id2: str) -> bool:
    if len(id1) != len(id2):
        return False
    # check character by character
    n_errors = 0
    for c1, c2 in zip(id1,id2):
        if c1 != c2:
            n_errors += 1
    
    if n_errors == 1:
        return True
    else:
        return False

# Part (a) test cases
assert check_id("abcdef") == (0,0)
assert check_id("bababc") == (1,1)
assert check_id("abbcde") == (1,0)
assert check_id("abcccd") == (0,1)
assert check_id("aabcdd") == (1,0)
assert check_id("abcdee") == (1,0)
assert check_id("ababab") == (0,1)

# Part (b) test cases
assert check_id_pair("abcde", "axcye") == False
assert check_id_pair("fghij", "fguij") == True
assert check_id_pair("abcde", "wvxyz") == False
assert check_id_pair("abcde", "abcde") == False

if __name__ == "__main__":
    # Read test data
    with open("./data/day02_a.txt", "r") as in_f:
        INPUT = [line.strip() for line in in_f]

    # Part (a)
    twos, threes = 0, 0
    # compute checksum for each test string
    for s in INPUT:
        two, three = check_id(s)
        twos += two
        threes += three
    # end for
    checksum = twos*threes
    print(checksum)

    """
    Part (b)
    Method 1: O (N^2)
    Time: ~90ms
    """
    start = time.time()
    N = len(INPUT)
    for i in range(N-1):
        for j in range(i+1,N):
            s1, s2 = INPUT[i], INPUT[j]
            if check_id_pair(s1, s2) == True:
                common_letters = ""
                for c1, c2 in zip(s1,s2):
                    if c1 == c2:
                        common_letters += c1
                    # end if
                # end for
                print("Found! s1: {0:s}, s2: {1:s}, common: {2:s}".format(s1, s2, common_letters))
                break
            # end if
        # end for j
    # end for i
    print("Total time = {0:f} ms".format((time.time()-start)*1000))
    
    """
    Part (b)
    Method 2: O (N log N)
    Time: ~0.5 ms
    """
    start = time.time()
    INPUT.sort()
    for s1, s2 in zip(INPUT, INPUT[1:]):
        if check_id_pair(s1, s2) == True:
            common_letters = ""
            for c1, c2 in zip(s1,s2):
                if c1 == c2:
                    common_letters += c1
                # end if
            # end for
            print("Found! s1: {0:s}, s2: {1:s}, common: {2:s}".format(s1, s2, common_letters))
            break
        # end if
    # end for
    print("Total time = {0:f} ms".format((time.time()-start)*1000))

# end main

