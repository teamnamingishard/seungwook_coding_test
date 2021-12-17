
from typing import List


def find_minimum_time(N: int, P: List):
  P.sort()
  for i in range(1, N):
    P[i] += P[i-1]
  return sum(P)

if __name__ == "__main__":
  N = int(input())
  P = list(map(int, input().split()))
  find_minimum_time(N, P)

