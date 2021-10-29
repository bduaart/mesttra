a, b, c = map(int,input().split())

if a > b and a > c:
    if b > c:
        print(f'{c}\n{b}\n{a}\n')
    else:
        print(f'{b}\n{c}\n{a}\n')
elif b > a and b > c:
    if a > c:
        print(f'{c}\n{a}\n{b}\n')
    else:
        print(f'{a}\n{c}\n{b}\n')
elif c > a and c > b:
    if a > b:
        print(f'{b}\n{a}\n{c}\n')
    else:
        print(f'{a}\n{b}\n{c}\n')
print(f'{a}\n{b}\n{c}')
