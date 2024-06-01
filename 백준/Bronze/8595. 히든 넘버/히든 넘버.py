n = int(input())
str = input().rstrip()
result = 0
temp = ""
for s in str:
  if s.isdecimal():
    temp += s
  else:
    if temp != "":
      result += int(temp)
      temp = ""

if temp!= "":
  result += int(temp)
print(result)
