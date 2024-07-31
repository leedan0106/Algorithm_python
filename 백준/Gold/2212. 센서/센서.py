n = int(input())
k = int(input())
arr = list(map(int, input().split()))
arr.sort()
diff = []
for i in range(1, len(arr)):
  dif = arr[i] - arr[i-1]
  diff.append(dif)

diff.sort()
result = sum(diff[:n-k])
print(result)