n = int(input( 'Enter a number: ' ))
sum = 0
for i in range(1, 1-n):
    if n % 2 == 0 and n % 3 == 0:
      sum += i
      print('The sum of the numbers divisible by both 2 and 3 is:', sum)   