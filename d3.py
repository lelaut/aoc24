#!/usr/bin/python3

# https://adventofcode.com/2024/day/3

from d0 import Challenge

class MullItOver(Challenge):
  def literal(self, text: str, offset: int, value: str):
    return (value, offset + len(value)) if text[offset:].startswith(value) else (None, offset)

  def number(self, text: str, offset: int):
    n, i = 0, 0

    while offset+i < len(text):
      try:
        v = int(text[offset:offset+i+1]) 
      except Exception:
        return (None, offset) if i == 0 else (n, offset+i)

      n = v
      i += 1

    return (n, offset+i)
  
  def parse(self, text: str, offset: int, expr: list[str]):
    buffer = []

    while offset < len(text) and len(buffer) < len(expr):
      e = expr[len(buffer)]

      if e[0] == 'L':
        (v, offset) = self.literal(text, offset, value=e[1:])
      elif e[0] == 'N':
        (v, offset) = self.number(text, offset)
      else:
        raise Exception("Not implemented")

      if v is None:
        break

      buffer.append(v)
      
    return buffer if len(buffer) == len(expr) else None
    
  def solution_p1(self, filename: str) -> int:
    mul_expr = ['Lmul(', 'N', 'L,', 'N', 'L)']

    with open(filename) as file:
      text = file.read()

    ans = 0

    for offset in range(len(text)):
      parsed = self.parse(text, offset, mul_expr)
      if parsed:
        ans += parsed[1]*parsed[3]

    return ans

  def solution_p2(self, filename: str) -> int:
    mul_expr = ['Lmul(', 'N', 'L,', 'N', 'L)']
    do_expr = ['Ldo()']
    dont_expr = ["Ldon't()"]

    with open(filename) as file:
      text = file.read()

    ans = 0
    enabled = True

    for offset in range(len(text)):
      parsed = self.parse(text, offset, mul_expr)
      if parsed:
        ans += parsed[1]*parsed[3] if enabled else 0
      elif enabled:
        if self.parse(text, offset, dont_expr):
          enabled = False
      else:
        if self.parse(text, offset, do_expr):
          enabled = True

    return ans

MullItOver(day=3, p1_sample=161, p2_sample=48).run()