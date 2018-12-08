"""
ADVENT 2018 - Day 07

https://adventofcode.com/2018/day/7

"""

import re
import time
from typing import List, Tuple, Dict, Set

def parse_nodes(steps: List[str]) -> List[Tuple[str,str]]:
    rx = r"Step ([A-Z]+) must be finished before step ([A-Z]+) can begin."
    edges = []
    for s in steps:
        match = re.match(rx, s)
        if match:
            edges.append(match.groups())
    # end for
    return edges

def create_graph(steps: List[str]) -> Dict[str,List[str]]:
    edges = parse_nodes(steps)

    parents = {}

    for n1, n2 in edges:
        parents[n1] = []
        parents[n2] = []

    # O(N) - where N is number of edges
    for n1, n2 in edges:
        # add parent nodes
        parents[n2].append(n1)
    # end for

    for n in parents:
        parents[n] = set(parents[n])

    return parents


def explore_graph(graph: Dict[str,Set[str]]) -> str:
    explore = set(graph.keys())
    seen = set()
    order = []

    while(explore):
        curr_nodes = []
        # Find all nodes whose parent nodes
        # have been "seen"
        for n in explore:
            graph[n] = graph[n]-seen
            if len(graph[n]) == 0:
                curr_nodes.append(n)
            # end if
        # end for

        # Out of all available nodes, select
        # the lowest alphabetically
        curr = min(curr_nodes)
        # Add to seen, remove from explore, and add to 
        # return order
        seen.add(curr)
        order.append(curr)
        explore.remove(curr)
    # end while
    return "".join(order)

def multiple_workers(graph: Dict[str,Set[str]], 
                     workers: int, 
                     TIME: int) -> Tuple[str, int]:
    explore = set(graph.keys())
    seen = set()
    order = []
    rem_time = {}
    curr_time = 0

    while(explore):
        print(curr_time, rem_time)
        for c in sorted(rem_time.keys()):
            if rem_time[c] == curr_time:
                # Add to seen, remove from explore, and add to 
                # return order
                seen.add(c)
                order.append(c)
                explore.remove(c)
                del rem_time[c]
            # end for
        curr_nodes = []
        if len(rem_time) < workers:
            # Find all nodes whose parent nodes
            # have been "seen"
            for n in explore:
                graph[n] = graph[n]-seen
                if len(graph[n]) == 0 and n not in rem_time:
                    curr_nodes .append(n)
                # end if
            # end for

            # Out of all available nodes, select
            # the lowest alphabetically
            curr_nodes = sorted(curr_nodes)[:workers-len(rem_time)+1]

        for c in curr_nodes:
            print(c, end=", ")
            if c not in rem_time:
                rem_time[c] = ord(c)-ord('A')+1+curr_time+TIME
        
        curr_time += 1
        
    # end while
    return ("".join(order), curr_time)


TEST_INPUT = ["Step C must be finished before step A can begin.",
              "Step C must be finished before step F can begin.",
              "Step A must be finished before step B can begin.",
              "Step A must be finished before step D can begin.",
              "Step B must be finished before step E can begin.",
              "Step D must be finished before step E can begin.",
              "Step F must be finished before step E can begin."]

parents = create_graph(TEST_INPUT)
# print(parents)
# print(explore_graph(parents))
print(multiple_workers(parents,2,0))
# assert (explore_graph(parents) == 'CABDFE')

if __name__ == "__main__":
    with open("./data/day07_a.txt", "r") as in_f:
        INPUT = [line.strip() for line in in_f]
    parents = create_graph(INPUT)
    parents_copy = {k:v for k, v in parents.items()}
    """
    Part One
    Runtime: 450 ms
    """
    # START = time.time()
    # result = explore_graph(parents_copy)
    # print("Total time = {0:f} ms".format((time.time()-START)*1000))
    # print("Part 1 solution: {0:s}".format(result))

    """
    Part Two
    Runtime:  secs
    """
    parents_copy = {k:v for k, v in parents.items()}
    START = time.time()
    result = multiple_workers(parents_copy, 5, 60)
    print("Total time = {0:f} ms".format((time.time()-START)*1000))
    print("Part 2 solution: {0:d}, {1:s}".format(result[1], result[0]))

