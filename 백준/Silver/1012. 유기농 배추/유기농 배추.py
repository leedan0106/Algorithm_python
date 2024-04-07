import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

t = int(input())
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def dfs(i, j):
  visited[i][j] = True

  for d in dir:
    new_i = i + d[0]
    new_j = j + d[1]
    if 0 <= new_i < m and 0 <= new_j < n and visited[new_i][new_j] == False and mat[new_i][new_j] == 1:
      dfs(new_i, new_j)

for _ in range(t):
  m, n, k = map(int, input().split())
  mat = [[0 for _ in range(n)] for _ in range(m)]
  for _ in range(k):
    a, b = map(int, input().split())
    mat[a][b] = 1

  visited = [[False for _ in range(n)] for _ in range(m)]
  count = 0
  for i in range(m):
    for j in range(n):
      if mat[i][j] == 1 and visited[i][j] == False:
        count += 1
        dfs(i, j)

  print(count)