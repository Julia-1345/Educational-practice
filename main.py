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

def generate_rsa_keys():
    p = int(input('Введите простое число p: '))
    q = int(input('Введите простое число q: '))

    if not is_prime(p):
        raise ValueError(f"Число p={p} не является простым")
    if not is_prime(q):
        raise ValueError(f"Число q={q} не является простым")

    n = p * q
    print(f"Произведение n = p * q = {p} * {q} = {n}")
    phi = (p - 1) * (q - 1)
    print(f"Функция Эйлера phi(n) = (p-1)*(q-1) = {phi}")

    for candidate in range(2, phi):
        if gcd(candidate, phi) == 1:
            e = candidate
            print(f"Автоматически выбран открытый экспонент e = {e}")
            break
    else:
        raise Exception('Не удалось найти подходящий e')

    d = modinv(e, phi)
    print(f"Закрытый ключ d = {d}")

    return ((e, n), (d, n))

def rsa_encrypt(message, pubkey):
    e, n = pubkey
    ciphertext = pow(message, e, n)
    print(f"Шифротекст c = m^e mod n = {message}^{e} mod {n} = {ciphertext}")
    return ciphertext

def rsa_decrypt(ciphertext, privkey):
    d, n = privkey
    plaintext = pow(ciphertext, d, n)
    print(f"Расшифрованное сообщение m = c^d mod n = {ciphertext}^{d} mod {n} = {plaintext}")
    return plaintext

def diffie_hellman():
    p = int(input('Введите простое число p (модуль): '))
    g = int(input('Введите генератор g по модулю p: '))

    if not is_prime(p):
        raise ValueError(f"p={p} не простое, нужен простой модуль")

    a = int(input('Выберите секретное целое a (ваш приватный ключ): '))
    b = int(input('Выберите секретное целое b (секрет собеседника): '))

    A = pow(g, a, p)
    print(f"Публичный ключ A = g^a mod p = {g}^{a} mod {p} = {A}")
    B = pow(g, b, p)
    print(f"Публичный ключ B = g^b mod p = {g}^{b} mod {p} = {B}")

    shared1 = pow(B, a, p)
    print(f"Общий секрет (сторона 1) s = B^a mod p = {B}^{a} mod {p} = {shared1}")
    shared2 = pow(A, b, p)
    print(f"Общий секрет (сторона 2) s = A^b mod p = {A}^{b} mod {p} = {shared2}")

    if shared1 != shared2:
        raise Exception('Ошибка: секреты не совпадают')
    return shared1

def main():
    print('--- RSA Encryption ---')
    pubkey, privkey = generate_rsa_keys()

    m = int(input('Введите целочисленное сообщение m < n для шифрования: '))
    c = rsa_encrypt(m, pubkey)
    m2 = rsa_decrypt(c, privkey)
    print(f"Оригинал: {m}, Расшифровано: {m2}")

    print('\n--- Diffie-Hellman Key Exchange ---')
    secret = diffie_hellman()
    print(f"Успешно установлен общий секрет: {secret}")

if __name__ == '__main__':
    main()