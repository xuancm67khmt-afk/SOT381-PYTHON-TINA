def themaximumnumber_theminimumnumber(a, b, c):
    mx = a
    mn = a

    if b > mx:
        mx = b
    if c > mx:
        mx = c
    if b < mn:
        mn = b
    if c < mn:
        mn = c
    return mx, mn

a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
c = int(input('Enter a number: '))

max, min = themaximumnumber_theminimumnumber(a, b, c)
print('The maximum number:', max)
print('The minimum number:', min)