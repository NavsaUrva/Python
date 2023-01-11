#input
namaKendaraan = str(input("Masukkan Jenis Kendaraan = "))
jenisBensin = str(input("Masukkan Jenis Bensin = "))
kotaTujuan = str(input("Masukkan Kota Tujuan = "))

print("===================================================")

#rumus
pakaiBensin = float
hargaBensin = float

#JAKARTA
if kotaTujuan == "Jakarta": 
    if jenisBensin == "Pertalite" :
        print("Jenis Kendaraan yang dipakai = ", namaKendaraan)
        print("Jenis bensin yang dipakai = ", jenisBensin)
        print("Kota Tujuan = ", kotaTujuan)
        pakaiBensin = 20/12
        print("Jumlah pemakaian bensin = ", round(pakaiBensin,2), "liter")
        hargaBensin = pakaiBensin * 10000
        print("Total harga bensin = Rp.", round(hargaBensin,2))
    elif jenisBensin == "Pertamax" :
        print("Jenis Kendaraan yang dipakai = ", namaKendaraan)
        print("Jenis bensin yang dipakai = ", jenisBensin)
        print("Kota Tujuan = ", kotaTujuan)
        pakaiBensin = 20/13
        print("Jumlah pemakaian bensin = ", round(pakaiBensin,2), "liter")
        hargaBensin = pakaiBensin * 14000
        print("Total harga bensin = Rp.", round(hargaBensin,2))
    elif jenisBensin == "Pertamax Turbo" :
        print("Jenis Kendaraan yang dipakai = ", namaKendaraan)
        print("Jenis bensin yang dipakai = ", jenisBensin)
        print("Kota Tujuan = ", kotaTujuan)
        pakaiBensin = 20/13.5
        print("Jumlah pemakaian bensin = ", round(pakaiBensin,2), "liter")
        hargaBensin = pakaiBensin * 17000
        print("Total harga bensin = Rp.", round(hargaBensin,2))

#BEKASI
elif kotaTujuan == "Bekasi" : 
    if jenisBensin == "Pertalite" :
        print("Jenis Kendaraan yang dipakai = ", namaKendaraan)
        print("Jenis bensin yang dipakai = ", jenisBensin)
        print("Kota Tujuan = ", kotaTujuan)
        pakaiBensin = 35.7/12
        print("Jumlah pemakaian bensin = ", round(pakaiBensin,2), "liter")
        hargaBensin = pakaiBensin * 10000
        print("Total harga bensin = Rp.", round(hargaBensin,2))
    elif jenisBensin == "Pertamax" :
        print("Jenis Kendaraan yang dipakai = ", namaKendaraan)
        print("Jenis bensin yang dipakai = ", jenisBensin)
        print("Kota Tujuan = ", kotaTujuan)
        pakaiBensin = 35.7/13
        print("Jumlah pemakaian bensin = ", round(pakaiBensin,2), "liter")
        hargaBensin = pakaiBensin * 14000
        print("Total harga bensin = Rp.", round(hargaBensin,2))
    elif jenisBensin == "Pertamax Turbo" :
        print("Jenis Kendaraan yang dipakai = ", namaKendaraan)
        print("Jenis bensin yang dipakai = ", jenisBensin)
        print("Kota Tujuan = ", kotaTujuan)
        pakaiBensin = 35.7/13.5
        print("Jumlah pemakaian bensin = ", round(pakaiBensin,2), "liter")
        hargaBensin = pakaiBensin * 17000
        print("Total harga bensin = Rp.", round(hargaBensin,2))

