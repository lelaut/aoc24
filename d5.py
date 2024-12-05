#!/usr/bin/python3

# https://adventofcode.com/2024/day/5

from d0 import Challenge

class PrintQueue(Challenge):
  def get_input(self, filename: str):
    with open(filename) as file:
      text = file.read()

    [rawOrder, batches] = text.split("\n\n")
    rawOrder = list(map(lambda x: list(map(int, x.split("|"))), rawOrder.split()))
    batches = list(map(lambda x: list(map(int, x.split(","))), batches.split()))

    order: dict[int, set] = {}
    for rule in rawOrder:
      if rule[0] in order:
        order[rule[0]].add(rule[1])
      else:
        order[rule[0]] = set([rule[1]])

    return order, batches

  def solution_p1(self, filename: str) -> int:
    order, batches = self.get_input(filename)
    
    ans = 0
    for batch in batches:
      correct = True
      
      for i in range(len(batch)):
        if batch[i] not in order:
          continue

        after = order[batch[i]]
        for j in range(0, i):
          if batch[j] in after:
            correct = False
            break
        
      if correct:
        ans += batch[len(batch)//2]

    return ans
    

  def solution_p2(self, filename: str) -> int:
    order, batches = self.get_input(filename)
    
    def sort_batch(batch, fixed = False):
      for i in range(len(batch)):
        
        if batch[i] not in order:
          continue

        after = order[batch[i]]
        for j in range(0, i):
          if batch[j] in after:
            swap = batch[i]
            batch[i] = batch[j]
            batch[j] = swap
            return sort_batch(batch, True)
          
      return batch[len(batch) // 2] if fixed else 0          

    return sum([sort_batch(batch) for batch in batches])

PrintQueue(day=5, p1_sample=143, p2_sample=123).run()