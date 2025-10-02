from random import randint 


class Dice:
    faces = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        
    def __init__(self, sides=6, color='white'):
        self.sides = sides
        self.color = color 
        self.face = 0

    def get_face(self):        
        return __class__.faces[self.face-1]

    def roll(self):
        self.face = randint(1, self.sides)
    
    def __add__(self, other):
        if self.get_face() == other.get_face():
            return self.get_face() + other.get_face()
        return 0
    
    def __str__(self):
        return f'I have a dice with {self.sides} sides'
    
    def __repr__(self):
        return f'This dice has {self.sides} sides with {self.color} color'



