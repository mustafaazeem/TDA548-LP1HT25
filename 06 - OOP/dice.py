from random import randint 

class Dice:
    def __init__(self, sides, c):
        self.sides = sides
        self.color = c 
        self.face = 0

    def get_face(self):
        return self.face

    def roll(self):
        self.face = randint(1, self.sides)

