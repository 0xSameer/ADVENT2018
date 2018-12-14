"""
ADVENT 2018 - Day 14

https://adventofcode.com/2018/day/14

"""

import time

class Recipes:
    def __init__(self):
        self.scores = [3,7]
        self.elf1 = 0
        self.elf2 = 1

    def add_recipe(self, n_recipes):
        while len(self.scores) < n_recipes:
            new_recipe = str(self.scores[self.elf1] + self.scores[self.elf2])
            for digit in new_recipe:
                self.scores.append(int(digit))
            self.elf1 = (1 + self.elf1 + self.scores[self.elf1]) % len(self.scores)
            self.elf2 = (1 + self.elf2 + self.scores[self.elf2]) % len(self.scores)
        # end while

    def find_recipe(self, recipe_str):
        found = False
        n_chars = len(recipe_str)
        pattern = [int(i) for i in recipe_str]
        while not found:
            new_recipe = str(self.scores[self.elf1] + self.scores[self.elf2])
            for digit in new_recipe:
                self.scores.append(int(digit))
                curr_score = self.scores[-n_chars:]
                if curr_score == pattern:
                    found = True
                    break
            
            self.elf1 = (1 + self.elf1 + self.scores[self.elf1]) % len(self.scores)
            self.elf2 = (1 + self.elf2 + self.scores[self.elf2]) % len(self.scores)
        return len(self.scores)-n_chars
        # end while

    def get_scores(self, start, num):
        # print(self.elf1, self.elf2)
        return "".join(map(str, self.scores[start:start+num]))

    def display_scores(self, start, num):
        # print(self.elf1, self.elf2)
        print("".join(map(str, self.scores[start:start+num])))


test = Recipes()
test.add_recipe(20)
assert (test.get_scores(9,10) == "5158916779")

test = Recipes()
assert (test.find_recipe("51589") == 9)
test = Recipes()
assert (test.find_recipe("01245") == 5)
test = Recipes()
assert (test.find_recipe("92510") == 18)
test = Recipes()
assert (test.find_recipe("59414") == 2018)


"""
Total time: 1 sec
"""
START = time.time()
part1 = Recipes()
part1.add_recipe(846601+20)
print(part1.get_scores(846601, 10))
print("Total time = {0:f} ms".format((time.time()-START)*1000))

"""
Total time: 28 secs
"""
START = time.time()
part2 = Recipes()
print(part2.find_recipe("846601"))
print("Total time = {0:f} ms".format((time.time()-START)*1000))

