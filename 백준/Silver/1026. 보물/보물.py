n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(key=lambda x: -x)
result = 0
for i in range(n):
  result += a[i]*b[i]

print(result)