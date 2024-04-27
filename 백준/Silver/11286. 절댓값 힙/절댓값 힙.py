import sys, heapq
input = sys.stdin.readline

minus_queue = []
plus_queue = []

n = int(input())
for _ in range(n):
  x = int(input())
  if x == 0:
    if plus_queue and minus_queue:
      if plus_queue[0] < minus_queue[0]:
        print(heapq.heappop(plus_queue))
      else:
        print(-heapq.heappop(minus_queue))
    elif not plus_queue and minus_queue:
        print(-heapq.heappop(minus_queue))
    elif plus_queue and not minus_queue:
        print(heapq.heappop(plus_queue))
    else:
      print(0)

  else:
    if x > 0:
      heapq.heappush(plus_queue, x)
    else:
      heapq.heappush(minus_queue, -x)