N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

first_count = int(M / (K + 1)) * K + M % (K + 1)
second_count = M - first_count

result = 0
result += first_count * first
result += second_count * second

print(result)
