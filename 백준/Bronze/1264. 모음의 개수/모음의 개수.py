collection = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    count = 0
    str = input()
    if str == '#':
        break
    for s in str:
        if s in collection:
            count += 1
    print(count)