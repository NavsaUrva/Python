print("=================== Program Kasir ====================")
pembeli = input("Masukkan Nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

def fungsimakanan():
   global totalMakan
   global porsi
   global makan
   print ("\n================= Menu Makanan =================")
   print("1. Nasi Goreng - Rp 15000")
   print("2. Soto - Rp 9000")
   print("3. Mie Ayam - Rp 11000")
   nomor= int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       totalMakan=porsi*15000
       print (porsi," porsi Nasi Goreng Telur = Rp", totalMakan)
       makan =("Nasi Goreng")
   elif nomor==2:
       totalMakan=porsi*9000
       print (porsi," porsi Soto = Rp", totalMakan)
       makan=("Soto")
   elif nomor==3:
       totalMakan=porsi*11000
       print (porsi, " porsi Mie Ayam = Rp", totalMakan)
       makan=("Mie Ayam")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()

def fungsiminuman():
   global totalMinuman
   global minum
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Es teh - Rp 2000")
   print("2. Es jeruk - Rp 3500")
   print("3. Es kopi - Rp 4000")
   nomor= int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       totalMinuman=gelas*2000
       print (gelas," Es Teh = Rp", totalMinuman)
       minum=(" Gelas Es Teh")
   elif nomor==2:
       totalMinuman=gelas*3500
       print (gelas, " Gelas Es Jeruk = Rp", totalMinuman)
       minum=("Es Jeruk")
   elif nomor==3:
       totalMinuman=gelas*4000
       print (gelas, " Gelas Es Kopi = Rp", totalMinuman)
       minum=("Es Kopi")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalMakan+totalMinuman