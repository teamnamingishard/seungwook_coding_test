# 빠르게 입력받기
## 한 줄 입력받아 출력하는 소스코드

import sys

# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()
# 이때 rstrip()을 꼭 해줘야 하는 이유는 엔터가 줄 바꿈 기호로 입력되는데, 이 공백 문자를 제거하기 위해서임

# 입력받은 문자열 그대로 출력
print(input_data)

