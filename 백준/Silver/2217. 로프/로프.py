n = int(input())
arr = []
for _ in range(n):
  arr.append(int(input()))

arr.sort(reverse=True)
result = 0
for i in range(n):
  temp = (i+1)*arr[i]
  if temp > result:
    result = temp

print(result)
