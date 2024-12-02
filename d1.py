#!/usr/bin/python3

# https://adventofcode.com/2024/day/1

from d0 import Challenge

class HistorianHysteria(Challenge):
  def solution_p1(self, filename: str) -> int:
    left = []
    right = []

    with open(filename) as file:
      for line in file:
        [l, r] = map(int, line.split("   "))
        left.append(l)
        right.append(r)

    left.sort()
    right.sort()

    return sum([abs(right[i] - left[i]) for i in range(len(left))])

  def solution_p2(self, filename: str) -> int:
    left = []
    right = {}

    with open(filename) as file:
      for line in file:
        [l, r] = map(int, line.split("   "))
        left.append(l)
        right[r] = right[r]+1 if r in right else 1
    
    return sum([l * right[l] if l in right else 0 for l in left])

HistorianHysteria(1, 11, 31).run()