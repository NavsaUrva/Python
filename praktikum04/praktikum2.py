# input
nama = input ("nama anda : " )
kelas = input ("kelas anda : " )
nilai = int(input('nilai anda : ' ))

# keterangan
if nilai > 90:
    ket = "istimewa"
elif nilai > 70 :
    ket = "sangat bagus"
elif nilai > 60 :
    ket = "cukup"
else :
    ket = "gagal"

# output
print ("nama saya " ,nama)
print ("kelas saya " ,kelas)
print ("nilai saya " ,nilai )
print ("predikat saya " ,ket)