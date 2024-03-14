#Tuliskan program yang meminta input 3 buah bilangan dan tentukan bilangan mana yang lebih besar, 2 bilangan lebih besar dari yang lain atau semua bilangan sama besar

nilai_1 = int(input("Masukkan nilai pertama: "))
nilai_2 = int(input("Masukkan nilai kedua: "))
nilai_3 = int(input("Masukkan nilai ketiga: "))

if nilai_1 >= nilai_2 and nilai_1 >= nilai_3:
    if nilai_1 == nilai_2:
        print(nilai_1, "adalah bilangan terbesar dan", nilai_1, "sama besar dengan bilangan kedua")
    elif nilai_1 == nilai_3:
        print(nilai_1, "adalah bilangan terbesar dan", nilai_1, "sama besar dengan bilangan ketiga")

if nilai_2 >= nilai_1 and nilai_2 >= nilai_3:
    if nilai_2 == nilai_3:
        print(nilai_2, "adalah bilangan terbesar dan", nilai_2, "sama besar dengan bilangan ketiga")

if nilai_3 >= nilai_2 and nilai_3 >= nilai_2:
    if nilai_3 == nilai_1:
        print(nilai_3, "adalah bilangan terbesar dan", nilai_3, "sama besar dengan bilangan pertama")

else:
    print(False)



