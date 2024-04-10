import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  dic = {}
  for _ in range(n):
    name, type = list(input().split())
    if dic.get(type) != None:
      dic[type] += 1
    else:
      dic[type] = 1

  result = 1
  for key in dic:
    result *= (dic[key]+1)

  print(result - 1)