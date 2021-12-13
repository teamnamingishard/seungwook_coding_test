N = int(input())
conference_time = [tuple(map(int, input().split())) for _ in range(N)]

# 시작 시간을 기준으로 정렬 + 마감 시간을 기준으로 정렬
conference_time = sorted(conference_time, key=lambda a: a[0])
conference_time = sorted(conference_time, key=lambda a: a[1])

count = 0
start_time = 0

for time in conference_time:
  if time[0] >= start_time:
    start_time = time[1]
    count += 1

print(count)