import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
tomato_arr = []
for _ in range(n):
  tomato_arr.append(list(map(int, input().split())))

queue = deque()
tomato_cnt = 0
# 익은 토마토가 있는 위치 찾기, 전체 토마토 개수 세기
for i in range(n):
  for j in range(m):
    if tomato_arr[i][j] == 1:
      queue.append((i, j))
    if tomato_arr[i][j] == 0 or tomato_arr[i][j] == 1:
      tomato_cnt += 1

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
count = 0
day = 0
while(queue):
  queue_len = len(queue)
  day += 1
  for _ in range(queue_len):
    tomato = queue.popleft()
    count += 1
    for d in dir:
      new_i = tomato[0] + d[0]
      new_j = tomato[1] + d[1]
      if 0 <= new_i < n and 0 <= new_j < m and tomato_arr[new_i][new_j] == 0:
        queue.append((new_i, new_j))
        tomato_arr[new_i][new_j] = 1

if count != tomato_cnt:
  print(-1)
else:
  print(day-1)