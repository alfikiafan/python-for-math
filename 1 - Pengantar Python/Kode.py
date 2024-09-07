# Mendeklarasikan variabel dengan tipe data yang berbeda
x = 10           # Kotak x berisi angka bulat (integer) 10
y = 3.14         # Kotak y berisi angka desimal (float) 3.14
name = "Fiki"    # Kotak name berisi teks (string) "Fiki"
is_active = True # Kotak is_active berisi nilai boolean True

# Operator Aritmatika
a = 5
b = 2
print(a + b)  # Menjumlahkan 5 dan 2, hasilnya 7
print(a - b)  # Mengurangi 5 dengan 2, hasilnya 3
print(a * b)  # Mengalikan 5 dengan 2, hasilnya 10
print(a / b)  # Membagi 5 dengan 2, hasilnya 2.5
print(a // b) # Pembagian bulat 5 dibagi 2, hasilnya 2
print(a % b)  # Sisa pembagian 5 dengan 2, hasilnya 1
print(a ** b) # 5 dipangkatkan 2, hasilnya 25

# Operator Pembanding
print(a == b) # Apakah 5 sama dengan 2? Hasilnya False
print(a != b) # Apakah 5 tidak sama dengan 2? Hasilnya True
print(a > b)  # Apakah 5 lebih besar dari 2? Hasilnya True
print(a < b)  # Apakah 5 lebih kecil dari 2? Hasilnya False

# Operator Logika
x = True
y = False
print(x and y) # Apakah x dan y keduanya True? Hasilnya False
print(x or y)  # Apakah x atau y salah satunya True? Hasilnya True
print(not x)   # Negasi dari x, hasilnya False

# Program menentukan jenis segitiga
a = 3
b = 4
c = 5

if a == b == c:
    print("Segitiga sama sisi")
elif a == b or b == c or a == c:
    print("Segitiga sama kaki")
else:
    print("Segitiga sembarang")

# Menghitung jumlah bilangan dari 1 hingga 5
total = 0
for i in range(1, 6):
    print(i)
    total += i
print("Jumlah bilangan dari 1 hingga 5 adalah:", total)

# Menghitung faktorial dari sebuah angka menggunakan while loop
n = 5
faktorial = 1
while n > 0:
    faktorial *= n
    n -= 1
print("Faktorial dari 5 adalah:", faktorial)

# Mendefinisikan fungsi untuk menghitung kuadrat dari sebuah angka
def kuadrat(x):
    return x * x

# Memanggil fungsi
angka = 4
print("Kuadrat dari", angka, "adalah", kuadrat(angka))

# Fungsi untuk menghitung luas segitiga
def luas_segitiga(alas, tinggi):
    return int(0.5 * alas * tinggi)

# Memanggil fungsi dengan parameter
alas = 5
tinggi = 10
print("Luas segitiga dengan alas", alas, "dan tinggi", tinggi, "adalah", luas_segitiga(alas, tinggi))