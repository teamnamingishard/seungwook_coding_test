N, K = map(int, input().split())

result = 0
while N >= K:
    if N % K != 0:
        N -= 1
        result += 1
        continue

    N //= K
    result += 1

while N > 1:
    N -= 1
    result += 1

print(result)