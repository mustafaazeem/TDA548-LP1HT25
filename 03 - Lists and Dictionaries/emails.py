with open('names.txt') as input_file:
    input_data = input_file.readlines()
    

email_list = []

for name in input_data:
    email = '.'.join(name.strip('-').split()) + '@chalmers.se'
    email_list.append(email.lower())
    print(email_list)
   

