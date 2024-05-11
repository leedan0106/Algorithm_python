import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(node):
  global max_len

  max_child = 0
  len_list = []
  for cur in child_list[node]:
    len_node = dfs(cur[0]) + cur[1]
    if len_node > max_child:
      max_child = len_node
    len_list.append(len_node)

  if len(len_list) > 1 :
    len_list.sort()  
    if len_list[-1] + len_list[-2] > max_len:
      max_len = len_list[-1] + len_list[-2]
  elif len(len_list) == 1:
    if len_list[0] > max_len:
      max_len = len_list[0]

  return max_child


n = int(input())
child_list = [[] for _ in range(n+1)]
max_len = 0
for _ in range(n-1):
  a, b, w = map(int, input().split())
  child_list[a].append([b, w])

dfs(1)
print(max_len)