N, M = map(int, input().split())

result = 0

for i in range(N):
    data = list(map(int, input().split()))
    min_value = 10001  # 입력되는 수는 10000 이하 이므로 초기값은 이와 같이 함
    for d in data:
        min_value = min(min_value, d)

    result = max(result, min_value)

print(result)