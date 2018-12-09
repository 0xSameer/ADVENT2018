"""
ADVENT 2018 - Day 08

https://adventofcode.com/2018/day/8

"""

import time
from typing import List, Dict, Tuple


class Node:
    def __init__(self, n_id, n_child: int, n_meta: int)-> None:
        self.n_id = n_id
        self.n_child = n_child
        self.n_meta = n_meta
        self.child = []
        self.meta = None
        self.value = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


def dfs(nums: List[int], curr: int, nodes: Dict[str, Node]) -> \
                                                    Tuple[Node, int]:
    # Create a new node
    # unique id is the current index in the license
    n_id = curr
    node = Node(n_id, nums[curr], nums[curr+1])
    curr += 2

    # Process child nodes
    for i in range(node.n_child):
        child_node, curr = dfs(nums, curr, nodes)
        node.child.append(child_node)
    # end for

    # Get meta data value
    meta_data = nums[curr:curr+node.n_meta]
    node.meta = meta_data
    curr += node.n_meta

    # Calculate value
    if node.n_child == 0:
        node.value = sum(meta_data)

    else:
        value = 0
        for i in meta_data:
            if i <= node.n_child:
                value += node.child[i-1].value
        # end for
        node.value = value
    # end else

    # Add node to dictionary
    nodes[n_id] = node

    return node, curr

def parse_license(nums: List[int]) -> Dict[str, Node]:
    N = len(nums)
    nodes = {}
    head, curr = dfs(nums, 0, nodes)

    return nodes



TEST_INPUT = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

test_nodes = parse_license(TEST_INPUT)
assert (sum([sum(node.meta) for node in test_nodes.values()]) == 138)
assert (test_nodes[0].value == 66)


if __name__ == "__main__":
    with open("./data/day08.txt", "r") as in_f:
        INPUT = [int(i) for i in in_f.read().strip().split()]

    """
    Part One, and Two
    Complexity: O(N)
    Runtime: 14 ms
    """
    START = time.time()
    nodes = parse_license(INPUT)
    meta_sum = sum([sum(node.meta) for node in nodes.values()])
    print("Part 1 solution: {0:d}".format(meta_sum))
    print("Part 2 solution: {0:d}".format(nodes[0].value))
    print("Total time = {0:f} ms".format((time.time()-START)*1000))