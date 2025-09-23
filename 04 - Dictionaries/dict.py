import sys

def make_dict(IN_FILE):
    infile = open(IN_FILE, 'r', encoding='utf-8')
    my_dict = {}
    for line in infile:
        fields = line.split(';')
        name = fields[0].strip()
        nos = fields[1].strip().split(',')
        if name not in my_dict:
            my_dict[name] = nos
        else:
            my_dict[name].extend(nos)
    infile.close()
    return my_dict

def save_in_file(OUT_FILE, my_dict):
    with open(OUT_FILE, 'w', encoding='utf-8') as outfile:
        for k,v in my_dict.items():
            outfile.write(f'{k}: {v} \n')    


def main():
    PROG_FILE, IN_FILE, OUT_FILE = sys.argv

    my_dict = make_dict(IN_FILE)
    save_in_file(OUT_FILE, my_dict)

    prompt_query = "Enter user name to search: "
    prompt_404 = "The user is not available"

    # query = input(prompt_query)
    # while query != '':
    #     print (my_dict.get(query, prompt_404))
    #     query = input(prompt_query)

    while True:
        query = input(prompt_query)
        if query == '':
            break
        print (my_dict.get(query, prompt_404))




    # print(PROG_FILE, IN_FILE, OUT_FILE)

main()
