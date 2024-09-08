# Pemrograman Berorientasi Objek (OOP) – Class dan Object

## 1. Pengantar OOP

Halo teman-teman! Selamat datang di materi Pemrograman Berorientasi Objek atau dalam bahasa Inggris disebut dengan Object Oriented Programming (OOP). Nah, kalian mungkin bertanya, **OOP itu apa sih?** OOP adalah cara kita memikirkan program sebagai kumpulan objek yang saling berinteraksi. Berbeda dengan pemrograman prosedural yang cenderung fokus pada rangkaian langkah atau instruksi, OOP lebih fokus pada objek-objek yang "hidup" dalam program kita.

Di sini kita akan belajar bagaimana membuat objek-objek itu menggunakan **class** dan bagaimana objek-objek itu dapat berinteraksi. Seru kan? Yuk, kita mulai dengan memahami dua hal penting: **class** dan **object**.

---

## 2. Class dan Object: Definisi Dasar

Oke, langsung aja! Dalam OOP, **class** adalah seperti cetak biru (_blueprint_) dari suatu benda. Misalnya, kalian bisa bayangkan class itu seperti _blueprint_ mobil. Dari _blueprint_ ini, kita bisa bikin banyak mobil yang berbeda-beda. Mobil-mobil yang kita buat dari _blueprint_ ini kita sebut sebagai **object**.

Jadi, intinya:
- **Class**: Blueprint atau rancangannya.
- **Object**: Barang hasil dari blueprint tersebut, yang "hidup" di dalam program.

### Contoh Class dan Object di Python

```python
class Mobil:
    # ini adalah class yang menggambarkan sebuah mobil
    pass  # untuk sekarang, class ini kosong dulu

# kita buat object dari class Mobil
mobil1 = Mobil()
mobil2 = Mobil()

print(mobil1)
print(mobil2)
```

Kalian bisa lihat, kita sudah bikin dua object `mobil1` dan `mobil2` dari class `Mobil`. Mereka berbeda, tapi berasal dari blueprint yang sama!

---

## 3. Membuat Class di Python

Sekarang, yuk kita mulai mengisi class kita dengan atribut dan metode (fungsi-fungsi yang bisa dipakai oleh objek).

### Atribut dan Metode
Dalam class, kita bisa punya **atribut**, yang menggambarkan sifat-sifat dari object, dan **metode**, yaitu fungsi yang bisa dijalankan oleh object.

Misalnya, class `Mobil` bisa punya atribut seperti warna, merek, dan kecepatan, serta metode untuk menjalankan atau menghentikan mobil.

### Membuat Constructor dengan `__init__`
Constructor adalah fungsi khusus dalam class yang otomatis dipanggil saat object baru dibuat. Biasanya kita menggunakannya untuk mengatur atribut-atribut awal.

```python
class Mobil:
    # constructor __init__ untuk menginisialisasi object baru
    def __init__(self, merek, warna):
        self.merek = merek  # atribut merek
        self.warna = warna  # atribut warna
    
    # metode untuk menjalankan mobil
    def jalankan(self):
        print(f"Mobil {self.merek} berwarna {self.warna} sedang berjalan.")
    
    # metode untuk menghentikan mobil
    def berhenti(self):
        print(f"Mobil {self.merek} berhenti.")

# membuat object mobil baru
mobil1 = Mobil("Toyota", "Merah")
mobil2 = Mobil("Honda", "Hitam")

# menggunakan metode dari object
mobil1.jalankan()  # Mobil Toyota berwarna Merah sedang berjalan.
mobil2.berhenti()  # Mobil Honda berhenti.
```

### Apa itu `self`?
Kalian pasti bertanya-tanya, **apa sih `self` itu?** Singkatnya, `self` merujuk pada object itu sendiri. Jadi setiap kali kita membuat object baru, `self` akan "mengikat" object tersebut ke atribut dan metode di dalam class.

Sebagai contoh:
- `self.merek` merujuk ke atribut `merek` milik object yang spesifik (misal, `mobil1` atau `mobil2`).
- `self.jalankan()` berarti kita memanggil metode `jalankan` untuk object yang spesifik.

