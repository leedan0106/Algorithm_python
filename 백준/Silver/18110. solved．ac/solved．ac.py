import sys
input = sys.stdin.readline

def my_round(x):
  if x - int(x) >= 0.5:
    return int(x) + 1
  elif x - int(x) < 0.5:
    return int(x)

n = int(input())
new_n = my_round(n*(15/100))

arr = []
for _ in range(n):
  arr.append(int(input()))

if n == 0:
  print(0)
else:
  arr.sort()
  new_arr = arr[new_n:n-new_n]
  print(my_round(sum(new_arr)/len(new_arr)))