import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

adj_list = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  adj_list[a].append(b)
  adj_list[b].append(a)

visited = [False for _ in range(n+1)]
queue = deque()

# 시작은 항상 1
visited[1] = True
queue.append([1, 0])
max_len = 0
while queue:
  item = queue.popleft()
  num = item[0]
  cnt = item[1]
  if cnt > max_len:
    max_len = cnt
  for adj in adj_list[num]:
    if visited[adj] == False:
      queue.append([adj, cnt+1])
      visited[adj] = True

result = []
visited = [False for _ in range(n+1)]
queue.append([1, 0])
visited[1] = True
while queue:
  item = queue.popleft()
  num = item[0]
  cnt = item[1]
  if cnt == max_len:
    result.append(num)
  for adj in adj_list[num]:
    if visited[adj] == False:
      queue.append([adj, cnt+1])
      visited[adj] = True

result.sort()
print(result[0], max_len, len(result))