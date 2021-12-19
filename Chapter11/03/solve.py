
def find_minimum_count(s: str)->int:
  count_0 = 0 # 모두 0으로 만드는 경우
  count_1 = 0
  
  if s[0] == '1':
    count_0 += 1
  else:
    count_1 += 1
    
  for i in range(len(s) - 1):
    if s[i] != s[i+1]:
      if s[i+1] == '1':
        count_0 += 1
      else:
        count_1 += 1
  
  result = min(count_0, count_1)
  print(result)
  return result