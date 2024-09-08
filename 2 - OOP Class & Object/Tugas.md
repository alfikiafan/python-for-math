# Tugas Praktikum: Sistem Pengelolaan Data Mahasiswa

## Deskripsi Tugas

Kalian diminta untuk membuat sebuah **program Python** yang dapat digunakan untuk **mengelola data mahasiswa** dalam sebuah kelas. Program ini akan memungkinkan pengguna untuk:
1. Menambahkan data mahasiswa.
2. Menampilkan data mahasiswa.
3. Menghitung rata-rata nilai dari semua mahasiswa.
4. Mencari mahasiswa dengan nilai tertinggi dan terendah.
5. Menampilkan mahasiswa yang lulus atau tidak lulus (nilai >= 60 lulus).

## Kriteria Program

1. Buat class `Mahasiswa` yang memiliki atribut:
   - `nama`: Nama mahasiswa.
   - `nim`: Nomor Induk Mahasiswa.
   - `nilai`: Nilai akhir mahasiswa (integer).

2. Class `Mahasiswa` harus memiliki metode:
   - `deskripsi()`: Menampilkan data mahasiswa (nama, NIM, nilai).
   - `status_kelulusan()`: Menampilkan status kelulusan (Lulus jika nilai >= 60, Tidak Lulus jika nilai < 60).

3. Buat class `Kelas` yang memiliki atribut:
   - `daftar_mahasiswa`: List untuk menyimpan object `Mahasiswa` yang sudah dibuat.
   - **Clue:** sintaks untuk membuat list dalam class "Kelas" adalah: `self.daftar_mahasiswa = []`.

4. Class `Kelas` harus memiliki metode:
   - `tambah_mahasiswa(mahasiswa)`: Menambahkan object `Mahasiswa` ke dalam list `daftar_mahasiswa`.  
   - **Clue:** sintaks untuk menambahkan object ke dalam list adalah: `self.daftar_mahasiswa.append(mahasiswa)`.
   - `tampilkan_semua_mahasiswa()`: Menampilkan semua data mahasiswa dalam kelas.
   - `hitung_rata_rata_nilai()`: Menghitung dan menampilkan rata-rata nilai mahasiswa dalam kelas.
   - **Clue:** gunakan fungsi `sum()` untuk menjumlahkan nilai-nilai mahasiswa dan `len()` untuk menghitung jumlah mahasiswa.
   - `cari_nilai_tertinggi()`: Menampilkan mahasiswa dengan nilai tertinggi.
   - **Clue:** gunakan fungsi `max()` untuk mencari nilai tertinggi.
   - `cari_nilai_terendah()`: Menampilkan mahasiswa dengan nilai terendah.
   - **Clue:** gunakan fungsi `min()` untuk mencari nilai terendah.

### Persyaratan Tambahan
- Gunakan **looping** (perulangan) dan **if-else** untuk mengecek status kelulusan mahasiswa dan menampilkan hasilnya.
- Pastikan tipe data yang digunakan untuk atribut sudah sesuai (contoh: `nilai` harus berupa integer).
- **Clue:** gunakan fungsi `int()` untuk mengubah input menjadi integer.
- Buatlah validasi sederhana agar nilai yang dimasukkan harus berada dalam rentang 0-100.
**Clue:** gunakan pernyataan `if` untuk mengecek nilai yang dimasukkan. Misalnya, jika nilai < 0, maka nilai = 0. Jika nilai > 100, maka nilai = 100.

---

### Panduan Penyelesaian

1. **Class Mahasiswa**
   - Buat class `Mahasiswa` yang memiliki atribut nama, NIM, dan nilai.
   - Buat metode `deskripsi()` untuk menampilkan detail mahasiswa dan metode `status_kelulusan()` untuk mengecek apakah mahasiswa lulus atau tidak.

2. **Class Kelas**
   - Buat class `Kelas` yang menyimpan daftar mahasiswa dalam list.
   - Implementasikan metode untuk menambah mahasiswa, menampilkan semua data mahasiswa, menghitung rata-rata nilai, dan mencari nilai tertinggi serta terendah.

---

### Contoh Hasil Eksekusi

```bash
===== Sistem Pengelolaan Data Mahasiswa =====
1. Tambah Mahasiswa
2. Tampilkan Semua Mahasiswa
3. Hitung Rata-rata Nilai
4. Cari Nilai Tertinggi
5. Cari Nilai Terendah
6. Keluar
Pilih opsi (1-6): 1
Masukkan nama mahasiswa: Andi
Masukkan NIM mahasiswa: 123456
Masukkan nilai mahasiswa (0-100): 85
Mahasiswa Andi berhasil ditambahkan.

===== Sistem Pengelolaan Data Mahasiswa =====
1. Tambah Mahasiswa
2. Tampilkan Semua Mahasiswa
3. Hitung Rata-rata Nilai
4. Cari Nilai Tertinggi
5. Cari Nilai Terendah
6. Keluar
Pilih opsi (1-6): 1
Masukkan nama mahasiswa: Budi
Masukkan NIM mahasiswa: 789012
Masukkan nilai mahasiswa (0-100): 92
Mahasiswa Budi berhasil ditambahkan.

===== Sistem Pengelolaan Data Mahasiswa =====
1. Tambah Mahasiswa
2. Tampilkan Semua Mahasiswa
3. Hitung Rata-rata Nilai
4. Cari Nilai Tertinggi
5. Cari Nilai Terendah
6. Keluar
Pilih opsi (1-6): 2

Daftar Mahasiswa:
1. Andi - NIM: 123456 - Nilai: 85 (Lulus)
2. Budi - NIM: 789012 - Nilai: 92 (Lulus)

===== Sistem Pengelolaan Data Mahasiswa =====
1. Tambah Mahasiswa
2. Tampilkan Semua Mahasiswa
3. Hitung Rata-rata Nilai
4. Cari Nilai Tertinggi
5. Cari Nilai Terendah
6. Keluar
Pilih opsi (1-6): 3
Rata-rata nilai kelas adalah: 88.50

===== Sistem Pengelolaan Data Mahasiswa =====
1. Tambah Mahasiswa
2. Tampilkan Semua Mahasiswa
3. Hitung Rata-rata Nilai
4. Cari Nilai Tertinggi
5. Cari Nilai Terendah
6. Keluar
Pilih opsi (1-6): 4
Mahasiswa dengan nilai tertinggi:
Budi - NIM: 789012 - Nilai: 92

===== Sistem Pengelolaan Data Mahasiswa =====
1. Tambah Mahasiswa
2. Tampilkan Semua Mahasiswa
3. Hitung Rata-rata Nilai
4. Cari Nilai Tertinggi
5. Cari Nilai Terendah
6. Keluar
Pilih opsi (1-6): 5
Mahasiswa dengan nilai terendah:
Andi - NIM: 123456 - Nilai: 85

===== Sistem Pengelolaan Data Mahasiswa =====
1. Tambah Mahasiswa
2. Tampilkan Semua Mahasiswa
3. Hitung Rata-rata Nilai
4. Cari Nilai Tertinggi
5. Cari Nilai Terendah
6. Keluar
Pilih opsi (1-6): 6
Program selesai.
```

---

### Batas Pengumpulan
Kumpulkan tugas kalian dalam bentuk **file Python (.py)** ke dalam Google Classroom **paling lambat 1 minggu** dari hari ini.

Selamat mengerjakan, dan jangan ragu untuk bertanya jika ada yang kurang jelas. Tetap semangat!