### 반복적, 재귀적 2가지 방식으로 구현한 팩토리얼 예제

# 반복적으로 구현
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 재귀적으로 구현
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_iterative(n - 1)


print("반복적으로 구현", factorial_iterative(5))
print("재귀적으로 구현", factorial_recursive(5))
