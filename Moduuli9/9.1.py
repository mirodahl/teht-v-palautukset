#Kirjoita Auto-luokka, jonka ominaisuuksina ovat
# rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka.
# Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Car:
    def __init__(self, regplate, topspd):
        self.regplate = regplate
        self.topspd = topspd
        self.curspd = 0
        self.travdist = 0


car = Car("ABC-123", 142)
print(f"Rekisteritunnuksella {car.regplate} olevan auton huippunopeus {car.topspd} km/h, \n"
      f"tämän hetkinen nopeus {car.curspd} ja kuljettu matka {car.travdist} km.")