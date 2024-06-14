import sys
sys.setrecursionlimit(10**9)

def dfs(i, j, type):
  global temp
  visited[i][j] = True
  temp += 1
  for d in dir:
    new_i = i + d[0]
    new_j = j + d[1]

    if 0 <= new_i < n and 0 <= new_j < m and arr[new_i][new_j] == type and visited[new_i][new_j] == False:
      dfs(new_i, new_j, type)


m, n = map(int, input().split())
arr = []
for _ in range(n):
  arr.append(input().rstrip())


visited = [[False for _ in range(m)] for _ in range(n)]
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dic = {"W": 0, "B": 0}
for i in range(n):
  for j in range(m):
    temp = 0
    if visited[i][j] == False:
      dfs(i, j, arr[i][j])
      dic[arr[i][j]] += temp**2

print(dic["W"], dic["B"])