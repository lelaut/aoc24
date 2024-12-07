#!/usr/bin/python3

# https://adventofcode.com/2024/day/7

from d0 import Challenge

class BridgeRepair(Challenge):
  all_operators: list[str]

  def step(self, target: int, acc: int, operator: str, values: list[int]) -> int:
    if len(values) == 0:
      return target if acc == target else 0
      
    value = values[0]
    if operator == "+":
      acc += value
    elif operator == "*":
      acc *= value
    else:
      acc = acc * 10 ** len(str(value)) + value

    if acc > target:
      return 0
    return max(map(lambda op: self.step(target, acc, op, values[1:]), self.all_operators))
  
  def solution_p1(self, filename: str) -> int:
    with open(filename) as file:
      all_equations = list(map(lambda line: list(map(int, line.replace(":", "").split())), file.read().split("\n")))

    ans = 0
    self.all_operators = ["+", "*"]
    for equation in all_equations:
      target = equation[0]
      acc = equation[1]
      values = equation[2:]

      ans += max(map(lambda op: self.step(target, acc, op, values), self.all_operators))
      
    return ans

  def solution_p2(self, filename: str) -> int:
    with open(filename) as file:
      all_equations = list(map(lambda line: list(map(int, line.replace(":", "").split())), file.read().split("\n")))

    ans = 0
    self.all_operators = ["+", "*", "||"]
    for equation in all_equations:
      target = equation[0]
      acc = equation[1]
      values = equation[2:]

      ans += max(map(lambda op: self.step(target, acc, op, values), self.all_operators))
      
    return ans

BridgeRepair(day=7, p1_sample=3749, p2_sample=11387).run()