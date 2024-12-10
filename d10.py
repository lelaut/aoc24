#!/usr/bin/python3

# https://adventofcode.com/2024/day/10

from d0 import Challenge

class HoofIt(Challenge):
  def compute(self, filename: str) -> list[int]:
    with open(filename) as file:
      text = file.read()
      
    map_width = text.index("\n")
    map_tiles = [int(c) for c in text.replace("\n", "")]
    map_size = len(map_tiles)
    all_trailhead = [i for i in range(map_size) if map_tiles[i] == 0]    
    all_directions = [-map_width, 1, map_width, -1]
    
    def step(pos_i: int, height: int) -> list[list[int]]:
      if height == 9:
        return [pos_i]
      
      scores = []
      next_height = height + 1
      for direction in all_directions:
        pos_y = pos_i // map_width
        pos_j = pos_i + direction

        if pos_j < 0 or pos_j >= map_size:
          continue
        if abs(direction) == 1 and (pos_j // map_width) != pos_y:
          continue
        
        if map_tiles[pos_j] == next_height:
          scores.extend(step(pos_j, next_height))
          
      return scores
      
    return [step(trailhead, 0) for trailhead in all_trailhead]
  
  def solution_p1(self, filename: str) -> int:
    return sum([len(set(item)) for item in self.compute(filename)])

  def solution_p2(self, filename: str) -> int:
    return sum([len(item) for item in self.compute(filename)])

HoofIt(day=10, p1_sample=36, p2_sample=81).run()