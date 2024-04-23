import sys
from collections import deque
input = sys.stdin.readline

MAX = 1000000001

a, b = map(int, input().split())
queue = deque()
visited = set()

queue.append([a, 1])
visited.add(a)

check = False
while queue:
  cur = queue.popleft()
  if cur[0] == b:
    print(cur[1])
    check = True
    break

  new_a = cur[0]*2
  if new_a < MAX and new_a not in visited:
    visited.add(new_a)
    queue.append([new_a, cur[1]+1])

  new_a = cur[0]*10 + 1
  if new_a < MAX and new_a not in visited:
    visited.add(new_a)
    queue.append([new_a, cur[1]+1])

if check == False:
  print(-1)