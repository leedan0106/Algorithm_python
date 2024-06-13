n = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = 1
for i in range(1, n):
  max_v = 0
  for j in range(i):
    if arr[j] < arr[i] and dp[j] > max_v:
      max_v = dp[j]
  dp[i] = max_v + 1
  
print(max(dp))