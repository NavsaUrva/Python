menu = ["nasi goreng", "mie goreng", "ayam geprek", "jus", "soft drink", "sweet ice tea"]
food = "Makan", "makan"
drink = "Minum", "minum"

# input
print("Selamat Datang di Restoran")
nama = input("nama anda = ")
no = int(input("Masukan nomor telepon anda = "))
pilihan = str(input("Pesan makan atau minum = "))

# output & rumus
if pilihan in food:
    print("Daftar Makan")
    print("Nasi goreng      = Rp.15.000")
    print("Mie goreng       = Rp.12.000")
    print("Ayam geprek      = Rp.18.000")

elif pilihan in drink:
    print("Daftar Minum")
    print("Aneka Jus        = Rp.15.000")
    print("soft drink       = Rp.10.000")
    print("Sweet Ice Tea    = Rp.5.000")
else:
    print("Pilihlah keinginan anda dengan benar, Silahkan restart program kembali")
pesanan = input("masukan pesanan  = ")
jumlah = int(input("jumlah yang dibeli  = "))
if pesanan in menu:
    if pesanan in menu[0]:
        hitung1 = jumlah * 15000
        print ("anda membeli nasi goreng seharga","Rp. ", hitung1 )
    elif pesanan in menu[1]:
        hitung2 = jumlah * 12000
        print ("anda membeli mie goreng seharga","Rp. ", hitung2 )
    elif pesanan in menu[2]:
        hitung3 = jumlah * 18000
        print ("anda membeli ayam geprek seharga","Rp. ", hitung3 )
    elif pesanan in menu[3]:
        hitung4 = jumlah * 15000
        print ("anda membeli aneka jus seharga","Rp. ", hitung4 )
    elif pesanan in menu[4]:
        hitung5 = jumlah * 10000
        print ("anda membeli soft drink seharga","Rp. ", hitung5 )
    elif pesanan in menu[5]:
        hitung6 = jumlah * 5000
        print ("anda membeli sweet ice tea seharga","Rp. ", hitung6 )
    else :
        print("ulang")
else:
    print("ulang")