#DEPOK
elif kotaTujuan == "Depok" :
    if jenisBensin == "Pertalite" :
        print("Jenis Kendaraan yang dipakai = ", namaKendaraan)
        print("Jenis bensin yang dipakai = ", jenisBensin)
        print("Kota Tujuan = ", kotaTujuan)
        pakaiBensin = 5/12
        print("Jumlah pemakaian bensin = ", round(pakaiBensin,2), "liter")
        hargaBensin = pakaiBensin * 10000
        print("Total harga bensin = Rp.", round(hargaBensin,2))
    elif jenisBensin == "Pertamax" :
        print("Jenis Kendaraan yang dipakai = ", namaKendaraan)
        print("Jenis bensin yang dipakai = ", jenisBensin)
        print("Kota Tujuan = ", kotaTujuan)
        pakaiBensin = 5/13
        print("Jumlah pemakaian bensin = ", round(pakaiBensin,2), "liter")
        hargaBensin = pakaiBensin * 14000
        print("Total harga bensin = Rp.", round(hargaBensin,2))
    elif jenisBensin == "Pertamax Turbo" :
        print("Jenis Kendaraan yang dipakai = ", namaKendaraan)
        print("Jenis bensin yang dipakai = ", jenisBensin)
        print("Kota Tujuan = ", kotaTujuan)
        pakaiBensin = 5/13.5
        print("Jumlah pemakaian bensin = ", round(pakaiBensin,2), "liter")
        hargaBensin = pakaiBensin * 17000
        print("Total harga bensin = Rp.", round(hargaBensin,2))

#TANGGERANG
elif kotaTujuan == "Tanggerang" :
    if jenisBensin == "Pertalite" :
        print("Jenis Kendaraan yang dipakai = ", namaKendaraan)
        print("Jenis bensin yang dipakai = ", jenisBensin)
        print("Kota Tujuan = ", kotaTujuan)
        pakaiBensin = 99/12
        print("Jumlah pemakaian bensin = ", round(pakaiBensin,2), "liter")
        hargaBensin = pakaiBensin * 10000
        print("Total harga bensin = Rp.", round(hargaBensin,2))
    elif jenisBensin == "Pertamax" :
        print("Jenis Kendaraan yang dipakai = ", namaKendaraan)
        print("Jenis bensin yang dipakai = ", jenisBensin)
        print("Kota Tujuan = ", kotaTujuan)
        pakaiBensin = 99/13
        print("Jumlah pemakaian bensin = ", round(pakaiBensin,2), "liter")
        hargaBensin = pakaiBensin * 14000
        print("Total harga bensin = Rp.", round(hargaBensin,2))
    elif jenisBensin == "Pertamax Turbo" :
        print("Jenis Kendaraan yang dipakai = ", namaKendaraan)
        print("Jenis bensin yang dipakai = ", jenisBensin)
        print("Kota Tujuan = ", kotaTujuan)
        pakaiBensin = 99/13.5
        print("Jumlah pemakaian bensin = ", round(pakaiBensin,2), "liter")
        hargaBensin = pakaiBensin * 17000
        print("Total harga bensin = Rp.", round(hargaBensin,2))

#BOGOR
elif kotaTujuan == "Bogor" :
    if jenisBensin == "Pertalite" :
        print("Jenis Kendaraan yang dipakai = ", namaKendaraan)
        print("Jenis bensin yang dipakai = ", jenisBensin)
        print("Kota Tujuan = ", kotaTujuan)
        pakaiBensin = 120.6/12
        print("Jumlah pemakaian bensin = ", round(pakaiBensin,2), "liter")
        hargaBensin = pakaiBensin * 10000
        print("Total harga bensin = Rp.", round(hargaBensin,2))
    elif jenisBensin == "Pertamax" :
        print("Jenis Kendaraan yang dipakai = ", namaKendaraan)
        print("Jenis bensin yang dipakai = ", jenisBensin)
        print("Kota Tujuan = ", kotaTujuan)
        pakaiBensin = 120.6/13
        print("Jumlah pemakaian bensin = ", round(pakaiBensin,2), "liter")
        hargaBensin = pakaiBensin * 14000
        print("Total harga bensin = Rp.", round(hargaBensin,2))
    elif jenisBensin == "Pertamax Turbo" :
        print("Jenis Kendaraan yang dipakai = ", namaKendaraan)
        print("Jenis bensin yang dipakai = ", jenisBensin)
        print("Kota Tujuan = ", kotaTujuan)
        pakaiBensin = 120.6/13.5
        print("Jumlah pemakaian bensin = ", round(pakaiBensin,2), "liter")
        hargaBensin = pakaiBensin * 17000
        print("Total harga bensin = Rp.", round(hargaBensin,2))