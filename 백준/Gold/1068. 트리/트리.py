import sys
input = sys.stdin.readline

def dfs(node):
  global count

  if node == remove_node:
    return

  if len(child[node]) == 0:
    count += 1
    return
  
  for adj in child[node]:
    if adj == remove_node and len(child[node]) == 1:
      count += 1
      break
    dfs(adj)


n = int(input())
node_parent = list(map(int, input().split()))
child = [[] for _ in range(n)]
remove_node = int(input())

for i in range(n):
  if node_parent[i] == -1:
    root = i
  else:
    child[node_parent[i]].append(i)

count = 0
dfs(root)
print(count)