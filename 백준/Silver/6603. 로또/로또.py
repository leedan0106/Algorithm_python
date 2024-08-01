import sys
input = sys.stdin.readline

def rec(idx, arr, count):
  if count == 0:
    print(*arr)
    return
  
  for i in range(idx, len(lotto_num)):
    if visited[i] == 0:
      visited[i] = 1
      rec(i, arr + [lotto_num[i]], count-1)
      visited[i] = 0
  

while True:
  arr = list(map(int, input().split()))
  if arr[0] == 0:
    break

  k = arr[0]
  lotto_num = arr[1:]
  visited = [0 for _ in range(len(lotto_num))]
  rec(0, [], 6)
  print()