#!/usr/bin/env python3

import random

NUM = 100

def prisoner_escape():
    inside_numbers = random.sample([x for x in range(NUM)], NUM)
    for prisoner in range(NUM):
        found = False
        box_num = prisoner
        for _ in range(NUM // 2):
            if inside_numbers[box_num] == prisoner:
                found = True
                break
            else:
                box_num = inside_numbers[box_num]
        if not found:
            return False
    return True

def main():
    while True:
        win = 0
        los = 1
        for _ in range(1_000):
            if prisoner_escape():
                win += 1
            else:
                los += 1
        print(f'{win} | {los} : {win / (win + los)}')

if __name__ == '__main__':
    main()