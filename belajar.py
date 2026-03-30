nama = input ("nama barang    : ")
harga = int(input("harga barang :"))
qty = int(input("Jumlah Barang :"))
print ("-" * 30)
subtotal = harga * qty
diskon = 0.20 * subtotal 
total = subtotal - diskon
print (f"Subtotal       : Rp. {subtotal:10.0f}")
print (f"diskon         : Rp. {diskon:10.0f}")
print (f"Total          : Rp. {total:10.0f}")