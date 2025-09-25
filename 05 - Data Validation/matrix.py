from random import randint

# mat = [[1, 3, 9], [2, 2, 8], [3, 3, 7]]
# print(mat)

no_of_rows = int(input("Enter how many rows you want: "))
no_of_cols = int(input("Enter how many cols you want: "))

mat2 = [
    [randint(10, 99) for _ in range(no_of_cols)]
    for _ in range(no_of_rows)
    ]

for i in range(no_of_rows):
    for j in range(no_of_cols):
        print(mat2[i][j], end=' ')
    print()