import sys
input = sys.stdin.readline

n = int(input())
student = []
for _ in range(n):
  std = input().rstrip().split()
  student.append([std[0], int(std[1]), int(std[2]), int(std[3])])

student.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for s in student:
  print(s[0])
