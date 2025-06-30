# RSA и Диффи-Хеллман на Python
# -*- coding: utf-8 -*-
import math
import random

def is_prime(n):

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            print(f"{n} делится на {i}, значит составное")
            return False
    return True

def gcd(a, b):
    """
    Находит наибольший общий делитель a и b.
    """
    while b != 0:
        a, b = b, a % b
    return a

def egcd(a, b):
    if b == 0:
        return (1, 0, a)
    else:
        x1, y1, d = egcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (x, y, d)

def modinv(e, phi):
    x, y, g = egcd(e, phi)
    if g != 1:
        raise Exception('Обратного элемента не существует, gcd != 1')
    return x % phi

def main():
    print('--- RSA Encryption ---')

    print('\n--- Diffie-Hellman Key Exchange ---')

if __name__ == '__main__':
    main()