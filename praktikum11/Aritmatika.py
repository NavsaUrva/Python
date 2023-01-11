# Modul Aritmatika

print("==========================MODUL ARITMATIKA==========================")

def tambah(*args):
  hasil = 0
  for arg in args:
    hasil += arg
  print("Hasil Penjumlahan = ", hasil)

def kurang(*args):
  hasil = args[0]
  for arg in args[1:]:
    hasil -= arg
  print("Hasil Pengurangan = ", hasil)

def kali(*args):
  hasil = 1
  for arg in args:
    hasil *= arg
  print("Hasil Perkalian = ", hasil)