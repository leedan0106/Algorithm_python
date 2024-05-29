n, m = map(int, input().split())
arr = list(map(int, input().split()))
num = n*m
result = []
for a in arr:
  result.append(a-num)
print(*result)