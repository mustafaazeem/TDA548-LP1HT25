def marks_avg(marks):
    res = 0 
    for entry in marks:
        # res = res + entry 
        res += entry 

    print(res / len(marks)) 

def main():
    # marks list contains marks of all students in assignment 1
    marks = [9, 8.5, 7.7, 10, 8, 9.9, 4.4, 10, 2, 3.6]
    # marks_avg(marks)
    print(marks)
    marks.sort()
    print(marks)

    number_of_students = len(marks)
    print(f'the total number of students is {number_of_students}')

main()