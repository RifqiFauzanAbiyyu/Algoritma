nama    =    input("Nama Barang  : ")
harga   =int(input("Harga        : "))
qty     =int(input("Qty          : "))
print("-" * 30)
subtotal = harga * qty
diskon   = 0.20 * subtotal
total    = subtotal - diskon
print(f"subtotal        : Rp. {subtotal:10.0f}")
print(f"diskon (20%)    : Rp. {diskon:10.0f}")
print(f"subtotal         : Rp. {total:10.0f}")