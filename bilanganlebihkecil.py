
#Tulisan program yang meminta input 3 buah bilangan dan tentukan bilangan mana yang lebih kecil

nilai_1 = int(input("Masukkan nilai pertama: "))
nilai_2 = int(input("Masukkan nilai kedua: "))
nilai_3 = int(input("Masukkan nilai ketiga: "))

if nilai_1 < nilai_2 and nilai_1 < nilai_3:
    print(nilai_1, "lebih kecil dari", nilai_2, "dan", nilai_3)
elif nilai_2 < nilai_1 and nilai_2 < nilai_3:
    print(nilai_2, "lebih kecil dari", nilai_1, "dan", nilai_3)
else:
    print(nilai_3, "lebiih kecil dari", nilai_1, "dan", nilai_2)
