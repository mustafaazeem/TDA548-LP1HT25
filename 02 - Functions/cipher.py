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
    for i in range(m):
        if (p * i) % m == 1:
            return i

def encrypt(info, p, m):
    cipher_text = info * p % m 
    return cipher_text    

def decrypt(encrypted_info, p_inv, m):
    clear_text = encrypted_info * p_inv % m
    return clear_text

def main():
    p = -1 
    m = -1 
    info = 524

    while True:
        p = randint(1, 999)
        if is_prime(p): # if is_prime(p) == True 
            break 

    while True:
        m = randint(1000, 9999)
        if gcd(p, m) == 1:
            break

    p_inv = find_inv(p, m)

    encrypted = encrypt(info, p, m)
    print('inf: ', info)
    print('encrypted: ', encrypted)
    clear_info = decrypt(encrypted, p_inv, m)
    print("decrpted_info: ", clear_info)


    # print(f'the prime: {p}, the modulo: {m}, the inverse {p_inv}')


  



main()