def the_max_number(a, b, c):
    mx = a
    if b > mx:
        mx = b
    if c > mx:
        max = c
    return mx

a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
c = int(input('Enter a number: '))

max = the_max_number(a,b,c)
print('The maximum number:', max)
