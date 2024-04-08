import sys
input = sys.stdin.readline

n, m = map(int, input().split())

name = set()
result = []
for _ in range(n):
  input_name = input().rstrip()
  name.add(input_name)

for _ in range(m):
  input_name = input().rstrip()
  if input_name in name:
    result.append(input_name)

result.sort()
print(len(result))
for i in range(len(result)):
  print(result[i])