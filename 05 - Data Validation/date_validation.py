
def main():

    while True:
        date = input("Enter your DoB (format: yyyy-mm-dd): ")

        if date[4] != '-' and date[7] != '-':
            print("Please use proper format, enter again")
            continue
        
        try:
            dob = [ int(i) for i in date.split('-')]
        
        except ValueError:
            print("You are only allowed to enter numerical data")
            continue



        if len(dob) != 3: 
            print("You entered an incorrect date with ... ")
            continue 

    
        
        print(dob)
        break


main()