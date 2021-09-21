N, K = map(int, input().split())
result = 0

while True:
    if N < K:
        break
    target = (N // K) * K
    result += N - target
    N = target

    result += 1
    N //= K

result += N - 1
print(result)