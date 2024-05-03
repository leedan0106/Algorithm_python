import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
  global max_distance
  queue = deque()
  visited = [[False for _ in range(m)] for _ in range(n)]

  queue.append([i, j, 0])
  visited[i][j] = True

  while queue:
    cur = queue.popleft()
    
    for d in dir:
      new_i = cur[0] + d[0]
      new_j = cur[1] + d[1]
      new_cnt = cur[2]+1

      if 0 <= new_i < n and 0 <= new_j < m and visited[new_i][new_j] == False and arr[new_i][new_j] == "L":
        visited[new_i][new_j] = True
        queue.append([new_i, new_j, new_cnt])
        max_distance = new_cnt


n, m = map(int, input().split())
arr = []
for _ in range(n):
  arr.append(input().rstrip())

result = []
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for i in range(n):
  for j in range(m):
    if arr[i][j] == "L":
      max_distance = 0
      bfs(i, j)
      # print(max_distance)
      result.append(max_distance)

print(max(result))