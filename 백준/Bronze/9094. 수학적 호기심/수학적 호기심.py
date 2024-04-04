import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  count = 0
  for i in range(1, n):
    for j in range(i+1,n):
      num = (i**2+j**2+m)/(i*j)
      if num % 1 == 0:
        count += 1
  print(count)