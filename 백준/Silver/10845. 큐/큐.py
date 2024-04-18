import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

queue = deque()
for _ in range(n):
  cmd_num = list(input().split())
  cmd = cmd_num[0]
  if cmd == "push":
    num = cmd_num[1]
    queue.append(num)
  elif cmd == "pop":
    if queue:
      print(queue.popleft())
    else:
      print(-1)
  elif cmd == "size":
    print(len(queue))
  elif cmd == "empty":
    if queue:
      print(0)
    else:
      print(1)
  elif cmd == "front":
    if queue:
      print(queue[0])
    else:
      print(-1)
  elif cmd == "back":
    if queue:
      print(queue[-1])
    else:
      print(-1)