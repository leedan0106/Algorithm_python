t = int(input())
for ts in range(1, t+1):
  n = int(input())
  if n == 0:
     print("Case #" + str(ts) + ": " + "INSOMNIA")
     continue

  i = 1
  count = set()
  while i <= 10**6:
      num_str = str(n*i)
      for num in num_str:
         num = int(num)
         if 0 <= num <= 9:
            count.add(num)
      i += 1
      if len(count) == 10:
        print("Case #" + str(ts) + ": " + num_str)
        break

  if len(count) < 10:
    print("Case #" + str(ts) + ": " + "INSOMNIA")