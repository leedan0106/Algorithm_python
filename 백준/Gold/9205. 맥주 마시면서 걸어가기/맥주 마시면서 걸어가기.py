from collections import deque

ts = int(input())

def bfs():
  global visited, queue, end_x, end_y, conv_store
  while queue:
    temp = queue.popleft()
    x, y = temp[0], temp[1]

    if abs(x-end_x) + abs(y-end_y) <= 1000:
      print("happy")
      return
    
    for i in range(len(conv_store)):
      if visited[i] == 0:
        conv = conv_store[i]
        if abs(x-conv[0]) + abs(y-conv[1]) <= 1000:
          queue.append(conv)
          visited[i] = 1   

  print("sad")
  return

for _ in range(ts):
  n = int(input())

  start_x, start_y = map(int, input().split())
  conv_store = []
  for i in range(n):
    x, y = map(int, input().split())
    conv_store.append([x, y])
  end_x, end_y = map(int, input().split())

  visited = [0 for _ in range(n)]
  queue = deque()
  queue.append([start_x, start_y])
  bfs()