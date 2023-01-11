#program menghitung berat badan ideal
#input
TinggiBadan = input("masukan tinggi badan dalam (cm) = ")

#rumus
TinggiBadan1 = (int(TinggiBadan) - 100) * 10/100
BeratIdeal = (int(TinggiBadan) - 100) - (int(TinggiBadan1))

#output
print ("berat badan ideal anda = ", BeratIdeal, "kg")