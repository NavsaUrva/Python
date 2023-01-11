print ("======= PROGRAM KALIMAT YANG DIBALIK =======")
print ("============================================")

def balik_kalimat(kalimat):
    kalimat_balik = ""

    kata = kalimat.split()

    for i in range(len(kata)):

        kalimat_balik += kata[-i-1] + " "
    return kalimat_balik

print(balik_kalimat("Saya Mahasiswa Nurul Fikri"))
print(balik_kalimat("Saya Prodi Teknik Informatika"))
print(balik_kalimat("Pemograman Dasar Menyenangkan"))