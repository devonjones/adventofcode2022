#!/usr/bin/env python
import sys

def get_elves(data):
    elves = []
    elf = None
    for line in data:
        l = line.strip()
        if len(l) == 0 and elf != None:
            elves.append(elf)
            elf = None
        else:
            if elf == None:
                elf = 0
            elf += int(l)
    return elves

def top_three(elves):
    elves.sort()
    return elves[-3:]

def main():
    data = sys.stdin.readlines()
    elves = get_elves(data)
    print(max(elves))
    top = top_three(elves)
    print(sum(top))

if __name__ == "__main__":
        sys.exit(main())
