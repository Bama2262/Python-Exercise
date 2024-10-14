# Dibuat Oleh : Bama Maulana Wibisana
# Tanggal Pengerjaan : 08 Oktober 2024
# Program Menghitung Rumus Limas Segitiga

print("="*20)
print("Rumus Limas Segitiga")
print("="*20)

a = int(input("Alas\t: "))
s1 = int(input("Sisi 1\t: "))
s2 = int(input("Sisi 2\t: "))
s3 = int(input("Sisi 3\t: "))
t = int(input("Tinggi\t: "))

l = 1/2 * a * (s1 + s2 + s3) + 1/2 * a
v = 1/3 * a * t

print(f"Luas Permukaan\t: {l}")
print(f"Volume\t: {v}")