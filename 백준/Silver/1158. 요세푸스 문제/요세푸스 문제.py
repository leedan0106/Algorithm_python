import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque([i for i in range(1, n+1)])
result = []
cnt = 1
while queue:
  if cnt < k:
    cnt += 1
    queue.append(queue.popleft())
  else:
    result.append(queue.popleft())
    cnt = 1

print("<", end="")
print(*result, sep=', ', end="")
print(">")
