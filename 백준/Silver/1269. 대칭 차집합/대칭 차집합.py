n, m = map(int, input().split())
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))

result = 0
for a_v in a:
  if a_v not in b:
    result += 1

for b_v in b:
  if b_v not in a:
    result += 1
print(result) 