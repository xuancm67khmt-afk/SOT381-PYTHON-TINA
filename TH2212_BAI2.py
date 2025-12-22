a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
c = int(input('Enter a number: '))
max = a
min = b
#Check the maximum value
if b > max:
    max = b
if c > max:
    max = c
#Check the minimum value
if a < min:
    min = b
if c < min:
    min = c
print('Maximum value: ', max)
print('Minimum value: ', min)