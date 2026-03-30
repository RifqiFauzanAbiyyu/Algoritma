print("Perhitungan Balok\n", "-" * 30)
p = int(input("Panjang  : "))
l = int(input("Lebar    : "))
t = int(input("Tinggi   : "))
print("-" * 30)
luas = 2 * p * l + 2 * p * t + 2 * l * t
volume = p * l * t
print(f"Luas Selimut    : {luas:5}")
print(f"Volume          : {volume:5}")
print(f"Dimensi         : {p} x {l} x {t}")
