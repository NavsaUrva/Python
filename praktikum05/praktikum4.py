# input
namaKendaraan = input ("kendaraan : " )
jenisBensin = input ("Jenis Bensin : " )
kotaTujuan = input ("Kota yang akan di tuju : " )

# keterangan
if jenisBensin == "pertalite":
    harga =10000
    jarakTempuh=12
elif jenisBensin == "pertamax":
    harga=14000
    jarakTempuh=13
elif jenisBensin == "pertamax turbo":
    harga=17000
    jarakTempuh =13.5
else:
    print("habis")

if kotaTujuan=="jakarta":
    jarakKota=20
elif kotaTujuan=="bekasi":
    jarakKota=35.7
elif kotaTujuan=="depok":
    jarakKota=5
elif kotaTujuan=="tanggerang":
    jarakKota=99
elif kotaTujuan=="bogor":
    jarakKota=120.6
else:
    print("kota tidak di ketahui")

pemakaianBensin = jarakKota/jarakTempuh
totalHargaBensin = pemakaianBensin*harga

# output
print ("kendaraan " ,namaKendaraan)
print ("bensin yang dipakai " ,jenisBensin)
print ("kota tujuan " ,kotaTujuan)
print("pemakaian bensin : ",pemakaianBensin ,"liter")
print ("total harga bensin : ","Rp." ,totalHargaBensin)