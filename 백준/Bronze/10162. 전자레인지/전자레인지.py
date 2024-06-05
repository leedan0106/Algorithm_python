n = int(input())

result = []
if n >= 300:
  result.append(n//300)
  n = n % 300
else:
  result.append(0)


if n >= 60:
  result.append(n // 60)
  n = n % 60
else:
  result.append(0)


if n % 10 != 0:
  result.append(-1)
else:
  result.append(n // 10)

if result[0] == -1 or result[1] == -1 or result[2] == -1:
  print(-1)
else:
  print(*result)

