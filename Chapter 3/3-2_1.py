N, M, K = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[N - 1]
second = data[N - 2]

result = 0

while True:
    if M == 0:
        break
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    result += second
    M -= 1

print(result)