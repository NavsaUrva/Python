# membuat program hitung luas bangun datar menggunakan modul

print ("Modul Hitung Luas Bangun Datar") 

def persegiPanjang (panjang, lebar) :
    hasil = panjang * lebar
    print ('Luas Persegi Panjang',':', panjang ,' x ',lebar,'=',hasil , 'cm')

def persegi (sisi1, sisi2) :
    hasil = sisi1 * sisi2
    print ('Luas persegi',':', sisi1,'x', sisi2, '=', hasil, 'cm')

def layangLayang (diagonal1, diagonal2) :
    hasil = 1/2 * (diagonal1 * diagonal2)
    print ('Luas layang-layang',':','1/2','x',diagonal1,'x', diagonal2,'=', hasil, 'cm')

def segitiga (alas, tinggi):
    hasil = 1/2 * (alas * tinggi)
    print ('Luas segitiga',':',' 1/2','*','(', alas,'x', tinggi,')','=', hasil, 'cm')

def jajarGenjang (alas, tinggi) :
    hasil = alas * tinggi
    print ('Luas Jajar Genjang',':',alas,'x',tinggi,'=', hasil, 'cm')
