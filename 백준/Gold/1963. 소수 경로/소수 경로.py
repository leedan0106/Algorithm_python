from collections import deque
# 에라토스테네스의 체. 10000보다 작은 소수 다 구하기.
prime_arr = [0 for _ in range(10000)]
prime_set = set()

for i in range(2, 10000):
  if prime_arr[i] == 0:
    if i > 999 and i < 10000:
      prime_set.add(i)

    for j in range(2, 10000):
      if i*j < 10000:
        prime_arr[i*j] = 1
      else:
        break

# prime_set에 대해서 인접한 것들 구하기. 약 40가지 경우의 수 존재
# 미리 다 구해놓기.
prime_adj = dict()
for prime in prime_set:
  prime_adj[prime] = []
  prime_str = str(prime)

  # 1000자리
  for t in range(1, 10):
    t_str = str(t)
    if t_str == prime_str[0]:
      continue

    new_number = t_str + prime_str[1:]
    if int(new_number) in prime_set:
      prime_adj[prime].append(int(new_number))

  # 100자리
  for t in range(0, 10):
    t_str = str(t)
    if t_str == prime_str[1]:
      continue

    new_number = prime_str[0] + t_str + prime_str[2:]
    if int(new_number) in prime_set:
      prime_adj[prime].append(int(new_number))

  # 10자리
  for t in range(0, 10):
    t_str = str(t)
    if t_str == prime_str[2]:
      continue

    new_number = prime_str[0:2] + t_str + prime_str[3]
    if int(new_number) in prime_set:
      prime_adj[prime].append(int(new_number))

  # 1자리
  for t in range(0, 10):
    t_str = str(t)
    if t_str == prime_str[3]:
      continue

    new_number = prime_str[0:3] + t_str
    if int(new_number) in prime_set:
      prime_adj[prime].append(int(new_number))


def bfs():
  global b
  while queue:
    temp = queue.popleft()
    temp_prime = temp[0]
    count = temp[1] + 1

    for adj in prime_adj[temp_prime]:
      # print(adj)
      if adj == b:
        print(count)
        return
      
      if adj not in visited:
        # print(adj)
        visited.add(adj)
        queue.append([adj, count])

  print("Impossible")
  return

test_case = int(input())
for _ in range(test_case):
  a, b = map(int, input().split())
  count = 0
  if a == b:
    print(count)
    continue

  visited = set()
  visited.add(a)
  queue = deque()
  queue.append([a, count])
  result = bfs()