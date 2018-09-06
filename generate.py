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
    return 3

def random_event(n):
    return str(n) + "Blue"

def random_bosses(n):
    return [str(n) + "Boss"]

main()
