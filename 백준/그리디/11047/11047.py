## 동전 0
N, K = map(int, input().split())
coin_list = []
for _ in range(N):
  coin_list.append(int(input()))
# arr = [int(input()) for _ in range(N)]

count, idx = 0, N-1

while K != 0:
  if coin_list[idx] > K:
    idx -= 1
  else:
    count += K // coin_list[idx]
    K %= coin_list[idx]

print(count)
    
