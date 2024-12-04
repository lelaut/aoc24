#!/usr/bin/python3

# https://adventofcode.com/2024/day/4

from d0 import Challenge

class CeresSearch(Challenge):
  def solution_p1(self, filename: str) -> int:
    def check(text_yx: str, x: int, y: int) -> int:
      target = list("XMAS")

      def step(direction_xy: tuple[int, int], i: int = 0):
        if text_yx[y+direction_xy[1]*i][x+direction_xy[0]*i] != target[i]:
          return 0
        
        i += 1
        
        if i == len(target):
          return 1
        if y+direction_xy[1]*i < 0 or y+direction_xy[1]*i == len(text_yx):
          return 0
        if x+direction_xy[0]*i < 0 or x+direction_xy[0]*i == len(text_yx[direction_xy[1]*i]):
          return 0

        return step(direction_xy, i)

      all_directions_xy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)]

      return sum([step(direction_xy) for direction_xy in all_directions_xy])
    
    with open(filename) as f:
      text_yx = f.read().split()
    ans = 0

    for y in range(len(text_yx)):
      for x in range(len(text_yx[y])):
        ans += check(text_yx, x, y)

    return ans

  def solution_p2(self, filename: str) -> int:
    def check(text_yx: str, x: int, y: int) -> int:
      if text_yx[y][x] != "A":
        return 0
      
      all_configs = [(-1, -1, "M"), (1, 1, "S"), (1, -1, "M"), (-1, 1, "S")]

      for i in range(4):
        invert_config = [i & 0b1, i & 0b10]
        found = True

        for j in range(4):
          [dx, dy, c] = all_configs[j]
          invert = invert_config[j >> 1]
          c = ("M" if c == "S" else "S") if invert else c

          if text_yx[y+dy][x+dx] != c:
            found = False
            break
        
        if found:
          return 1
      
      return 0
    
    with open(filename) as f:
      text_yx = f.read().split()
    ans = 0

    for y in range(1, len(text_yx) - 1):
      for x in range(1, len(text_yx[y]) - 1):
        ans += check(text_yx, x, y)

    return ans

CeresSearch(day=4, p1_sample=18, p2_sample=9).run()