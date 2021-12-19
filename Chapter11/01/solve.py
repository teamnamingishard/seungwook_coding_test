from typing import List

def find_maximum_group(n: int, x: List)->int:
  x.sort()
  result = 0
  count = 0
  for i in x:
    count += 1
    if count >= i:
      result += 1
      count = 0
  print(result)
  return result