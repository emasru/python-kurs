def fibonacci(n):
    if n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

sum = 0
i = 0
while True:
    fib = fibonacci(i)
    if fib > 4000000:
        break
    if fib % 2 == 0:
        sum += fib
    i += 1

print(sum)

#for i in range(1, 50):
#    print(fibonacci(i))
