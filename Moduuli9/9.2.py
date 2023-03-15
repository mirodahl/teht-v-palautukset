#Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
# joka saa parametrinaan nopeuden muutoksen
# (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa.
# Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
# Tulosta tämän jälkeen auton nopeus.
# Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.

class Car:
    def __init__(self, regplate, topspd):
        self.regplate = regplate
        self.topspd = topspd
        self.curspd = 0
        self.travdist = 0
    def accelerate(self, change):
        self.curspd = self.curspd + change
        if self.curspd > self.topspd:
            self.curspd = self.topspd
        if self.curspd < 0:
            self.curspd = 0
        return print(f"Tämän hetkinen nopeus {car.curspd} km/h")


car = Car("ABC-123", 142)
print(f"Rekisteritunnuksella {car.regplate} olevan auton huippunopeus {car.topspd} km/h, \n"
      f"tämän hetkinen nopeus {car.curspd} km/h ja kuljettu matka {car.travdist} km.")
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
car.accelerate(-200)


