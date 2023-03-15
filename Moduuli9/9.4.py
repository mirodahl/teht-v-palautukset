#Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
# Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
# Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

#Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
# Tämä tehdään kutsumalla kiihdytä-metodia.
#Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
#Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
import random
from prettytable import PrettyTable

cars = []
cardist = []
cartable = PrettyTable()
class Car:
    car_count = 0
    def __init__(self, regplate, topspd):
        self.regplate = regplate
        self.topspd = topspd
        self.curspd = 0
        self.travdist = 0
        Car.car_count += 1
        print(f"{Car.car_count}. Auto luotu, rekno: {regplate}, huippunopeus {topspd}")
    def accelerate(self, change):
        self.curspd = self.curspd + change
        if self.curspd > self.topspd:
            self.curspd = self.topspd
        if self.curspd < 0:
            self.curspd = 0
        return self.curspd
    def travel(self, hours):
        change = self.curspd * hours
        self.travdist = self.travdist + change
        return self.travdist
    def __str__(self):
        return "{}".format(self.regplate)
#    def race(self, distance):
#        for car in cars:
#            while distance <= 10000:
#                car.accelerate(random.randint(-15, 10))
#                car.travel(1)
#                print(f"Auto {car.regplate}, nykyinen nopeus {car.curspd}, kuljettu matka {car.travdist}")




def race():
    race_over = False
    while not race_over:
        for car in cars:
            car.accelerate(random.randint(-15, 10))
            car.travel(1)
            if car.travdist == 10000:
                race_over = True



#luodaan autot
for i in range(10):
    cars.append(Car("ABC- " + str(i+1), random.randint(100, 200)))

#kisataan!
race()

#muutetaan intit floateiksi prettytablelle
float_topspd = [float(car.topspd) for car in cars]
float_curspd = [float(car.curspd) for car in cars]
float_travdist = [float(car.travdist) for car in cars]

#prettytable taulukko
cartable.field_names = ["Registerplate", "Top speed", "Current speed", "Travelled distance"]
cartable.add_rows(
    [
        [cars[0], float_topspd[0], float_curspd[0], float_travdist[0]],
        [cars[1], float_topspd[1], float_curspd[1], float_travdist[1]],
        [cars[2], float_topspd[2], float_curspd[2], float_travdist[2]],
        [cars[3], float_topspd[3], float_curspd[3], float_travdist[3]],
        [cars[4], float_topspd[4], float_curspd[4], float_travdist[4]],
        [cars[5], float_topspd[5], float_curspd[5], float_travdist[5]],
        [cars[6], float_topspd[6], float_curspd[6], float_travdist[6]],
        [cars[7], float_topspd[7], float_curspd[7], float_travdist[7]],
        [cars[8], float_topspd[8], float_curspd[8], float_travdist[8]],
        [cars[9], float_topspd[9], float_curspd[9], float_travdist[9]],
    ]
)

print(cartable)