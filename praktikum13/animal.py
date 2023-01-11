class Animal:
    def __init__(self, name, food, habitat, reproduction):
        self.name = name
        self.food = food
        self.habitat = habitat
        self.reproduction = reproduction

class Badak (Animal):
    def __init__(self, name, food, habitat, reproduction, size, weight): 
        super().__init__(name, food, habitat, reproduction)
        self.size = size 
        self.weight = weight

    def display_characteristics (self): 
        print(f"Nama: {self.name}")
        print(f"Makanan: {self.food}") 
        print(f"Habitat: {self.habitat}")
        print(f"Cara berkembang biak: {self.reproduction}")
        print(f"Ukuran: {self.size}")
        print(f"Berat: {self.weight}")

class Ikan (Animal): 
    def __init__(self, name, food, habitat, reproduction, color, fins):
        super().__init__(name, food, habitat, reproduction)
        self.color = color 
        self.fins = fins

    def display_characteristics (self): 
        print(f"Nama: {self.name}") 
        print(f"Makanan: {self.food}") 
        print(f"Habitat: {self.habitat}")
        print(f"Cara berkembang biak: {self.reproduction}") 
        print(f"Warna: {self.color}")
        print(f"Sirip: {self.fins}")

class Ular (Animal):
    def __init__(self, name, food, habitat, reproduction, length, venomous): 
        super().__init__(name, food, habitat, reproduction) 
        self.length = length
        self.venomous = venomous
        
        
    def display_characteristics (self): 
        print(f"Nama: {self.name}")
        print(f"Makanan: {self.food}") 
        print(f"Habitat: {self.habitat}")
        print(f"Cara berkembang biak: {self.reproduction}")
        print(f"Panjang: {self.length}")
        print(f"Berbisa: {self.venomous}")

class Gajah (Animal):
    def _init(self, name, food, habitat, reproduction, size, weight): 
        super().__init__(name, food, habitat, reproduction) 
        self.size = size
        self.weight = weight
        
    def display_characteristics (self):
        print(f"Nama: {self.name}") 
        print(f"Makanan: {self.food}")
        print(f"Habitat: {self.habitat}")
        print(f"Cara berkembang biak: {self.reproduction}") 
        print(f"Ukuran: {self.size}")
        print(f"Berat: {self.weight}")

badak = Badak ("Badak", "Herbivora", "Hutan", "Beranak", "Besar", "Berat")
badak.display_characteristics()
print('\n====================')

ikan = Ikan ("Ikan", "Omnivora", "Laut", "Bertelur", "Merah", "Banyak") 
ikan.display_characteristics()
print('\n====================')

ular = Ular ("Ular", "Karnivora", "Rawa-rawa", "Bertelur", "Tergantung", "Mematikan")
ular.display_characteristics()
print('\n====================')

gajah = Gajah("Gajah", "Herbivora", "Hutan", "Beranak", "Besar", "Sangat Berat" )
gajah.display_characteristics()