import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = max(arr)
end = 1000000000

def check(mid):
  global m
  count = 0
  sum_val = 0
  check_val = True
  for item in arr:
    if count >= m:
      check_val = False
      break

    if sum_val + item > mid:
      count += 1
      sum_val = item
    else:
      sum_val += item
  
  if sum_val > mid:
    check_val = False
  else:
    count += 1

  if check_val and count <= m:
    return True
  return False
      

while start < end:
  mid = (start + end) // 2
  result = check(mid)
  if result:
    end = mid
  else:
    start = mid + 1

print((start + end)//2)

