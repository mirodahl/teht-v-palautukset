#Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan
# tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
# Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

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
    def travel(self, hours):
        change = self.curspd * hours
        self.travdist = self.travdist + change
        return print(f"Mittarilukema: {car.travdist}")


car = Car("ABC-123", 142)
print(f"Rekisteritunnuksella {car.regplate} olevan auton huippunopeus {car.topspd} km/h, \n"
      f"tämän hetkinen nopeus {car.curspd} km/h ja kuljettu matka {car.travdist} km.")

car.accelerate(20)
car.travel(1.5)
car.accelerate(30)
car.travel(1)
