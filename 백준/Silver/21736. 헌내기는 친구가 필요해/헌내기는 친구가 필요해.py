import sys
from collections import deque
input = sys.stdin.readline

def bfs():
  global count
  while queue:
    item = queue.popleft()
    i = item[0]
    j = item[1]

    for d in dir:
      new_i = i + d[0]
      new_j = j + d[1]

      if 0 <= new_i < n and 0 <= new_j < m and visited[new_i][new_j] == False:
        if campus[new_i][new_j] == "O" or campus[new_i][new_j] == "P":
          if campus[new_i][new_j] == "P":
            count += 1
          visited[new_i][new_j] = True
          queue.append((new_i, new_j))

n, m = map(int, input().split())
campus = []
for _ in range(n):
  campus.append(input().rstrip())

visited = [[False for _ in range(m)] for _ in range(n)]
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
queue = deque()
count = 0

for i in range(n):
  for j in range(m):
    if campus[i][j] == "I":
      queue.append((i, j))
      visited[i][j] = True
      bfs()
      break

print(count if count != 0 else "TT")