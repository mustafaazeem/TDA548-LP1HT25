l = [25, 18, 9, 54, 23, 86]
print(l)
print(sorted(l, key=lambda x: -x))
print(l)

l.sort(key=lambda x: -x)
print(l)

# def my_range(start, end):
#     term = start
#     while term < end:
#         yield term 
#         term += 1


# x = my_range(40, 50)

# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# for i in my_range(10, 15):
#     print (i)