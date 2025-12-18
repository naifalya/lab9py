# ========================================
# STUDI KASUS: Validasi Form Input
# ========================================
print("="*50)
print("STUDI KASUS: Validasi Form Input")
print("="*50)

# Input data dari user
print("Silakan masukkan data pendaftaran:")
nama = input("Nama lengkap: ")
telepon = input("Nomor telepon: ")
email = input("Email: ")

# Variabel untuk tracking validasi
validasi_berhasil = True
pesan_error = []

# Validasi nama lengkap (hanya huruf dan spasi)
# Cara kerja: hapus spasi dulu, lalu cek apakah hanya huruf
nama_tanpa_spasi = nama.replace(" ", "")
if not nama_tanpa_spasi.isalpha():
    validasi_berhasil = False
    pesan_error.append("ERROR: Nama lengkap harus hanya berisi huruf!")
elif len(nama) == 0:
    validasi_berhasil = False
    pesan_error.append("ERROR: Nama tidak boleh kosong!")

# Validasi nomor telepon (hanya angka)
if not telepon.isdigit():
    validasi_berhasil = False
    pesan_error.append("ERROR: Nomor telepon harus hanya berisi angka!")
elif len(telepon) == 0:
    validasi_berhasil = False
    pesan_error.append("ERROR: Nomor telepon tidak boleh kosong!")

# Validasi email (harus mengandung @ dan .)
if "@" not in email or "." not in email:
    validasi_berhasil = False
    pesan_error.append("ERROR: Email harus mengandung karakter @ dan . !")
elif len(email) == 0:
    validasi_berhasil = False
    pesan_error.append("ERROR: Email tidak boleh kosong!")

# Validasi tambahan: @ harus sebelum .
if "@" in email and "." in email:
    posisi_at = email.find("@")
    posisi_titik = email.rfind(".")
    if posisi_at > posisi_titik:
        validasi_berhasil = False
        pesan_error.append("ERROR: Format email tidak valid! @ harus sebelum .")

# Tampilkan hasil validasi
print("\n" + "="*50)
print("HASIL VALIDASI")
print("="*50)

if validasi_berhasil:
    print("SUKSES: Data pendaftaran valid!")
    print("\nData yang terdaftar:")
    print("Nama    :", nama)
    print("Telepon :", telepon)
    print("Email   :", email)
else:
    print("GAGAL: Validasi gagal! Terdapat kesalahan:\n")
    for i, error in enumerate(pesan_error, 1):
        print(f"{i}. {error}")

print("\n" + "="*50)
print("PROGRAM SELESAI")
print("="*50)