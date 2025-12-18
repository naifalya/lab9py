# ========================================
# LATIHAN 1: Operasi Dasar String
# ========================================
print("="*50)
print("LATIHAN 1: Operasi Dasar String")
print("="*50)

txt = 'Hello World'
print("String awal:", txt)
print()

# 1. Hitung jumlah karakternya
jumlah_karakter = len(txt)
print("1. Jumlah karakter:", jumlah_karakter)

# 2. Ambil karakter terakhir
# Cara 1: menggunakan index negatif
karakter_terakhir = txt[-1]
print("2. Karakter terakhir:", karakter_terakhir)

# Cara 2: menggunakan len()
# karakter_terakhir = txt[len(txt)-1]

# 3. Ambil karakter index ke-2 sampai index ke-4 (llo)
# Index 2, 3, 4 -> tapi index akhir tidak termasuk, jadi [2:5]
substring = txt[2:5]
print("3. Karakter index 2-4 (llo):", substring)

# 4. Hilangkan spasi pada text tersebut (HelloWorld)
tanpa_spasi = txt.replace(" ", "")
print("4. Tanpa spasi:", tanpa_spasi)

# 5. Ubah text menjadi huruf besar
huruf_besar = txt.upper()
print("5. Huruf besar:", huruf_besar)

# 6. Ubah text menjadi huruf kecil
huruf_kecil = txt.lower()
print("6. Huruf kecil:", huruf_kecil)

# 7. Ganti karakter H dengan karakter J
ganti_huruf = txt.replace("H", "J")
print("7. Ganti H dengan J:", ganti_huruf)

print()