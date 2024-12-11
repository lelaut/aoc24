#!/usr/bin/python3

# https://adventofcode.com/2024/day/11

from d0 import Challenge

class PlutonianPebbles(Challenge):
  def blink(self, filename: str, times: int) -> list[int]:
    with open(filename) as file:
      stones = [int(stone) for stone in file.read().split(" ")]
    
    counter: dict[int, int] = {}
    for stone in stones:
      if stone in counter:
        counter[stone] += 1
      else:
        counter[stone] = 1
    
    def count_digits(n: int):
      i = 0
      while n > 0:
        n //= 10
        i += 1
      return i
    
    for _ in range(times):
      for stone, amount in list(counter.items()):
        if stone == 0:
          counter[1] = counter.get(1, 0) + amount
        else:
          stone_digits = count_digits(stone)
          
          if stone_digits % 2 == 0:
            stone_cut = (10 ** (stone_digits // 2))
            l_stone = stone // stone_cut
            r_stone = stone % stone_cut
            
            counter[l_stone] = counter.get(l_stone, 0) + amount
            counter[r_stone] = counter.get(r_stone, 0) + amount
          else:
            counter[stone*2024] = counter.get(stone*2024, 0) + amount

        counter[stone] -= amount
        if counter[stone] == 0:
          counter.pop(stone)

    return sum(counter.values())
  
  def solution_p1(self, filename: str) -> int:
    return self.blink(filename, times=25)

  def solution_p2(self, filename: str) -> int:
    return self.blink(filename, times=75)

PlutonianPebbles(day=11, p1_sample=55312, p2_sample=65601038650482).run()