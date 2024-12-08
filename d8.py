#!/usr/bin/python3

# https://adventofcode.com/2024/day/8

from d0 import Challenge
from typing import Callable

class ResonantCollinearity(Challenge):
  map_width: int
  map_size: int
  
  def pos_xy(self, index: int) -> tuple[int, int]:
    return index % self.map_width, index // self.map_width
    
  def pos_index(self, x: int, y: int) -> int:
    if y < 0 or y * self.map_width >= self.map_size:
      return None
    if x < 0 or x >= self.map_width:
      return None
      
    return y*self.map_width+x
    
  def each_antenna_in_frequency(self, filename: str, process: Callable[[int, int], None]):
    with open(filename) as file:
      text = file.read()
    self.map_width = text.index("\n")
    map_tiles = text.replace("\n", "")
    self.map_size = len(map_tiles)
    
    antennas: dict[str, list[int]] = {}
    for pos in range(len(map_tiles)):
      tile = map_tiles[pos]
      if tile != ".":
        if tile in antennas:
          antennas[tile].append(pos)
        else:
          antennas[tile] = [pos]
          
    for antennas_by_frequencies in antennas.values():
      for i in range(len(antennas_by_frequencies)):
        for j in range(i+1, len(antennas_by_frequencies)):
          process(antennas_by_frequencies[i], antennas_by_frequencies[j])
  
  def solution_p1(self, filename: str) -> int:
    all_antinode = set()
    
    def add_antinodes(antenna_i: int, antenna_j: int):
      xi,yi = self.pos_xy(antenna_i)
      xj,yj = self.pos_xy(antenna_j)
      
      xd = xi-xj
      yd = yi-yj
          
      antinode_a = self.pos_index(xi+xd, yi+yd)
      if antinode_a != None:
        all_antinode.add(antinode_a)
      antinode_b = self.pos_index(xj-xd, yj-yd)
      if antinode_b != None:
        all_antinode.add(antinode_b)
      
    self.each_antenna_in_frequency(filename, add_antinodes)
    
    return len(all_antinode)

  def solution_p2(self, filename: str) -> int:
    all_antinode = set()
    
    def add_antinodes(antenna_i: int, antenna_j: int):
      all_antinode.add(antenna_i)
      all_antinode.add(antenna_j)
      
      xi,yi = self.pos_xy(antenna_i)
      xj,yj = self.pos_xy(antenna_j)
      
      xd = xi-xj
      yd = yi-yj
      
      for direction in [1, -1]:
        k = 1
        while True:
          antinode = self.pos_index(xi+xd*k*direction, yi+yd*k*direction)
          if antinode == None:
            break
          all_antinode.add(antinode)
          k += 1
      
    self.each_antenna_in_frequency(filename, add_antinodes)
    
    return len(all_antinode)

ResonantCollinearity(day=8, p1_sample=14, p2_sample=34).run()