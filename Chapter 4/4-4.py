n, m = map(int, input().split())
x, y, direction = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

d = [[0] * m for _ in range(n)]

d[x][y] = 1  # 초기 좌표 방문 처리

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1
turn = 0
while True:
    # 왼쪽 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전 이후 정면에 가보지 않은 칸이 존재할때 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn = 0
        continue

    else:
        turn += 1

    if turn == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny

        # 뒤가 바다라서 움직임을 멈추는 경우
        else:
            break

        turn = 0

print(count)