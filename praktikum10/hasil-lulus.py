print ("Navsa Urva")
print ("==============================")

hasilAkhir = [
    {'nama':'Reza', 'nilai':70},
    {'nama':'abdul', 'nilai':63},
    {'nama':'Nabil', 'nilai':85},
    {'nama':'ishaq', 'nilai':60}
]

def lulusNilai(input):
    # Filter nilai siswa yang lulus
    siswaLulus = [i for i in input if i['nilai'] > 65]

    return siswaLulus

siswaLulus = lulusNilai(hasilAkhir)

for siswa in siswaLulus:
    print(f"{siswa['nama']} Lulus")