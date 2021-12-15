from typing import List


def find_big_num(input: List):
  a, b = input
  return max(int(str(a)[::-1]), int(str(b)[::-1]))