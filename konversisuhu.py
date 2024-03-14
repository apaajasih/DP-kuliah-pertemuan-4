#Program untuk mengonversi suhu dari Celsius ke Fahrenheit atau sebaliknya, sesuai dengan input pengguna.

print("Pilih mode konversi:")
print("1. Celsius ke Fahrenheit")
print("2. Fahrenheit ke Celsius")

mode = int(input("Masukkan pilihan Anda (1/2): "))

if mode == 1:
    celcius = float(input("Masukkan suhu dalam Celcius: "))
    fahrenheit = (celcius * 9/5) + 32
    print(celcius,"derajat Celcius sama dengan", fahrenheit,"derajat Fahrenheit.")

elif mode == 2:
    fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
    celcius = (fahrenheit - 32) * 5/9
    print(fahrenheit,"derajat Fahrenheit sama dengan", celcius, "derajat Celcius.")

else:
    print("Pilihan tidak valid.")

