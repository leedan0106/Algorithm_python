import sys
input = sys.stdin.readline

n = int(input())
stack = []
cnt = 1
result_arr = []
result = True
for _ in range(n):
  num = int(input())
  if not stack or stack[-1] < num:
    # num까지 스택에 넣기
    while cnt <= num:
      stack.append(cnt)
      result_arr.append("+")
      cnt += 1

  # 꺼내기
  if stack[-1] == num:
    stack.pop()
    result_arr.append("-")
  else:
    result = False

if result:
  for r in result_arr:
    print(r)
else:
  print("NO")