Baik, mari kita lanjutkan materi tentang cara membuat object dari class dan bagaimana cara mengakses atribut serta metode pada object.

---

## 4. Membuat Object dari Class

Setelah kita punya **class** dengan atribut dan metode, saatnya kita membuat object dari class tersebut. Ini disebut dengan **instansiasi**, yaitu proses pembuatan object dari sebuah class.

### Contoh Instansiasi Object

Mari kita ambil contoh class `Mobil` yang sudah kita buat sebelumnya. Kita akan membuat beberapa mobil baru dari class tersebut.

```python
class Mobil:
    def __init__(self, merek, warna):
        self.merek = merek
        self.warna = warna
    
    def jalankan(self):
        print(f"Mobil {self.merek} berwarna {self.warna} sedang berjalan.")
    
    def berhenti(self):
        print(f"Mobil {self.merek} berhenti.")

# instansiasi object dari class Mobil
mobil1 = Mobil("Toyota", "Merah")
mobil2 = Mobil("Honda", "Hitam")

print(mobil1)  # akan mencetak <__main__.Mobil object at ...>
```

Sekarang, `mobil1` dan `mobil2` adalah dua object berbeda yang berasal dari class `Mobil`. Mereka punya atribut yang berbeda (merek dan warna), tapi keduanya bisa melakukan hal yang sama, seperti `jalankan` dan `berhenti`.

---

## 5. Atribut dan Metode pada Object

Setelah kita punya object, kita bisa **mengakses atribut** dan **menggunakan metode** yang ada di dalam class tersebut. Berikut adalah cara mengakses atribut dan metode dari object.

### Mengakses Atribut Object

Atribut dari sebuah object bisa diakses dengan menggunakan notasi titik (`.`). Misalnya, kita ingin melihat merek dan warna dari `mobil1`.

```python
print(mobil1.merek)  # Output: Toyota
print(mobil1.warna)  # Output: Merah
```

### Memanggil Metode pada Object

Selain atribut, kita juga bisa memanggil metode yang ada di dalam class. Seperti ini:

```python
mobil1.jalankan()  # Output: Mobil Toyota berwarna Merah sedang berjalan.
mobil2.berhenti()  # Output: Mobil Honda berhenti.
```

Di sini, metode `jalankan()` dipanggil untuk `mobil1`, dan metode `berhenti()` dipanggil untuk `mobil2`. Karena mereka adalah object yang berbeda, hasilnya juga spesifik untuk masing-masing object.

---

Saat kita membuat object dari sebuah class, kita bisa memodifikasi atribut object tersebut setelah object dibuat. Yuk kita bahas bagaimana caranya!

### Menambah Atribut Object

Kita bisa menambahkan atribut baru ke object setelah object tersebut dibuat. Misalnya, kita ingin menambahkan atribut baru `tahun` pada object `mobil1` yang belum ada sebelumnya.

```python
mobil1.tahun = 2023  # menambah atribut baru
print(mobil1.tahun)  # Output: 2023
```

### Mengubah Atribut Object

Atribut yang sudah ada bisa diubah dengan cara yang sama seperti menambah atribut. Misalnya, kita ingin mengubah warna mobil dari `Merah` menjadi `Putih`.

```python
mobil1.warna = "Putih"  # mengubah atribut warna
print(mobil1.warna)  # Output: Putih
```

### Menghapus Atribut Object

Kita juga bisa menghapus atribut dari object dengan menggunakan kata kunci `del`. Misalnya, kita ingin menghapus atribut `tahun` dari `mobil1`.

```python
del mobil1.tahun  # menghapus atribut tahun

# jika kita coba akses, akan muncul error
# print(mobil1.tahun)  # AttributeError: 'Mobil' object has no attribute 'tahun'
```

Jadi, dengan ini, kita bisa membuat object yang lebih dinamis dan fleksibel!

## 7. Best Practices dalam OOP

