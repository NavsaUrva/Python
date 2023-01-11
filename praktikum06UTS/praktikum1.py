#program menghitung luas dan keliling layang layang
#input
diagonal1 = int(input('masukan diagonal 1 = '))
diagonal2 = int(input('masukan diagonal 2 = '))
sisi1 = int(input(' masukan sisi 1 = '))
sisi2 = int(input(' masukan sisi 2 = '))

#rumus
luas : float (1/2 * (diagonal1 * diagonal2))
keliling : float (2 * (sisi1 + sisi2))

#output
print ("luas dari layang-layang adalah =", luas)
print ("keliling dari layang-layang adalah =", keliling)