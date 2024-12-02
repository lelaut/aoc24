#!/usr/bin/python3

# https://adventofcode.com/2024/day/2

from d0 import Challenge
from typing import TypeAlias

class RedNosedReports(Challenge):
  def check(self, levels: list[int]) -> bool:
    cur = levels[0]
    inc = levels[0] < levels[1]

    for item in levels[1:]:
      if inc and cur > item:
        return False
      if not inc and cur < item:
        return False

      diff = abs(cur-item)
      if diff < 1 or diff > 3:
        return False
            
      cur = item

    return True
    
  def solution_p1(self, filename: str) -> int:
    safe = 0

    with open(filename) as file:
      for line in file:
        row = list(map(int, line.split()))
        
        if self.check(row):
          safe += 1

    return safe

  def solution_p2(self, filename: str) -> int:
    safe = 0

    with open(filename) as file:
      for line in file:
        row = list(map(int, line.split()))
        
        if self.check(row):
          safe += 1
        else:
          for i in range(len(row)):
            if self.check(row[:i] + row[i+1:]):
              safe += 1
              break

    return safe

RedNosedReports(2, 2, 4).run()