import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(node, cnt):
  global result, b
  visited[node] = True

  for adj in adj_arr[node]:
    if visited[adj] == False:
      if adj == b:
        result = cnt + 1
        return
      
      dfs(adj, cnt+1)


n = int(input())
a, b = map(int, input().split())
m = int(input())
adj_arr = [[] for _ in range(n+1)]
result = 0
for _ in range(m):
  x, y = map(int, input().split())
  adj_arr[x].append(y)
  adj_arr[y].append(x)

visited = [False for _ in range(n+1)]
dfs(a, 0)
if result == 0:
  print(-1)
else:
  print(result)