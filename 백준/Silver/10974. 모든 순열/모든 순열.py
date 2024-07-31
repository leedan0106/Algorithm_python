import sys
input = sys.stdin.readline

n = int(input())
check = [0 for _ in range(n+1)]

def rec(count, arr):
  if count == 0:
    print(*arr)
    return
  
  for i in range(1, n+1):
    if check[i] == 0:
      check[i] = 1
      rec(count-1, arr + [i])
      check[i] = 0

rec(n, [])