#!/usr/bin/python3

# https://adventofcode.com/2024/day/6

from d0 import Challenge

class GuardGallivant(Challenge):
  def solution_p1(self, filename: str) -> int:
    with open(filename) as file:
      text = file.read()

    map_width = text.index("\n")
    map_tiles = text.replace("\n", "")
    map_moves = [0] * len(map_tiles)
    guard_i = map_tiles.index("^")
    map_moves[guard_i] = 1
    directions = [-map_width, 1, map_width, -1]
    guard_rot = 0

    def count_forward() -> tuple[int, bool]:
      forward_i = guard_i + directions[guard_rot]
      guard_y = guard_i // map_width

      while forward_i >= 0 and forward_i < len(map_tiles) and map_tiles[forward_i] != "#":
        if guard_rot % 2 == 1 and guard_y != (forward_i // map_width):
          return forward_i - directions[guard_rot], True
        
        map_moves[forward_i] = 1
        forward_i += directions[guard_rot]

      guard_out = forward_i < 0 or forward_i >= len(map_tiles)

      return forward_i - directions[guard_rot], guard_out

    while True:
      guard_j, guard_out = count_forward()

      if guard_out:
        return sum(map_moves)

      guard_i = guard_j
      guard_rot = (guard_rot+1) % 4

  def solution_p2(self, filename: str) -> int:
    with open(filename) as file:
      text = file.read()

    map_width = text.index("\n")
    map_tiles = text.replace("\n", "")
    start_guard_i = map_tiles.index("^")
    directions = [-map_width, 1, map_width, -1]

    def in_loop(guard_i: int, guard_rot: int) -> int:
      direction_change = {}

      while True:
        guard_y = guard_i // map_width
        guard_i += directions[guard_rot]

        while guard_i >= 0 and guard_i < len(map_tiles) and map_tiles[guard_i] != "#":
          if guard_rot % 2 == 1 and guard_y != (guard_i // map_width):
            return 0
          
          guard_i += directions[guard_rot]

        if guard_i < 0 or guard_i >= len(map_tiles):
          return 0
        if guard_rot % 2 == 1 and guard_y != (guard_i // map_width):
            return 0

        guard_i -= directions[guard_rot]
        guard_rot = (guard_rot+1) % 4
        if guard_i in direction_change:
          if (direction_change[guard_i] & (1 << guard_rot)) != 0:
            return 1
          
          direction_change[guard_i] |= 1 << guard_rot
        else:
          direction_change[guard_i] = 1 << guard_rot

    loops = 0
    computed = set()
    guard_i = start_guard_i
    guard_rot = 0
    while True:
      guard_y = guard_i // map_width
      block_i = guard_i + directions[guard_rot]

      if block_i < 0 or block_i >= len(map_tiles):
        break
      if guard_rot % 2 == 1 and (block_i // map_width) != guard_y:
        break
      if map_tiles[block_i] == "#":
        guard_rot = (guard_rot+1) % 4
        continue

      if block_i != start_guard_i and block_i not in computed:
        map_tiles = map_tiles[:block_i] + "#" + map_tiles[block_i+1:]
        loops += in_loop(guard_i, guard_rot)
        computed.add(block_i)
        map_tiles = map_tiles[:block_i] + "." + map_tiles[block_i+1:]

      guard_i = block_i

    return loops

GuardGallivant(day=6, p1_sample=41, p2_sample=6).run()