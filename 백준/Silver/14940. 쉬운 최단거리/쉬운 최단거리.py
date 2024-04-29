import sys
from collections import deque
input = sys.stdin.readline

def bfs():
  while queue:
    item = queue.popleft()
    cnt = my_map[item[0]][item[1]]
    for d in dir:
      new_i = item[0] + d[0]
      new_j = item[1] + d[1]

      if 0 <= new_i < n and 0 <= new_j < m and visited[new_i][new_j] == False and my_map[new_i][new_j] == 1:
        my_map[new_i][new_j] = cnt+1
        visited[new_i][new_j] = True
        queue.append([new_i, new_j])



n, m = map(int, input().split())
my_map = []
for _ in range(n):
  my_map.append(list(map(int, input().split())))

queue = deque()
visited = [[False for _ in range(m)] for _ in range(n)]
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 2인 지점 찾기
check = False
for i in range(n):
  for j in range(m):
    if my_map[i][j] == 2:
      check = True
      my_map[i][j] = 0
      visited[i][j] = True
      queue.append([i, j])
      bfs()
      break
  if check:
    break

# 출력
for i in range(n):
  for j in range(m):
    if visited[i][j] == False and my_map[i][j] == 1:
      print(-1, end=" ")
    else:
      print(my_map[i][j], end=" ")
  print()