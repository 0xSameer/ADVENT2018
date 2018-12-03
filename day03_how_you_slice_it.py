"""
ADVENT 2018 - Day 03

https://adventofcode.com/2018/day/3

""" 

from typing import List
import numpy as np
import re

def check_claim(claim: str, fabric: np.array) -> None:
    #print(claim)
    reg_str = r"#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"
    n_claim, c, r, n_cols, n_rows  = map(int, re.match(reg_str, claim).groups())

    fabric[r:r+n_rows,c:c+n_cols] += 1
    return (n_claim, r, c, n_rows, n_cols)

def check_all_claims(claims: List[str], size=1000) -> int:
    fabric = np.zeros((size,size), dtype=np.int32)
    
    claim_details = []
    for claim in claims:
        claim = check_claim(claim, fabric)
        claim_details.append(claim)
    
    two_or_more_claims = len(fabric[fabric >= 2])
    
    return two_or_more_claims, fabric, claim_details
    
def check_claim_overlap(claim, fabric):
    _, r, c, n_rows, n_cols = claim
    return np.all(fabric[r:r+n_rows, c:c+n_cols] == 1)

# TEST_INPUT = """#123 @ 3,2: 5x4"""  

TEST_INPUT = ["#44 @ 220,541: 16x25"]

TEST_INPUT = ["#1 @ 1,3: 4x4", 
              "#2 @ 3,1: 4x4",
              "#3 @ 5,5: 2x2",
              "#3 @ 5,5: 1x1"]

# print(check_claim("#1 @ 1,3: 4x4", TEST_FABRIC))
# print(check_claim("#123 @ 3,2: 5x4", TEST_FABRIC))
print(check_all_claims(TEST_INPUT, 8))

if __name__ == "__main__":
    with open("./data/day03_a.txt", "r") as in_f:
        INPUT = [line.strip() for line in in_f]
        print(len(INPUT))
    
    two_or_more_claims, fabric, claim_ids = check_all_claims(INPUT, 1000)
    print(two_or_more_claims)

    # print(list(zip(*np.where(fabric == 1)[0])))
    for claim in claim_ids:
        if check_claim_overlap(claim, fabric):
            print(claim[0])
        # end if
    # end for
    


