import sys
input = sys.stdin.readline

n = int(input())
count = 0
num = "666"
while True:
  if "666" in num:
    count += 1
    if count == n:
      print(num)
      break
  num = str(int(num) + 1)