masuk = input("Masuk (hh:mm) : ").split(":")
keluar = input("Keluar (hh:mm) :").split(":")
jm = int(masuk[0])
mm = int(masuk[1])
jk = int(masuk[0])
mk = int(masuk[1])
print("-" * 30)
lama = (jk * 60 + mk) - (jm * 60 + mm)
lama_jam = lama // 60
lama_menit = lama % 60
print(f"lama : {lama} menit", end="")
print(f"({lama_jam} jam {lama_menit} menit")
bayar = lama / 60 * 5000
print(f"bayar : Rp. {bayar}")
