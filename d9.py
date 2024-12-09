#!/usr/bin/python3

# https://adventofcode.com/2024/day/9

from d0 import Challenge

class DiskFragmenter(Challenge):
  def setup(self, filename: str) -> tuple[list[list[int]], list[list[int]]]:
    with open(filename) as file:
      disk_map = [int(c) for c in file.read()]
    file_space = []
    free_space = []
    disk_pos = 0
    for disk_i in range(len(disk_map)):
      is_free = (disk_i % 2) == 1
      
      if is_free:
        free_space.append([disk_pos, disk_map[disk_i]])
      else:
        file_space.append([disk_pos, disk_map[disk_i], len(file_space)])
      
      disk_pos += disk_map[disk_i]
      
    return file_space, free_space
  
  def checksum(self, file_space: list[list[int]]):
    return sum([sum([(f+file[0])*file[2] for f in range(file[1])]) for file in file_space])
  
  def solution_p1(self, filename: str) -> int:
    file_space, free_space = self.setup(filename)
    
    while len(free_space) > 0 and free_space[0][0] < file_space[-1][0]:
      if free_space[0][1] < file_space[-1][1]:
        file_space[-1][1] -= free_space[0][1]
        file_space.append(free_space[0] + [file_space[-1][2]])
        free_space.pop(0)
      else:
        file_space[-1] = [free_space[0][0]] + file_space[-1][1:]
        free_space[0][0] += file_space[-1][1]
        free_space[0][1] -= file_space[-1][1]
        
      file_space.sort(key=lambda x: x[0])
      
    return self.checksum(file_space)
      
  def solution_p2(self, filename: str) -> int:
    file_space, free_space = self.setup(filename)
    
    search_index = list(range(len(file_space)))
    for file_id in reversed(range(len(file_space))):
      file_i = search_index[file_id]
      
      for free_i in range(len(free_space)):
        if free_space[free_i][0] > file_space[file_i][0]:
          break
        
        if free_space[free_i][1] >= file_space[file_i][1]:
          search_index[file_i] = free_space[free_i][0]
          file_space[file_i] = [free_space[free_i][0]] + file_space[file_i][1:]
          free_space[free_i][0] += file_space[file_i][1]
          free_space[free_i][1] -= file_space[file_i][1]
          break
        
    return self.checksum(file_space)

DiskFragmenter(day=9, p1_sample=1928, p2_sample=2858).run()