"""
ADVENT 2018 - Day 12

https://adventofcode.com/2018/day/12

"""

import re
import time

def read_state(s: str):
    state_str = re.match(r"initial state: (.*)", s).groups()[0]
    state = "...."+state_str+"...."
    center = 4
    return state, center

def read_rules(rules):
    pot_rules = {}
    for rule_str in rules:
        rule, out = re.match(r"(.*) => (.)*", rule_str.strip()).groups()
        pot_rules[rule] = out
    return pot_rules

def next_gen(state, center, patterns):
    new_state = [".", "."]
    for i in range(2, len(state)-2):
        match_found = False
        substr = state[i-2:i+3]
        # print(i, substr, substr in patterns)
        if substr in patterns:
            new_state.append(patterns[substr])
        else:
            new_state.append(".")

    # check if new pots added to the left or right
    add_left = 0
    add_right = 0
    if new_state[0] == "#":
        add_left += 1
    if new_state[1] == "#":
        add_left += 1

    if new_state[-1] == "#":
        add_right += 1
    if new_state[-2] == "#":
        add_right += 1

    new_state.extend([".", "."])

    # print(add_left, add_right, new_state)

    pots = "."*add_left + "".join(new_state) + "."*add_right

    center += add_left
    # print(pots)
    return pots, center



TEST_INPUT = ["initial state: #..#.#..##......###...###",
"",
"...## => #",
"..#.. => #",
".#... => #",
".#.#. => #",
".#.## => #",
".##.. => #",
".#### => #",
"#.#.# => #",
"#.### => #",
"##.#. => #",
"##.## => #",
"###.. => #",
"###.# => #",
"####. => #"]


def compute_pot_state(pot_input, NUM_GEN):
    initial_state, center = read_state(pot_input[0].strip())
    print(0, initial_state)
    pot_rules = read_rules(pot_input[2:])

    new_state = initial_state[:]
    for i in range(1,NUM_GEN+1):
        new_state, center = next_gen(new_state, center, pot_rules)
        # print(i, new_state, center, new_state.count("#"))
        total = 0
        for j, c in enumerate(new_state):
            total += (j-center) if c == "#" else 0
        print(i, total)

# compute_pot_state(TEST_INPUT, 20)

with open("./data/day12.txt", "r") as in_f:
    INPUT = in_f.readlines()

"""
Part 1
"""
compute_pot_state(INPUT, 20)

"""
Part 2

gen# total
100 4602
101 4655
102 4698
103 4744
104 4790
105 4836
106 4882
107 4928
108 4974

After iteration 102, in each generation 46 plants are added
Therefore, in 50 billion:
((50000000000-102) * 46) + 4698
 = 2300000000006
"""
START = time.time()
compute_pot_state(INPUT, 1000)
print("Total time = {0:f} ms".format((time.time()-START)*1000))
