#!/usr/bin/env python
import sys
from pprint import pprint

#Fri Dec  2 11:56:27 MST 2022
#Fri Dec  2 12:07:59 MST 2022

#Fri Dec  2 12:09:45 MST 2022
#Fri Dec  2 12:18:10 MST 2022

def score(rounds):
    score_list = []
    object = {'X': 1, 'Y': 2, 'Z': 3}
    results = {
        'AX': 3, 'AY': 6, 'AZ': 0,
        'BX': 0, 'BY': 3, 'BZ': 6,
        'CX': 6, 'CY': 0, 'CZ': 3,
    }
    for round in rounds:
        a,b = round
        round_score = 0
        round_score += object[b]
        round_score += results["%s%s" % (a,b)]
        score_list.append(round_score)
    return(score_list)

def real_score(rounds):
    newrounds = []
    choice = {
        'AX': ('A','Z'), 'AY': ('A','X'), 'AZ': ('A','Y'),
        'BX': ('B','X'), 'BY': ('B','Y'), 'BZ': ('B','Z'),
        'CX': ('C','Y'), 'CY': ('C','Z'), 'CZ': ('C','X'),
    }

    for round in rounds:
        a,b = round
        newrounds.append(choice["%s%s" % (a,b)])
    return newrounds

def get_rounds(data):
    rounds = []
    for line in data:
        l = line.strip()
        if len(l) != 0:
            a, b = l.split(" ")
            rounds.append((a,b))
    return rounds

def main():
    data = sys.stdin.readlines()
    rounds = get_rounds(data)
    score_list = score(rounds)
    print(sum(score_list))
    new_rounds = real_score(rounds)
    new_score_list = score(new_rounds)
    print(sum(new_score_list))

if __name__ == "__main__":
        sys.exit(main())
