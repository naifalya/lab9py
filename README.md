# Latihan Python String

## Deskripsi
Latihan Python String untuk mahasiswa semester 1 Teknik Informatika. Mencakup operasi dasar string, format string, dan validasi form input.

---



## Latihan 1: Operasi Dasar String

### Screenshot Output

<img width="554" height="341" alt="Latihan1" src="https://github.com/user-attachments/assets/624ae739-e3ac-4037-ab00-7ccddbd91ae7" />


### Materi

```
txt = 'Hello World'
```

1. **Hitung jumlah karakter:** `len(txt)` → 11
2. **Karakter terakhir:** `txt[-1]` → 'd'
3. **Slicing index 2-4:** `txt[2:5]` → 'llo'
4. **Hilangkan spasi:** `txt.replace(" ", "")` → 'HelloWorld'
5. **Huruf besar:** `txt.upper()` → 'HELLO WORLD'
6. **Huruf kecil:** `txt.lower()` → 'hello world'
7. **Ganti karakter:** `txt.replace("H", "J")` → 'Jello World'

### Konsep Penting
- String di Python **immutable** (tidak bisa diubah)
- Index dimulai dari **0**
- Index negatif untuk akses dari **belakang**

---

## Latihan 2: Format String

### Screenshot Output

<img width="539" height="304" alt="Latihan2" src="https://github.com/user-attachments/assets/1f743d90-a35b-4e56-bd49-947555696228" />


### 4 Cara Format String

#### 1. Method `.format()`
```
txt = 'Nama saya {}, umur {} tahun'
print(txt.format('john', 24))
```

#### 2. Named Placeholder
```
txt = 'Nama saya {nama}, umur {umur} tahun'
print(txt.format(nama='john', umur=24))
```

#### 3. F-string (Python 3.6+)
```
nama = 'john'
umur = 24
txt = f'Nama saya {nama}, umur {umur} tahun'
```

#### 4. % Operator
```
txt = 'Nama saya %s, umur %d tahun' % ('john', 24)
```

---

## Studi Kasus: Validasi Form Input

### Spesifikasi
Validasi input pendaftaran online:
- **Nama:** Hanya huruf (dan spasi)
- **Telepon:** Hanya angka
- **Email:** Harus ada @ dan .

### String Methods yang Digunakan

| Method | Fungsi | Contoh |
|--------|--------|--------|
| `replace()` | Mengganti substring | `"a b".replace(" ", "")` → `"ab"` |
| `isalpha()` | Cek hanya huruf | `"abc".isalpha()` → `True` |
| `isdigit()` | Cek hanya angka | `"123".isdigit()` → `True` |
| `find()` | Cari posisi substring | `"abc".find("b")` → `1` |
| `rfind()` | Cari dari belakang | `"abcb".rfind("b")` → `3` |

### Penjelasan Validasi

#### Validasi Nama
```python
nama_tanpa_spasi = nama.replace(" ", "")
if not nama_tanpa_spasi.isalpha():
    # Error: nama tidak valid
```
- Hapus spasi → cek apakah hanya huruf

#### Validasi Telepon
```python
if not telepon.isdigit():
    # Error: telepon tidak valid
```
- Cek apakah semua karakter adalah angka

#### Validasi Email
```python
if "@" not in email or "." not in email:
    # Error: email tidak valid

# Validasi tambahan: @ harus sebelum .
posisi_at = email.find("@")
posisi_titik = email.rfind(".")
if posisi_at > posisi_titik:
    # Error: format email salah
```

### Contoh Output

<img width="560" height="391" alt="StudiKasus" src="https://github.com/user-attachments/assets/6741f1b3-4b14-4364-bc98-23dcbf5d6e87" />



