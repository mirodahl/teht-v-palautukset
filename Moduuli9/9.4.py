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
class Car:

    car_count = 0
    def __init__(self, regplate, topspd):
        Car.car_count += 1
        print(f"{Car.car_count}. Auto luotu, rekno: {regplate}, huippunopeus {topspd}")
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
        return
    def travel(self, hours):
        change = self.curspd * hours
        self.travdist = self.travdist + change
        return


cars = []
for i in range(10):
    cars.append(Car("ABC- " + str(i+1), random.randint(100, 200)))

while cars.travdist < 1000:
    for i in range(10):
        cars.accelerate(random.randint -10, 15)