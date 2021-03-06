## 계수 정렬 - 일반적으로 큰 데이터와 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적
## 최악의 경우에도 수행시간 O(N + K) - 여기서 N은 데이터의 갯수, K는 데이터 중 최댓값
## 직접 데이터의 값을 비교하고 위치를 변경하며 정렬하는 방식이 아님!
### 쉽게 말하면 공간을 확 늘려서! 가장 작은 데이터 ~ 가장 큰 데이터가 모두 담길 수 있게 하여 카운팅 및 정렬 진행

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1  # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):  # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=" ")  # 띄어쓰기를 구분으로 등당한 횟수만큼 인덱스 출력
