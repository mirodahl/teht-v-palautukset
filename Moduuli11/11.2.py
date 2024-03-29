#Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
# Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
# Kirjoita aliluokille alustajat.
# Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
# Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.
# Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja
# yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
# Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja
# tulosta autojen matkamittarilukemat.
import random
cars = []
class Car:
    def __init__(self, reg_plate, top_spd):
        self.reg_plate = reg_plate
        self.top_spd = top_spd
        self.cur_spd = 0
        self.trav_dist = 0
        print(f"Auto luotu, rekno: {reg_plate}, huippunopeus {top_spd}")

    def accelerate(self, change):
        self.cur_spd = self.cur_spd + change
        if self.cur_spd > self.top_spd:
            self.cur_spd = self.top_spd
        if self.cur_spd < 0:
            self.cur_spd = 0
        return print(f"Auton {self.reg_plate} tämän hetkinen nopeus {self.cur_spd} km/h")

    def travel(self, hours):
        change = self.cur_spd * hours
        self.trav_dist = self.trav_dist + change
        print(f"Autolla {self.reg_plate} ajetaan {hours} tuntia")
        return self.trav_dist

class ElectricCar(Car):
    def __init__(self, reg_plate, top_spd, battery_cap):
        self.battery_cap = battery_cap
        super().__init__(reg_plate, top_spd)

class PetrolCar(Car):
    def __init__(self, reg_plate, top_spd, tank_size):
        self.tank_size = tank_size
        super().__init__(reg_plate, top_spd)


###pääohjelma alkaa

cars.append(ElectricCar("ABC-15", 180, 52.5))
cars.append(PetrolCar("ABD-123", 165, 32.3))

for car in cars:
    car.accelerate(200)
    car.travel(3)

print("Nyt ollaan ajettu haluttu aika, katsotaas kuinka monta kilometriä kertyikään mittariin")

for car in cars:
    print(f"Autolla {car.reg_plate} on ajettu {car.trav_dist} kilometriä")
