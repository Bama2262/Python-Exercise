# Dibuat Oleh : Bama Maulana Wibisana
# Tanggal Pengerjaan : 08 Oktober 2024
# Program Menghitung Rumus Trapesium

print("="*20)
print("Rumus Trapesium")
print("="*20)

sisi1 = int(input("Sisi Sejajar 1\t\t: "))
sisi2 = int(input("Sisi Sejajar 2\t\t: "))
sisi3 = int(input("Sisi Tidak Sejajar 1\t: "))
sisi4 = int(input("Sisi Tidak Sejajar 2\t: "))
t = int(input("Tinggi\t\t\t: "))

l = 1/2 * (sisi1 + sisi2) * t
k = sisi1 + sisi2 + sisi3 + sisi4

print(f"Luas\t\t\t: {l}")
print(f"Keliling\t\t: {k}")