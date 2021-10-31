# 부품 찾기 문제, 계수 정렬
## 모든 원소의 번호를 포함할 수 있는 크기의 리스트 만든 뒤 리스트이 인덱스에 직접 접근하여 존재하는지 확인

n = int(input())
array = [0] * 1000001
# 문제의 범위가 100만개이므로...

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")
