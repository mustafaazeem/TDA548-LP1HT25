from random import randint
def gen_list():
    return [randint(1,99) for i in range(8)]
    # data = []
    # for i in range(20):
    #     data.append( randint(100, 999) )
    # return data

def b_sort(data):
    for i in range(len(data)):      # 100
        for j in range(len(data)-1):    # 100
            if (data[j] > data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]
    return data 
      


def main():
    data = gen_list()
    print(data)
    print(b_sort(data))

main()