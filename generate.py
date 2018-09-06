#!/usr/bin/env python3

import random

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
    if random.randint(0, 1):
        return 1

    return 5


def random_event(n):
    return str(n) + "Blue"

def random_bosses(n):
    return [str(n) + "Boss"]

main()
