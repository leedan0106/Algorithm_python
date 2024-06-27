arr = [0 for _ in range(26)]
str = input().rstrip()
for s in str:
  idx = ord(s) - 97
  arr[idx] += 1
print(*arr)
