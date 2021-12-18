from typing import List

def minimum_price(n: int, length: List, price: List) -> int:
  res = 0
  m = price[0]
  for i in range(n-1):
    if price[i] < m:
      m = price[i]
    res += m * length[i]
  print(res)
  return res

if __name__ == "__main__":
  n = int(input())
  length = list(map(int, input().split()))
  price = list(map(int, input().split()))
  minimum_price(n, length, price)