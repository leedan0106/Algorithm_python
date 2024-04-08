import sys
input = sys.stdin.readline

n, m = map(int, input().split())
name_arr = ["" for _ in range(n+1)]
name_dic = {}
for i in range(1, n+1):
  name = input().rstrip()
  name_arr[i] = name
  name_dic[name] = i

for _ in range(m):
  name = input().rstrip()
  if name.isdigit():
    print(name_arr[int(name)])
  else:
    print(name_dic[name])