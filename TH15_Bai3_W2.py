while True:
    n = int(input("Enter n (0 < n < 10): "))
    if 0 < n < 10:
        break
factorial_of_n = 1
for i in range(1, n + 1):
    factorial_of_n *= i
print(n, "! =", factorial_of_n)
