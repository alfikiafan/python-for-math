# Pengantar Python

## 1. Pengenalan Pemrograman

Pemrograman (_programming_) ibarat memberikan instruksi atau perintah kepada komputer untuk melakukan tugas tertentu. Bayangkan komputer itu seperti asisten yang sangat pintar, tapi dia hanya bisa melakukan apa yang kamu perintahkan secara tepat. Misalnya, jika kamu ingin asistenmu menghitung nilai matematika atau menganalisis data, kamu harus memberitahunya dengan jelas apa yang harus dilakukan.

<p align="center">
  <img src="https://storage.googleapis.com/fastwork-static/dfeb4215-792f-40a7-9f57-783a1927eb3e.jpg" alt="Ilustrasi Pemrograman" width="50%" title="Ilustrasi Pemrograman: Komputer bertindak seperti asisten yang menjalankan instruksi yang diberikan oleh programmer"/>
</p>

Di dunia matematika, pemrograman sangat berguna. Kamu bisa menggunakan kode untuk melakukan perhitungan rumit, menganalisis data besar, atau bahkan memvisualisasikan grafik. Dengan kata lain, pemrograman bisa membantu kamu mengerjakan tugas-tugas matematika yang sulit dengan lebih cepat dan efisien.

## 2. Pengenalan Python

<p align="center">
  <img src="https://i0.wp.com/junilearning.com/wp-content/uploads/2020/06/python-programming-language.webp" alt="Logo Bahasa Pemrograman Python" width="25%" title="Logo Bahasa Pemrograman Python"/>
</p>

Python adalah salah satu bahasa pemrograman yang sangat populer dan mudah dipelajari, terutama untuk pemula. Dengan sintaks yang sederhana dan kemampuan untuk menangani berbagai tugas, Python adalah pilihan yang tepat untuk mulai belajar pemrograman.

### Kenapa Python?

- Sederhana dan Mudah Dipahami, seperti menulis kalimat dalam bahasa sehari-hari.
- Kuat dan serbaguna, bisa digunakan untuk banyak hal, mulai dari perhitungan matematika hingga pembuatan AI.

## 3. Tipe Data, Variabel dan Operator

## 3.1 Tipe Data

Sebelum kita membahas lebih jauh tentang variabel, mari kita pahami terlebih dahulu apa itu tipe data. Tipe data adalah jenis data yang bisa kamu simpan dalam variabel. Di Python, ada beberapa tipe data dasar yang sering digunakan.

#### Tipe Data Dasar di Python:

- Integer (`int`): Bilangan bulat tanpa desimal. Misalnya, `10`, `-3`, `0`.
- Float (`float`): Bilangan desimal. Misalnya, `3.14`, `-0.5`, `2.0`.
- String (`str`): Teks atau rangkaian karakter. Misalnya, `"Python"`, `"123"`, `'Hello World!'`.
- Boolean (`bool`): Nilai benar atau salah, yaitu `True` atau `False`.

### 3.2 Variabel

Bayangkan variabel itu seperti kotak penyimpanan yang bisa kamu beri nama. Di dalam kotak ini, kamu bisa menyimpan berbagai jenis data, seperti angka atau teks. Tipe data menentukan jenis informasi yang bisa disimpan dalam variabel tersebut.

#### Contoh:
```python
# Mendeklarasikan variabel dengan tipe data yang berbeda
x = 10           # Kotak x berisi angka bulat (integer) 10
y = 3.14         # Kotak y berisi angka desimal (float) 3.14
name = "Fiki"    # Kotak name berisi teks (string) "Fiki"
is_active = True # Kotak is_active berisi nilai boolean True
```

Penjelasan:
- `x`, `y`, dan `name` adalah nama kotak (variabel) yang kita gunakan untuk menyimpan data. 
  - `x` menyimpan angka bulat, yang disebut sebagai `integer`.
  - `y` menyimpan angka desimal, yang disebut sebagai `float`.
  - `name` menyimpan teks, yang disebut sebagai `string`.
  - `is_active` menyimpan nilai benar atau salah, yang disebut sebagai `boolean`.

- Kamu bisa menggunakan nama yang sesuai dengan isi kotaknya. Misalnya, jika kamu ingin menyimpan nama seseorang, menggunakan nama variabel seperti `name` akan lebih masuk akal daripada menggunakan nama yang tidak relevan seperti `x` atau `y`.

### 3.3 Operator

Operator adalah simbol yang digunakan untuk melakukan operasi pada data dalam variabel. Misalnya, jika kamu ingin menjumlahkan dua angka atau membandingkan dua nilai, kamu akan menggunakan operator.

#### Contoh:
```python
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
```

Penjelasan:
- Operator aritmatika melakukan operasi matematika dasar.
- Operator pembanding digunakan untuk membandingkan dua nilai.
- Operator logika digunakan untuk menggabungkan atau membalik kondisi.

## 4. Kondisi (If-Else)

Dengan kondisi, kamu bisa membuat komputer membuat keputusan. Misalnya, kamu bisa memberi tahu komputer untuk melakukan sesuatu jika suatu kondisi tertentu terpenuhi.

### 4.1 Struktur If-Else

#### Contoh:
```python
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
```

