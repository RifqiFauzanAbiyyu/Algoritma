total = int(input("Total Bayar :"))
bayar = int(input("Uang yang dibayarkan :"))
kembali = bayar - total
print(f"Kembalian Rp. {kembali}")
print("Rincian Kembalian")
rp50000 = kembali // 50000
print(f"Rp. 50.000 : {rp50000} lembar")
kembali = kembali % 50000
rp20000 = kembali // 20000
print (f"Rp. 20.000 : {rp20000} lembar")
kembali %= 20000
rp10000 = kembali // 10000
print (f"Rp. 10.000 : {rp10000} lembar")
kembali %= 10000
rp5000 = kembali // 5000
print(f"Rp. 5.000 : {rp5000} lembar")
kembali %= 5000
rp2000 = kembali // 2000
print(f"Rp. 2.000 : {rp2000} lembar")
kembali %= 2000
rp1000 = kembali // 1000
print(f"Rp. 1.000 : {rp1000} lembar")
kembali %= 1000
