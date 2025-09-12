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

def encrypt_text(msg, p, m):
    msg_list = list(msg)
    encrypted_list = [] 
    print(encrypted_list)
    for i in msg_list:
        encrypted_list.append( ord(i) * p % m ) 
    
    return encrypted_list

def decrypt(encrypted_data, p_inv, m):
    clear_data = []
    for number in encrypted_data:
        clear_data.append( chr (number * p_inv % m ))

    clear_msg = ''.join(clear_data)
    print(clear_data)
    print(clear_msg)


def main():
    p = -1 
    m = -1 
    msg = "This is our Python class 2025" 
    while True:
        p = randint(1, 999)
        if is_prime(p): # if is_prime(p) == True 
            break 
    while True:
        m = randint(1000, 9999)
        if gcd(p, m) == 1:
            break

    p_inv = find_inv(p, m)
    encrypted_list = encrypt_text(msg, p, m)
    print(encrypted_list)
    decrypt(encrypted_list, p_inv, m)





main()