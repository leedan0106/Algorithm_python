import sys
input = sys.stdin.readline
str = list(input().rstrip())
n = int(input())
stack = []
for _ in range(n):
  cmd = input().rstrip().split()

  if cmd[0] == "L":
    if len(str) > 0:
      stack.append(str.pop())
  elif cmd[0] == "D":
    if len(stack) > 0:
      str.append(stack.pop())
  elif cmd[0] == "B":
    if len(str) > 0:
      str.pop()
  elif cmd[0] == "P":
    str.append(cmd[1])

print(*(str + stack[::-1]), sep="")