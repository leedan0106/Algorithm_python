import sys
input = sys.stdin.readline

def my_round(number):
  integer = int(number)
  decimal = number - integer

  if number >= 0:
    if decimal >= 0.5:
      return integer + 1
    else:
      return integer
  else:
    if -decimal >= 0.5:
      return integer - 1
    else:
      return integer


n = int(input())
arr = []
count = {}
for _ in range(n):
  num = int(input())
  arr.append(num)
  if num in count:
    count[num] += 1
  else:
    count[num] = 1

# 평균
print(my_round(sum(arr)/n))


# 중앙값
arr.sort()
print(arr[n//2])

# 최빈값
many_cnt = 0
for c in count:
  if count[c] > many_cnt:
    many_cnt = count[c]

first = False
for i in range(n):
  if many_cnt == count[arr[i]]:
    if first == False:
      first = True
      many_num = arr[i]
    elif first and arr[i] != many_num:
      many_num = arr[i]
      break
print(many_num)

# 범위
print(arr[-1]-arr[0])
