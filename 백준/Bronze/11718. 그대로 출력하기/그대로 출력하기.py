while True:
  try:
    str = input().rstrip()
    print(str)
  except EOFError:
    break