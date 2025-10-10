from random import randint 
# def bin_search(num, data, start, end):   
    # iterative binary search algorithm 
#     while start <= end:
#         mid = (start + end) // 2
#         if num == data[mid]:
#             return mid 
#         elif num > data[mid]:
#             start = mid + 1
#         elif num < data[mid]:
#             end = mid - 1
#     return -1 

def bin_search(elem, num_list, start, end):
    # recursive binary search algorithm 
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
    data = [ randint(1, 20) for _ in range(20) ]
    data.sort()
    num = 16
    start = 0
    end = len(data)-1
    ind = bin_search(num, data, start, end)
    print(data)
    print(f'{num} found at {ind}')
   


main()