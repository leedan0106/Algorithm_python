n = int(input())
card = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

card_set = set()
for c in card:
  card_set.add(c)

for num in nums:
  print(1 if num in card_set else 0, end=" ")
