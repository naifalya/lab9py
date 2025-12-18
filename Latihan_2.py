# ========================================
# LATIHAN 2: Format String
# ========================================
print("="*50)
print("LATIHAN 2: Format String")
print("="*50)

umur = 24
txt = 'Hello, nama saya john, dan umur saya adalah {} tahun'
print(txt.format(umur))

# Alternatif cara format string:
# Cara 1: menggunakan .format() dengan nama variabel
txt2 = 'Hello, nama saya {nama}, dan umur saya adalah {umur} tahun'
print(txt2.format(nama="john", umur=24))

# Cara 2: menggunakan f-string (Python 3.6+)
nama = "john"
umur = 24
txt3 = f'Hello, nama saya {nama}, dan umur saya adalah {umur} tahun'
print(txt3)

# Cara 3: menggunakan % operator
txt4 = 'Hello, nama saya %s, dan umur saya adalah %d tahun' % ('john', 24)
print(txt4)

print()