saldo =int(input("Saldo Awal    :"))
bunga =float(input("Bunga (%)     :"))
waktu =int(input("Jangka Waktu  :"))
print ("-" * 30)
akhir = saldo  * (1 + bunga/100) ** waktu
print(f"Saldo di bulan {waktu} : Rp. {akhir:10.2f}")
print("Rincian per bulan \n " + "-" * 20)
for bulan in range (1, waktu +1 ):
    akhir = saldo * (1 + bunga / 100) ** bulan
    print(f"Saldo di bulan {bulan}  : Rp.  {akhir:12.2f}")

