n = int(input())
result = 0
for i in range(1, n+1):
  str_n = str(i)
  temp = i
  for s in str_n:
    temp += int(s)

  if temp == n:
    result = i
    break

print(result)