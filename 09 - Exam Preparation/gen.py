def file_gen(fname):
    with open(fname) as infile:
        for line in infile:
            yield line # return line 

def main():
    fname = 'data.txt'

    # calling return function 
    # file_gen(fname)

    # line_generator = file_gen(fname)

    for next in file_gen(fname):
        print(next)

    # print( next (line_generator) )

    # print( next (line_generator) )


main()

