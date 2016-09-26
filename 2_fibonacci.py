def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)

sum = 0
i=1
while fib(i) <= 4000000:
    if fib(i)%2 == 0:
        sum += fib(i)
        print( i, fib(i), sum)
    i += 1

print(sum)