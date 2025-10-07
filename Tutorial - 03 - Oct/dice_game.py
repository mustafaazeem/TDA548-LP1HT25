from dice import * 

def main():
    d1 = Dice()
    d2 = Dice(8, 'red')

    print(d1.get_sides())   # print d1.sides 
    print(d2.get_sides())
    d1.set_sides(12) 
    # d1.sides = 12 
    print(d1.get_sides()) # print(d1.sides)


if __name__ == '__main__':
    main()