Penjelasan:
- `if` digunakan untuk mengecek apakah suatu kondisi benar. Jika ya, maka blok kode di bawahnya akan dijalankan.
- `elif` (else if) digunakan jika kondisi pertama tidak terpenuhi dan kamu ingin mengecek kondisi lainnya.
- `else` digunakan untuk kondisi di luar `if` dan `elif`.

## 5. Loop (Pengulangan)

Loop memungkinkan kamu untuk menjalankan bagian kode berulang kali. Misalnya, jika kamu ingin menghitung total dari beberapa angka, kamu bisa menggunakan loop.

### 5.1 For Loop

For loop digunakan untuk mengulangi blok kode untuk setiap item dalam urutan.

#### Contoh:
```python
# Menghitung jumlah bilangan dari 1 hingga 5
total = 0
for i in range(1, 6):
    total += i
print("Jumlah bilangan dari 1 hingga 5 adalah:", total)
```

Penjelasan:
- `range(1, 6)` menghasilkan urutan angka dari 1 hingga 5.
- `for` loop mengulangi blok kode untuk setiap angka dalam urutan.

### 5.2 While Loop

While loop digunakan untuk mengulangi blok kode selama kondisi tertentu benar.

#### Contoh:
```python
# Menghitung faktorial dari sebuah angka menggunakan while loop
n = 5
faktorial = 1
while n > 0:
    faktorial *= n
    n -= 1
print("Faktorial dari 5 adalah:", faktorial)
```

Penjelasan:
- `while` loop terus mengulangi blok kode selama `n` lebih besar dari 0.
- Faktorial dihitung dengan mengalikan `faktorial` dengan `n` dan kemudian mengurangi `n` hingga mencapai 0.

## 6. Fungsi

Fungsi adalah cara untuk mengorganisir kode kamu dengan membuat blok kode yang bisa dipanggil berkali-kali. Ini membantu untuk membuat kode lebih bersih dan terstruktur.

### 6.1 Mendefinisikan dan Memanggil Fungsi

#### Contoh:
```python
# Mendefinisikan fungsi untuk menghitung kuadrat dari sebuah angka
def kuadrat(x):
    return x * x

# Memanggil fungsi
angka = 4
print("Kuadrat dari", angka, "adalah", kuadrat(angka))
```

Penjelasan:
- Fungsi `kuadrat` menerima satu parameter `x` dan mengembalikan `x` kuadrat.
- Kamu bisa memanggil fungsi ini dengan memberikan nilai untuk `x` dan mendapatkan hasilnya.

### 6.2 Fungsi dengan Beberapa Parameter

#### Contoh:
```python
# Fungsi untuk menghitung luas segitiga
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

# Memanggil fungsi dengan parameter
alas = 5
tinggi = 10
print("Luas segitiga dengan alas", alas, "dan tinggi", tinggi, "adalah", luas_segitiga(alas, tinggi))
```

Penjelasan:
- Fungsi `luas_segitiga` menerima dua parameter, `alas` dan `tinggi`, dan mengembalikan luas segitiga.
- Kamu bisa memanggil fungsi ini dengan memberikan nilai untuk `alas` dan `tinggi`.

## 7. Komentar

Komentar adalah catatan atau penjelasan dalam kode yang tidak dijalankan oleh komputer. Mereka berguna untuk menulis informasi atau catatan tentang kode agar lebih mudah dipahami oleh orang lain (atau diri sendiri di masa depan).

### Kenapa Komentar Penting?

- Menjelaskan Kode: Komentar bisa menjelaskan apa yang dilakukan oleh kode atau mengapa kode tersebut ditulis dengan cara tertentu.
- Memudahkan Pemeliharaan: Ketika kamu atau orang lain kembali ke kode setelah beberapa waktu, komentar bisa membantu memahami apa yang sudah dilakukan tanpa harus membaca setiap baris kode dengan teliti.

### Cara Menulis Komentar di Python

Di Python, ada dua cara untuk menulis komentar:

1. Komentar Satu Baris: Komentar ini dimulai dengan tanda `#`. Semua yang ada setelah `#` pada baris tersebut dianggap sebagai komentar dan tidak akan dieksekusi oleh Python.

   #### Contoh:
   ```python
   # Ini adalah komentar satu baris
   x = 10  # Ini juga komentar satu baris, di akhir baris kode
   ```

2. Komentar Beberapa Baris: Jika kamu perlu menulis komentar yang lebih panjang atau beberapa baris komentar, kamu bisa menggunakan tanda kutip tiga (`"""` atau `'''`) untuk membuat komentar multi-baris.

   #### Contoh:
   ```python
   """
   Ini adalah komentar beberapa baris.
   Kamu bisa menulis beberapa baris di sini untuk menjelaskan sesuatu yang lebih kompleks.
   Python akan mengabaikan semua baris ini.
   """
   x = 10
   ```

   Penjelasan:
   - Komentar ini dimulai dengan tiga tanda kutip ganda (`"""`) dan diakhiri dengan tiga tanda kutip ganda. Python akan mengabaikan semua teks di antara tanda kutip ini.

### Tips untuk Menulis Komentar

- Jangan berlebihan. Jangan terlalu banyak berkomentar. Jika kode sudah jelas, komentar yang berlebihan malah bisa membuat bingung.
- Jelaskan logika, bukan sintaks. Fokuskan komentar pada logika dan alasan di balik kode, bukan hanya menjelaskan sintaks dasar yang sudah jelas.
