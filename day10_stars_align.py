"""
ADVENT 2018 - Day 10

https://adventofcode.com/2018/day/10

"""

from typing import List
import re
import time
import math

class Point:
    def __init__(self,x: int, y: int, dx: int, dy: int):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move_point(self, steps: int):
        self.x += (steps*self.dx)
        self.y += (steps*self.dy)

    @staticmethod
    def parse_point(s: str) -> "Point":
        rx = r"position=<\s*([-0-9]+),\s*([-0-9]+)> velocity=<\s*([-0-9]+),\s*([-0-9]+)>"

        return Point(*list(map(int, re.match(rx, s).groups())))

    def __str__(self):
        vals = [self.x, self.y, self.dx, self.dy]
        return "x,y={0:d},{1:d}, dx,dy={2:d},{3:d}".format(*vals)

    def __repr__(self):
        vals = [self.x, self.y, self.dx, self.dy]
        return "x,y={0:d},{1:d}, dx,dy={2:d},{3:d}".format(*vals)

# end class Point

def move_points(points: List[Point], steps: int) -> None:
    for p in points:
        p.move_point(steps)

def grid_size(points: List[Point]) -> None:
    xvals = [p.x for p in points]
    yvals = [p.y for p in points]
    x_min, x_max = min(xvals), max(xvals)
    y_min, y_max = min(yvals), max(yvals)
    return (x_max-x_min+1) + (y_max-y_min+1)


def display_points(points: List[Point]) -> None:
    xvals = [p.x for p in points]
    yvals = [p.y for p in points]

    locs = set()
    for p in points:
        locs.add((p.x, p.y))
    
    x_min, x_max = min(xvals), max(xvals)
    y_min, y_max = min(yvals), max(yvals)

    for y in range(y_min, y_max+1):
        for x in range(x_min, x_max+1):
            if (x,y) in locs:
                print("#", end="")
            else:
                print(".", end="")
        # end for row
        print("\n")

TEST_1 = "position=< 9,  1> velocity=< 0,  2>"
p = Point.parse_point(TEST_1)
print(p)
for i in range(5):
    p.move_point(i)
    print(p)

TEST_INPUT = [
    "position=< 9,  1> velocity=< 0,  2>",
    "position=< 7,  0> velocity=<-1,  0>",
    "position=< 3, -2> velocity=<-1,  1>",
    "position=< 6, 10> velocity=<-2, -1>",
    "position=< 2, -4> velocity=< 2,  2>",
    "position=<-6, 10> velocity=< 2, -2>",
    "position=< 1,  8> velocity=< 1, -1>",
    "position=< 1,  7> velocity=< 1,  0>",
    "position=<-3, 11> velocity=< 1, -2>",
    "position=< 7,  6> velocity=<-1, -1>",
    "position=<-2,  3> velocity=< 1,  0>",
    "position=<-4,  3> velocity=< 2,  0>",
    "position=<10, -3> velocity=<-1,  1>",
    "position=< 5, 11> velocity=< 1, -2>",
    "position=< 4,  7> velocity=< 0, -1>",
    "position=< 8, -2> velocity=< 0,  1>",
    "position=<15,  0> velocity=<-2,  0>",
    "position=< 1,  6> velocity=< 1,  0>",
    "position=< 8,  9> velocity=< 0, -1>",
    "position=< 3,  3> velocity=<-1,  1>",
    "position=< 0,  5> velocity=< 0, -1>",
    "position=<-2,  2> velocity=< 2,  0>",
    "position=< 5, -2> velocity=< 1,  2>",
    "position=< 1,  4> velocity=< 2,  1>",
    "position=<-2,  7> velocity=< 2, -2>",
    "position=< 3,  6> velocity=<-1, -1>",
    "position=< 5,  0> velocity=< 1,  0>",
    "position=<-6,  0> velocity=< 2,  0>",
    "position=< 5,  9> velocity=< 1, -2>",
    "position=<14,  7> velocity=<-2,  0>",
    "position=<-3,  6> velocity=< 2, -1>"
]

test_points = [Point.parse_point(p) for p in TEST_INPUT]
print("Time step: {0:d}".format(0))
display_points(test_points)
min_step = 0
min_size = math.inf
for i in range(0,5):
    move_points(test_points, 1 if i else 0)
    g_size = grid_size(test_points)
    print("Time step: {0:d}, grid size: {1:d}".format(i, g_size))
    if g_size < min_size:
        min_step = i
        min_size = g_size
print(min_step)
move_points(test_points, -i)
move_points(test_points, min_step)
display_points(test_points)


if __name__ == "__main__":
    with open("./data/day10.txt", "r") as in_f:
        INPUT = [line.strip() for line in in_f]

    points = [Point.parse_point(p) for p in INPUT]
    
    min_step = 0
    min_size = math.inf
    for i in range(0,100000):
        move_points(points, 1 if i else 0)
        g_size = grid_size(points)
        print("Time step: {0:d}, grid size: {1:d}".format(i, g_size))
        if g_size < min_size:
            min_step = i
            min_size = g_size
        else:
            break
        # end if
    # end for

    print(min_step)
    move_points(points, -1)
    display_points(points)