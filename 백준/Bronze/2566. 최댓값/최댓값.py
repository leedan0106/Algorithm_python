n = 9
temp = []
for i in range(n):
  temp.append(list(map(int, input().split())))

max_idx = [0, 0]
max_value = 0
for i in range(n):
  for j in range(n):
    if temp[i][j] >= max_value:
      max_value = temp[i][j]
      max_idx = [i+1, j+1]

print(max_value)
print(*max_idx)
