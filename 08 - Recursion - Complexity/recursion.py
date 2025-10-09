import time 
from random import randint
def lin_search(elem, num_list):
    for i in range(len(num_list)):
        if elem == num_list[i]:
            return i
    return -1

def bin_search(elem, num_list, start, end):
    mid = (start + end) // 2
    if start > end:
        return -1 
    if elem == num_list[mid]:
        return mid
    elif elem > num_list[mid]:  
        # start = mid 
        return bin_search(elem, num_list, mid+1, end)
    elif elem < num_list[mid]: 
        # end = mid 
        return bin_search(elem, num_list, start, mid-1)


def main():
    my_list = [
        randint(1, 1_000_000) 
        for _ in range(1_000_000)
    ]
    elem = 980524
    start = time.process_time()
    for _ in range(100):
        ind = lin_search(elem, my_list)
    end = time.process_time()
    print('linear: ', start, end, end-start)

    my_list.sort()

    start = time.process_time()
    for _ in range(1_000_000):
        ind2 = bin_search(elem, my_list, 0, len(my_list))
    end = time.process_time()
    print('binary: ', start, end, end-start)






main()








def fac(n):
    # iterative factorial algorithm 
    res = 1
    for i in range(1, n+1):
        res *= i
    return res 

def fac2(n):
    # recursive factorial algorithm 
    if n == 1:
        return 1
    return n * fac2(n-1)


def main2():
    start = time.process_time()
    for _ in range(100000):
        res = fac(50)
    end = time.process_time()

    print('iterative: ', start, end, end-start)

    start = time.process_time()
    for _ in range(100000):
        res = fac2(50)
    end = time.process_time()

    print('recurive: ', start, end, end-start)

