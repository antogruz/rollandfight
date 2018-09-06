#!/usr/bin/env python3

import random
from patterns import *

fullsize = 25

def main():
    print([2] + generate(2))

def generate(n):
    gap = random_gap()

    if (n + gap >= fullsize):
        return [gap] + random_bosses(n + gap)

    return [gap, random_event(gap + n)] + generate(gap + n)

def random_gap():
    draw = random.randint(0, 9)
    if draw < 5 :
        return 3
    if draw < 7 :
        return 2
    if draw < 9 :
        return 4
    if coinflip():
        return 1

    return 5

def random_event(n):
    if coinflip():
        return random_encounter(n)
    else:
        return random_location(n)

def random_encounter(n):
    pattern = random_pattern()
    return pattern.get(n)

def random_pattern():
    draw = random.randint(0, 10)
    if draw < 7 :
        return SurviveOrWin()
    if draw < 10 :
        return MultipleWays(1)
    return MultipleWays(2)

def random_location(n):
    return str(n) + "location"

def coinflip():
    return random.randint(0, 1)

def random_bosses(n):
    return [str(n) + "Boss"]

main()
