from random import randint

class Dice:
    def __init__(self, s=6, c='white'):
        self.sides = s
        self.color = c
    
    def roll(self):
        return randint(1, self.sides)
    
    def get_sides(self):
        return self.sides
    
    def set_sides(self, s):
        self.sides = s
    

if __name__ == '__main__':
    main()