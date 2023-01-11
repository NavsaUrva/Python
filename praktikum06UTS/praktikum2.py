# Program Membuat Kalkulator
# INPUT
x = int(input("masukan angka ke-1 = "))
y = int(input("masukan angka ke-2 = "))

print('======================')
print('pilih operator')
print(' 1. Tambah \t [+]')
print(' 2. Kurang \t [-]')
print(' 3. Pembagian \t [/]')
print(' 4. Kali \t [*]')
print(' 5. Pangkat \t [**]')
operator = input("masukan pilihan operator = ")

print ('===============')

# KETERANGAN
if operator == '1' :
    hasil = x + y
elif operator == '2' :
    hasil = x - y
elif operator == '3' :
    hasil = x / y
elif operator == '4' :
    hasil = x * y
elif operator == '5' :
    hasil = x ** 2
else :
    print ('hasil tidak ditemukan, mohon ulang lagi dari awal')

# OUTPUT
print("angka ke-1 = ", x)
print("angka ke-2 = ", y)
print("pilihan operator = ", operator)
print("hasil operator = ", hasil)
    