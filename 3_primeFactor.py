from cmath import sqrt


def primeFactor (n):
    f = True
    for i in range (2, int(n/2)+1):
        if n % i == 0:
            f = False
    return f

dig = 600851475143
largest = 1
for i in range (2, int(sqrt(dig)) + 1):
    if dig % i == 0 and primeFactor(i):
        largest = i
        print(largest)

print (largest)