Sekarang setelah kalian paham dasar-dasar OOP, yuk kita bahas beberapa **best practices** atau praktik terbaik dalam penggunaan OOP. Hal ini penting agar kode yang kalian buat mudah dipahami, dirawat, dan diperluas di masa mendatang.

### 1. **Gunakan Nama Class dengan Huruf Kapital**
   Biasanya, nama class ditulis dengan huruf kapital pada huruf pertama setiap kata, contohnya: `Mahasiswa`, `Mobil`, `Lingkaran`, dsb. Hal ini membuat kode lebih mudah dibaca dan mengikuti konvensi umum.

   ```python
   class Mahasiswa:  # bukan class mahasiswa
       pass
   ```

### 2. **Pisahkan Logika dengan Menggunakan Metode**
   Sebisa mungkin, masukkan logika atau tindakan-tindakan yang berhubungan dengan object ke dalam metode di dalam class. Jangan menaruh logika di luar class, karena ini akan memecah fokus dan membuat kode lebih sulit diikuti.

   ```python
   class Mobil:
       def __init__(self, merek, warna):
           self.merek = merek
           self.warna = warna

       def deskripsi(self):
           return f"Mobil {self.merek} berwarna {self.warna}"

   # jangan seperti ini:
   # mobil1.merek = "Toyota"
   # mobil1.warna = "Merah"
   ```

### 3. **Jaga Atribut agar Konsisten**
   Cobalah untuk menjaga atribut object konsisten di seluruh program. Misalnya, jika mobil punya atribut `merek` dan `warna`, pastikan semua object `Mobil` memiliki atribut ini. Jangan menambahkan atribut baru secara sembarangan, karena bisa membingungkan.

### 4. **Gunakan Constructor untuk Inisialisasi**
   Selalu gunakan constructor (`__init__`) untuk menetapkan nilai awal atribut object. Ini membuat object kalian lebih terstruktur dan jelas sejak awal.

   ```python
   class Mahasiswa:
       def __init__(self, nama, nim):
           self.nama = nama
           self.nim = nim
   ```

### 5. **Buat Kode Modular dan Reusable**
   OOP sangat mendukung modularitas, di mana kalian bisa membuat class yang mudah digunakan kembali di berbagai bagian program. Buat class dan metode yang bersifat umum dan bisa digunakan di berbagai situasi.

---

## 8. Studi Kasus Sederhana

Mari kita coba membuat sebuah studi kasus sederhana untuk lebih memahami konsep class dan object. Misalnya, kita akan membuat class `Mahasiswa` yang menggambarkan mahasiswa di sebuah universitas.

### Contoh Class Mahasiswa

```python
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
    
    def perkenalan(self):
        print(f"Halo, nama saya {self.nama}, NIM {self.nim}, dari jurusan {self.jurusan}.")
    
    def belajar(self, mata_kuliah):
        print(f"{self.nama} sedang belajar mata kuliah {mata_kuliah}.")

# Membuat object mahasiswa
mahasiswa1 = Mahasiswa("Andi", "123456", "Matematika")
mahasiswa2 = Mahasiswa("Budi", "789012", "Fisika")

# Menggunakan metode perkenalan
mahasiswa1.perkenalan()  # Output: Halo, nama saya Andi, NIM 123456, dari jurusan Matematika.
mahasiswa2.perkenalan()  # Output: Halo, nama saya Budi, NIM 789012, dari jurusan Fisika.

# Memanggil metode belajar
mahasiswa1.belajar("Aljabar Linear")  # Output: Andi sedang belajar mata kuliah Aljabar Linear.
mahasiswa2.belajar("Fisika Dasar")    # Output: Budi sedang belajar mata kuliah Fisika Dasar.
```

Di sini, kita membuat class `Mahasiswa` dengan atribut `nama`, `nim`, dan `jurusan`. Setiap object mahasiswa bisa memperkenalkan diri dan belajar mata kuliah tertentu. Keren, kan?

Selamat mencoba! Kalian bisa bereksperimen dengan class dan object ini, membuat variasi object yang berbeda, dan melihat bagaimana OOP membantu menyederhanakan kode kalian.