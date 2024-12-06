#!/usr/bin/python3

import time

class Challenge:
  def __init__(self, day: int, p1_sample: int, p2_sample: int = None):
    self.day = day
    self.p1_sample = p1_sample
    self.p2_sample = p2_sample

  def run(self):
    sample_filename = f"sample/d{self.day}.txt"
    input_filename = f"input/d{self.day}.txt"

    start_time = time.time()
    sample_p1 = self.solution_p1(sample_filename)
    sol_time = time.time() - start_time
    assert sample_p1 == self.p1_sample, f"Fail part 1: {sample_p1} != {self.p1_sample}"
    print(f"Day {self.day} part 1 test passed in {sol_time} seconds")

    has_p2 = self.p2_sample is not None

    if has_p2:
      start_time = time.time()
      sample_p2 = self.solution_p2(sample_filename)
      sol_time = time.time() - start_time
      assert sample_p2 == self.p2_sample, f"Fail part 2: {sample_p2} != {self.p2_sample}"
      print(f"Day {self.day} part 2 test passed in {sol_time} seconds")

    start_time = time.time()
    input_p1 = self.solution_p1(input_filename)
    sol_time = time.time() - start_time
    print(f"Day {self.day} part 1 answer is {input_p1} in {sol_time} seconds")
    if has_p2:
      start_time = time.time()
      input_p2 = self.solution_p2(input_filename)
      sol_time = time.time() - start_time
      print(f"Day {self.day} part 2 answer is {input_p2} in {sol_time} seconds")

  def solution_p1(self, filename: str) -> int:
    pass
  
  def solution_p2(self, filename: str) -> int:
    pass

if __name__ == "__main__":
  print("This file should not be run as main...")