import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
  person = list(input().split())
  arr.append([int(person[0]), i, person[1]])

arr.sort()
for a in arr:
  print(a[0], a[2])