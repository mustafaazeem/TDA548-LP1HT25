# '''This program helps you calculate 
# your salary depending upon your 
# current tax rate '''



for i in range(5):

    gross_salary = int( input(f'Please enter your salary for person {i}: ') )   # int (100,000)
    tax_rate = int(input('enter your tax rate: '))

    tax_amount = gross_salary * tax_rate / 100 
    net_salary = gross_salary - tax_amount

    print("your tax amount is ", tax_amount)
    print("your net salary is ", net_salary)

print("After loop")