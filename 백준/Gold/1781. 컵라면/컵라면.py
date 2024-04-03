import sys, heapq
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))

arr.sort(key=lambda x:-x[0])
cur_dedline = arr[0][0]
heap = []
result = 0

cur_idx = 0
for i in range(n, 0, -1):
  while True:
    if cur_idx < n and arr[cur_idx][0] == i:
       heapq.heappush(heap, -arr[cur_idx][1])
       cur_idx += 1
    else:
      if heap:
        result += heapq.heappop(heap)
      break

print(-result)