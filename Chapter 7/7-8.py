# 떡볶이 떡 자르기
## 전형적인 이진 탐색 문제이자, 파라메트릭 서치 유형(최적화 문제를 결정 문제로 바꾸어 해결하는 기법, 즉 예 - 아니오로 답하는 문제)

### 또한 문제에서 탐색 범위가 최대 10억까지의 정수이므로 바로 `이진 탐색`을 떠올려야 한다.

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid  # 최대한 덜 잘랐을 때가 정답이므로, 여기서 result에 우선 기록해두기
        start = mid + 1
print(result)