"""
ADVENT 2018 - Day 04

https://adventofcode.com/2018/day/4

""" 

import operator
import re
from collections import deque
import numpy as np

from typing import NamedTuple, Tuple, List, Dict

class LogEntry(NamedTuple):
    year:   int
    month:  int
    day:    int
    hour:   int
    minute: int
    details: str

def parse_log_entry(s: str) -> Tuple[LogEntry]:
    rx = r"\[([0-9]+)-([0-9]+)-([0-9]+) ([0-9]+):([0-9]+)\] (.+)"
    vals = list(re.match(rx, s).groups())
    vals[:5] = map(int, vals[:5])
    entry = LogEntry(*vals)
    return entry

def parse_log_entries(s_list: List) -> LogEntry:
    log_entries = []
    for s in s_list:
        log_entries.append(parse_log_entry(s))
    return log_entries

def check_guard_data(log: List[LogEntry]) -> Dict[int, List[LogEntry]]:
    if len(log) == 0:
        return None
    
    # pattern to extract guard id
    rx_gid = r"Guard #([0-9]+)"

    # store guard level details in dictionary
    guard_data = {}

    # start with first entry
    c = 0
    # check entries until last sleep/wake pair
    while c < len(log)-3:
        if "Guard" in log[c].details:
            curr_g = int(re.match(rx_gid, log[c].details).groups()[0])
            if curr_g not in guard_data:
                guard_data[curr_g] = np.zeros(60, dtype=np.int32)
            c += 1
        else:
            # next pair of entries should be falls asleep
            # and wake up event
            sleep = log[c].minute
            c += 1
            wake = log[c].minute
            c += 1
            guard_data[curr_g][sleep:wake] += 1
        # end if-else
    # end while
    # return guard_data
    return guard_data



TEST_ENTRIES = ["[1518-11-01 00:00] Guard #10 begins shift",
                "[1518-11-01 00:05] falls asleep",
                "[1518-11-01 23:58] Guard #99 begins shift",
                "[1518-11-02 00:40] falls asleep",
                "[1518-11-02 00:50] wakes up",
                "[1518-11-04 00:02] Guard #99 begins shift",
                "[1518-11-04 00:36] falls asleep",
                "[1518-11-04 00:46] wakes up",
                "[1518-11-03 00:05] Guard #10 begins shift",
                "[1518-11-03 00:24] falls asleep",
                "[1518-11-03 00:29] wakes up",
                "[1518-11-05 00:03] Guard #99 begins shift",
                "[1518-11-05 00:45] falls asleep",
                "[1518-11-05 00:55] wakes up]",
                "[1518-11-01 00:25] wakes up",
                "[1518-11-01 00:30] falls asleep",
                "[1518-11-01 00:55] wakes up",
]

"""
TEST CODE
"""
# parse_log_entry("[1518-11-01 00:00] Guard #10 begins shift")
# print(TEST_ENTRIES[2])
# test_log = parse_log_entries(TEST_ENTRIES)
# test_log.sort(key=operator.attrgetter("year", "month", "day", "hour", "minute"))

# print(test_log[:3])
# test_guard_data = check_guard_data(test_log)

# max_sleep_guard = max(test_guard_data.items(), key=lambda t: np.sum(t[1]))[0]
# max_sleep_min = np.argmax(test_guard_data[max_sleep_guard])
# print(max_sleep_guard, max_sleep_min, (max_sleep_guard * max_sleep_min))


"""
MAIN CODE
"""
if __name__ == "__main__":
    with open("./data/day04_a.txt", "r") as in_f:
        INPUT = [line.strip() for line in in_f]

    log = parse_log_entries(INPUT)
    """
    sort data as per timestamps
    """
    log.sort(key=operator.attrgetter("year", "month", "day", "hour", "minute"))

    """
    for each guard, count the total sleep time for every minute
    between 0-59
    """
    guard_data = check_guard_data(log)

    """
    Strategy 1:
    Find the guard with the max total sleep time
    For this guard, find the minute with the highest sleep time
    """
    max_sleep_guard = max(guard_data.items(), key=lambda t: np.sum(t[1]))[0]
    max_sleep_min = np.argmax(guard_data[max_sleep_guard])
    print(max_sleep_guard, max_sleep_min, (max_sleep_guard * max_sleep_min))

    """
    Strategy 2:
    For each guard, find the minute where they sleep they most
    """
    g_id = max(guard_data.items(), key=lambda t: np.max(t[1]))[0]
    max_min = np.argmax(guard_data[g_id ])
    print(g_id, max_min, (g_id * max_min))
