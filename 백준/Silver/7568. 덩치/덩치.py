import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))

result = [0 for _ in range(n)]
for i in range(n):
  count = 0
  for j in range(n):
    if arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]:
      count += 1
  result[i] = count + 1
print(*result)
