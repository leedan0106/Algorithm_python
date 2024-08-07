import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = []
for _ in range(k):
  arr.append(int(input()))

start = max(1, min(arr) // n)
end = sum(arr) // n

def check(mid):
  global n
  count = 0
  for a in arr:
    count += a // mid
  
    if count >= n:
      return True
  return False

while start <= end:
  mid = (start + end) // 2

  result = check(mid)
  if result:
    start = mid + 1
  else:
    end = mid - 1

print(end)