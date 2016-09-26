lst = []
for i in range (100, 999):
    for j in range (100, 999):
        num = i * j
        s = str(num)
        if s == s[::-1]:

            lst.append(num)
print(max(lst))