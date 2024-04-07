import sys
input = sys.stdin.readline

while True:
  abc = list(map(int, input().split()))
  if sum(abc) == 0:
    break
  abc.sort()
  if abc[0]**2 + abc[1]**2 == abc[2]**2:
    print("right")    
  else:
    print("wrong")