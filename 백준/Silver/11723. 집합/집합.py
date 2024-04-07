import sys
input = sys.stdin.readline

m = int(input())
arr = [0 for _ in range(21)]
for _ in range(m):
  order = list(input().split())
  if order[0] == "add":
    arr[int(order[1])] = 1
  elif order[0] == "remove":
    arr[int(order[1])] = 0
  elif order[0] == "check":
    print(arr[int(order[1])])
  elif order[0] == "toggle":
    arr[int(order[1])] = 0 if arr[int(order[1])] == 1 else 1
  elif order[0] == "all":
    for i in range(1, 21):
      arr[i] = 1
  elif order[0] == "empty":
    for i in range(1, 21):
      arr[i] = 0