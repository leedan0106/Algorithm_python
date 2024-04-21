import sys
from collections import deque
input = sys.stdin.readline
MAX = 100000

n, k = map(int, input().split())

queue = deque()
visited = [False for _ in range(MAX+1)]

queue.append([n, 0])
while queue:
  cur = queue.popleft()
  x = cur[0]
  t = cur[1]
  visited[x] = True
  
  if x == k:
    count = 1
    while queue:
      temp = queue.popleft()
      if temp[1] != t:
        break

      if temp[0] == k:
        count += 1
    print(t)
    print(count)
    break

  if 0 <= x-1 <= MAX and visited[x-1] == False:
    queue.append([x-1, t+1])

  if 0 <= x+1 <= MAX and visited[x+1] == False:
    queue.append([x+1, t+1])

  if 0 <= x*2 <= MAX and visited[x*2] == False:
    queue.append([x*2, t+1])