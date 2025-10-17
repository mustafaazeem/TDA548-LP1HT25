from dice import Dice 
from graphics import *


def main():
    win = GraphWin("TDA548's window", 600, 600)
    win.setBackground('green')
    win.setCoords(0, 0, 10, 10)
    # cir = Circle( Point(40,40),  20)
    # cir.draw(win)

    d1 = Dice(6, 'white')    
    d2 = Dice(6, 'blue')
    for i in range(10):

        d1_face.setFace()


        d1.roll()
        d2.roll()

        d1_face = Text(Point(4,5), d1.get_face())
        d2_face = Text(Point(6,5), d2.get_face())

        d1_face.setSize(36)
        d2_face.setSize(36)

        d1_face.draw(win)
        d2_face.draw(win)
        win.getMouse()

        d1_face.undraw()
        d2_face.undraw()
    
    # d1_face = d1.get_face()
    # d2_face = d2.get_face()   

    win.getMouse()

    print(d1_face, d2_face)


if __name__ == '__main__':
    main()
