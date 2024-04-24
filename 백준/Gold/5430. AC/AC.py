import sys
from collections import deque
input = sys.stdin.readline

def arr_print(queue):
  string = "["
  for i in range(len(queue)):
    string += str(queue[i]) + ("," if i < len(queue) -1 else "")
  string += "]"
  print(string)

test_case = int(input())

for _ in range(test_case):
  cmd_arr = input().rstrip()
  n = int(input())
  arr = input().rstrip()
  arr = eval(arr)
  queue = deque(arr) # 배열 형태의 스트링을 배열로 변경. eval. 수식읽는 함수

  is_reverse = False
  is_error = False
  for cmd in cmd_arr:  
    if cmd == "R":
      is_reverse = not is_reverse
    else:
      if queue:
        if is_reverse:
          queue.pop()
        else:
          queue.popleft()
      else:
        is_error = True
        break
  if is_error:
    print("error")
  else:
    if is_reverse:
      arr_print(list(queue)[::-1])
    else:
      arr_print(queue)