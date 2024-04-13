import sys, heapq
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr_set = list(set(arr))

heap = []
for a in arr_set:
  heapq.heappush(heap, a)

result_dic = {}
for i in range(len(arr_set)):
  num = heapq.heappop(heap)
  result_dic[num] = i

for a in arr:
  print(result_dic[a], end=" ")