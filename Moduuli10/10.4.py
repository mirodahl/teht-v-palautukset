#Tehtävä on jatkoa aiemmalle autokilpailutehtävälle.
# Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä
# ja osallistuvien autojen lista.
# Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan
# ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

#tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein
# tehtävät toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle
# kulje-metodia.

#tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi
# muotoiltuna.

#kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut
# vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.

#Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
# Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia,
# jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
# Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein
# sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.

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

class Race:
    def __init__(self,racename, racedist, cars):
        self.racename = racename
        self.racedist = racedist
        self.race_over = False
        self.cars = cars
        print(f"Kisa {racename} aloitettu! Kisan pituus {racedist} kilometriä.")

    def hour_pass(self):
        if not self.race_over == True:
            for car in cars:
                car.accelerate(random.randint(-15, 10))
                car.travel(1)
                return
    def race_finished(self):
        for car in cars:
            if car.travdist == self.racedist:
                self.race_over = True
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
                # cartable.reversesort = True
                print("Kilpailu ohi!")
                print(cartable.get_string(sortby="Travelled distance"))
            else:
                self.race_over = False
                print("Kilpailu on vielä kesken.")
                return race.live_situation
    def live_situation(self):
        if not self.race_over == True:
            # prettytable taulukko
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
            # cartable.reversesort = True
            return print(cartable.get_string(sortby="Travelled distance"))

###pääohjelma alkaa

#luodaan autot
for i in range(10):
    cars.append(Car("ABC- " + str(i+1), random.randint(100, 200)))

#muutetaan intit floateiksi prettytablelle
float_topspd = [float(car.topspd) for car in cars]
float_curspd = [float(car.curspd) for car in cars]
float_travdist = [float(car.travdist) for car in cars]

#luodaan suuri romuralli
race = Race("Suuri romuralli", 8000, cars)