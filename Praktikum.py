#1.Variabel dan tipe data
print("=== 1. variabel dan tipe data ===")
angka_int = 10
angka_float = 3.14


kata_str = "Halo"
daftar_list = [1, 2, 3]

print(angka_int)
print(angka_float)
print(kata_str)
print(daftar_list)
print()

print("=== 2. List Dan Manipulasi ===")

belanja = ["beras", "minyak", "telur"]
belanja.append("gula")
belanja.append("kopi")

for item in belanja:
    print(item)
print()

print("=== 3. Dictionary ===")
belanjaan = {
    "beras": 12000,
    "minyak": 17000,
    "telur": 24000,
    "gula": 15000,
    "kopi": 20000
}
total_harga = sum(belanjaan.values())
for belanja, harga in belanjaan.items():
    print(f"- {belanja}: Rp: {harga}")

print("Total harga semua belanjaan:", total_harga)
print()

print("=== 4. Fungsi ===")

def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

luas, keliling = hitung_persegi_panjang(5, 3)
print("Luas:", luas)
print("Keliling:", keliling)
print()

print("=== 5. Percabangan ===")
usia = int(input("Masukkan usia: "))
if 0 <= usia <= 13:
    print("Anak")
elif 14 <= usia <= 24:
    print("Remaja")
elif 25 <= usia <= 49:
    print("Dewasa")
elif usia > 50:
    print("Lansia")
else:
    print("Usia tidak valid")
    print()