max_score = 0
max_index = 0
for i in range(5):
  score = list(map(int, input().split()))
  score_temp = sum(score)
  if score_temp > max_score:
    max_index = i+1
    max_score = score_temp

print(max_index, max_score)