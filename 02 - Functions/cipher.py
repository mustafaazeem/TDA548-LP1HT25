from random import randint 
def is_prime(p):
    if p <= 1:
        return False 
    elif p == 2 or p == 3:
        return True
    n = 2
    while n < p/2:
        if (p % n) == 0:            
            return False
        n = n + 1 
    return True 

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a 

def find_inv(p, m):
    p_inv = 1 
    while 
def main():
    p = -1 
    m = -1 
    while True:
        p = randint(1, 999)
        if is_prime(p):
            break 
    m = randint(1000, 9999)

    print(f'the prime you got is {p}, and m you got is {m}')
  


main()