import sys
from collections import deque
input = sys.stdin.readline

def bfs():
  global w, h
  
  while queue:
    cur = queue.popleft()
    cur_i = cur[0]
    cur_j = cur[1]

    for d in dir:
      new_i = cur_i + d[0]
      new_j = cur_j + d[1]

      if 0 <= new_i < h and 0 <= new_j < w and visited[new_i][new_j] == False and arr[new_i][new_j] == 1:
        visited[new_i][new_j] = True
        queue.append([new_i, new_j])

while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  
  arr = []
  for _ in range(h):
    arr.append(list(map(int, input().split())))

  visited = [[False for _ in range(w)] for _ in range(h)]
  dir = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
  count = 0
  queue = deque()
  for i in range(h):
    for j in range(w):
      if visited[i][j] == False and arr[i][j] == 1:
        count += 1
        queue.append([i, j])
        bfs()

  print(count)