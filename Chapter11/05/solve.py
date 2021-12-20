from typing import List

def find_combination(n: int, m:int, data: List)->int:
  array = [0] * 11 # 1 ~ 10까지의 무게를 담을 수 있는 리스트, 볼링공의 무게의 범위
  for datum in data:
    array[datum] += 1
  result = 0
  for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n
  
  print(result)
  return result