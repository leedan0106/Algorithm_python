n = int(input())
if n != 1:
  num = 2
  result = []
  while n > 1:
    if n % num == 0:
      n = n // num
      print(num)
      num = 2
    else:
      num += 1
