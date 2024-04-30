import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque()
for _ in range(n):
  cmp_num = input().rstrip().split()
  cmp = cmp_num[0]
  if cmp == "push_front":
    queue.appendleft(int(cmp_num[1]))
  elif cmp == "push_back":
    queue.append(int(cmp_num[1]))
  elif cmp == "pop_front":
    if queue:
      print(queue.popleft())
    else:
      print(-1)
  elif cmp == "pop_back":
    if queue:
      print(queue.pop())
    else:
      print(-1)
  elif cmp == "size":
    print(len(queue))
  elif cmp == "empty":
    if queue:
      print(0)
    else:
      print(1)
  elif cmp == "front":
    if queue:
      print(queue[0])
    else:
      print(-1)
  elif cmp == "back":
    if queue:
      print(queue[-1])
    else:
      print(-1)
