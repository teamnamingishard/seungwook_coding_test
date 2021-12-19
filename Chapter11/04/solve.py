from typing import List

def find_minimum_num(n: int, x: List)->int:
  x.sort() # [1, 1, 2, 3, 9]
  
  target = 1
  for x_ in x:
    print(x_)
    if target < x_:
      break
    target += x_
    
  print(target)
  return target