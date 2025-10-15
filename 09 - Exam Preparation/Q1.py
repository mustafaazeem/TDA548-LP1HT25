from math import pi, sqrt 
# import math 
M = 1.991e30 
G = 6.67e-11
RADIUS = {
    "mercury": 57.9e9,
    "venus": 108.2e9,
    "earth": 149.6e9,
    "mars": 228e9,
    "jupiter": 779.3e9,
    "saturn": 1427e9,
    "uranus": 2871e9,
    "neptune": 4497e9,
    "pluto": 5913e9
}

def planet_period(name):
    # T_squared = ((4*pi**2) / (G*M)) * RADIUS[name]**3
    # return sqrt(T_squared) / (24 * 60 * 60)
    return sqrt ( ((4*pi**2) / (G*M)) * RADIUS[name]**3 ) / (24 * 60 * 60)

def main():
    while True:
        planet = input("Please enter planet name, or 'exit': ")
        if planet in RADIUS:
            print(planet_period(planet))
        elif planet == 'exit':
            print('Exiting the program ...')
            break
        else:
            print('you entered an incorrect choice, please enter again: ')
            

main()