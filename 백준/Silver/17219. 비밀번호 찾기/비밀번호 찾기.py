import sys
input = sys.stdin.readline

n, m = map(int, input().split())
site_dic = {}
for _ in range(n):
  site = list(input().rstrip().split())
  site_dic[site[0]] = site[1]

for _ in range(m):
  site_name = input().rstrip()
  print(site_dic[site_name])