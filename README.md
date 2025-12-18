# Latihan Python String

## Deskripsi

Repository ini berisi latihan-latihan Python String untuk mahasiswa semester 1 Teknik Informatika. Materi mencakup operasi dasar string, format string, dan studi kasus validasi form input.

## Latihan 1: Operasi Dasar String

Tujuan

Memahami operasi-operasi dasar pada tipe data string di Python, termasuk indexing, slicing, dan penggunaan built-in methods.

Screenshot Output Latihan 1
<img width="554" height="341" alt="Latihan1" src="https://github.com/user-attachments/assets/9e9e985e-a791-4680-bb41-25d10febf618" />

Materi yang Dipelajari

1. Menghitung Jumlah Karakter
```
txt = 'Hello World'
jumlah = len(txt)  # Output: 11
```
Penjelasan: Fungsi len() mengembalikan jumlah total karakter dalam string, termasuk spasi.

2. Mengambil Karakter Terakhir
```
karakter_terakhir = txt[-1]  # Output: 'd'
```
Penjelasan:

- Index negatif dimulai dari akhir string
- -1 = karakter terakhir
- -2 = karakter kedua dari belakang, dst

3. String Slicing (Index ke-2 sampai ke-4)
```
substring = txt[2:5]  # Output: 'llo'
```

Penjelasan:

- Format: string[start:end]

- Index start termasuk, index end tidak termasuk

- txt[2:5] mengambil karakter index 2, 3, 4

4. Menghilangkan Spasi
```
tanpa_spasi = txt.replace(" ", "")  # Output: 'HelloWorld'
```
Penjelasan: Method `replace(old, new)` mengganti semua kemunculan karakter/substring lama dengan yang baru.

5. Mengubah ke Huruf Besar
```
huruf_besar = txt.upper()  # Output: 'HELLO WORLD'
```
Penjelasan: Method upper() mengkonversi semua huruf menjadi uppercase.

6. Mengubah ke Huruf Kecil
```
huruf_kecil = txt.lower()  # Output: 'hello world'
```
Penjelasan: Method lower() mengkonversi semua huruf menjadi lowercase.

8. Mengganti Karakter
```
ganti_huruf = txt.replace("H", "J")  # Output: 'Jello World'
```
Penjelasan: Mengganti karakter 'H' dengan 'J'.

Konsep Penting

- Immutability: String di Python bersifat immutable (tidak bisa diubah). Operasi seperti `replace()`, `upper()`, `lower()` menghasilkan string baru, bukan mengubah string asli.
- Zero-based Indexing: Index dimulai dari 0, bukan 1.
