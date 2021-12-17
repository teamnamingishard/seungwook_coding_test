
def minimize_number(expression: str):
  expression = expression.split("-")
  sum = 0
  for num in expression[0].split("+"):
    sum += int(num)
  for num in expression[1:]:
    for num_ in num.split("+"):
      sum -= int(num_)
  print(sum)
  return sum

if __name__ == "__main__":
  input = input()
  minimize_number(input)
  