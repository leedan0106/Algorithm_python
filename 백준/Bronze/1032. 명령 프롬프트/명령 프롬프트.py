n = int(input())
str_v = input().rstrip()
check = list(str_v)
for i in range(1, n):
  temp = input().rstrip()
  for j in range(len(str_v)):
    if temp[j] != str_v[j]:
      check[j] = "?"
print(*check, sep="")
