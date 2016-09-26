
import timeit
start_time = timeit.default_timer()
start = 20
flag = True
num = 0
while(flag):
    ind = True
    for i in range (1, 21):
        if start%i != 0:
            ind = False
            break
    if ind == True:
        flag = False
        break
    start += 20

print(start)


end_time = timeit.default_timer()
elapsed_time = end_time - start_time
print("the answer is , done in {:.5f} seconds".format( elapsed_time))