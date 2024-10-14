# Dibuat Oleh : Bama Maulana Wibisana
# Tanggal Pengerjaan : 08 Oktober 2024
# Program Menghitung Rumus Segitiga

print("="*20)
print("Rumus Segitiga")
print("="*20)

a = int(input("Alas\t\t: "))
t = int(input("Tinggi\t\t: "))
sisi1 = int(input("Sisi 1\t\t: "))
sisi2 = int(input("Sisi 2\t\t: "))
sisi3 = int(input("Sisi 3\t\t: "))

l = 1/2 * a * t
k = sisi1 + sisi2 + sisi3

print(f"Luas\t\t: {l}")
print(f"Keliling\t: {k}")