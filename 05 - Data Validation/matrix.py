
def mul_matrix(m1, m2): 
    # we need to check dimensions 
    # if
    # elif 

    mat = [
        [
           ( sum(a*b) for a,b in zip(row, col))
           
            for col in zip(*m2)
        ]
        for row in m1
    ]


    
def add_matrix(m1, m2):
    if len(m1) != len(m2):
        return False 
    elif len(m1[0] != len(m2[0])):
        return None 
    else:
        mat = [
            [ a+b for a,b in zip(row_m1, row_m2)]
            for row_m1, row_m2 in zip(m1, m2)
        ]
        return mat
    # mat = []
    # for i in range(len(m1)):
    #     for j in range(len(m1[0])):
    #         mat.append()


def main():
    m1 = [ [1,2,3,4], [5,6,7,8], [9,1,0,1] ]
    m2 = [ [9,8,7,6], [5,4,3,2] ] #, [1,0,9,8] ] 

    # for i in range(len(m1)):
    #     print(m1[i], '\t', m2[i])

    print('\n')
    m3 = add_matrix(m1, m2)
    # m3 = m1 + m2
    for i in range(len(m3)):
        print(m3[i])

if __name__ == '__main__':
    main()