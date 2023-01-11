# KENDARAAN KE KULIAH
def berangkat(cuaca):
    if cuaca == "hujan":
        print ("Cuaca hujan saya memesan Gocar")
    elif cuaca == "adem" :
        print ("Cuaca adem saya mengendarai motor")
    else :
        print ("jalan kaki")

berangkat (input("bagaimana cuaca hari ini?"))