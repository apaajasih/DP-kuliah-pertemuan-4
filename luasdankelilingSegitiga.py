#Buatlah program yang menghitung luas dan keliling segitiga berdasarkan panjang sisi-sisinya. (Gunakan Rumus Heron)

import math

def input_sisi():
    a = float(input("Masukkan panjang sisi a: "))
    b = float(input("Masukkan panjang sisi b: "))
    c = float(input("Masukkan panjang sisi c: "))
    return a, b, c

def luas_segitiga(a, b, c):
    s = (a + b + c) / 2
    luas = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return luas

def keliling_segitiga(a, b, c):
    keliling = a + b + c
    return keliling

def main():
    a, b, c = input_sisi()
    luas = luas_segitiga(a, b, c)
    keliling = keliling_segitiga(a, b, c)
    print("Luas segitiga: ", luas)
    print("Keliling segitiga: ", keliling)

print(main())