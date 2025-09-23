import json 
from constants import *

def write_to_file(file, my_dict):
    # data = json.dumps(my_dict)
    # print(data)

    with open(file, 'w') as out_file:
        json.dump(my_dict, out_file)


def display_dictionary(my_dict):
    for k,v in my_dict.items():
        print(f'name is {k}, and the phone is {v}')

def del_from_dict(my_dict, key):
    my_dict.pop(key)
 
def add_to_dict(my_dict, k, v):
    my_dict[k] = v

def main():
    phone_dict = { "Mustafa" : '076 523 41 44',
                  "William" : '031 524 85 85',
                  "Kareem" : "031 521 36 25"  } 
    
    write_to_file(OUT_FILE, phone_dict)
    



    # display_dictionary(phone_dict)
    # del_from_dict(phone_dict, 'Kareem')
    # add_to_dict(phone_dict, 'John', '052 12 1365')
    # display_dictionary(phone_dict)
    # add_to_dict(phone_dict, 'Mustafa', '000011110000')
    # display_dictionary(phone_dict)

 

main()