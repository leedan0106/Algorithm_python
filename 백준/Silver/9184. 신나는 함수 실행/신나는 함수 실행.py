import sys
input = sys.stdin.readline

dp = [[[0 for _ in range(51)] for _ in range(51)] for _ in range(51)] # a, b, c
dp[0][0][0] = 1
def w(a, b, c):
  if a <= 0 or b <= 0 or c <= 0:
    return 1
  
  
  if a > 20 or b > 20 or c > 20:
    dp[a][b][c] = dp[20][20][20] if dp[20][20][20] != 0 else w(20, 20, 20)
  
  elif a < b and b < c:
    temp1= dp[a][b][c-1] if dp[a][b][c-1] != 0 else w(a, b, c-1)
    temp2 = dp[a][b-1][c-1] if dp[a][b-1][c-1] != 0 else w(a, b-1, c-1)
    temp3 = dp[a][b-1][c] if dp[a][b-1][c] != 0 else w(a, b-1, c)
    dp[a][b][c] = temp1 + temp2 - temp3


  else:
    temp1= dp[a-1][b][c] if dp[a-1][b][c] != 0 else w(a-1, b, c)
    temp2 = dp[a-1][b-1][c] if dp[a-1][b-1][c] != 0 else w(a-1, b-1, c)
    temp3 = dp[a-1][b][c-1] if dp[a-1][b][c-1] != 0 else w(a-1, b, c-1)
    temp4 = dp[a-1][b-1][c-1] if dp[a-1][b-1][c-1] != 0 else w(a-1, b-1, c-1)
    
    dp[a][b][c] = temp1 + temp2 + temp3 - temp4
  
  return dp[a][b][c]
  
while True:
  a, b, c= map(int, input().split())
  if a == -1 and b == -1 and c == -1:
    break
  
  print("w(" + str(a) +  ", " + str(b) +", "+ str(c)+") = ", end = "")
  if a <= 0 or b <= 0 or c <= 0:
    print(1)
  else:
    print(w(a, b, c))