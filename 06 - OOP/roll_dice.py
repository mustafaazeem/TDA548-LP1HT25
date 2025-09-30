from dice import Dice 

def main():
    d1 = Dice(8, 'white')
    d1.roll()
    f = d1.get_face()
    print(f)
    d2 = Dice(16, 'blue')
    d2.roll() 
    g = d2.get_face()
    print(g)


if __name__ == '__main__':
    main()
