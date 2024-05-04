n, x = map(int, input().split())
nArr = map(int, input().split())

for num in nArr:
  if num < x:
    print(num, end=" ")