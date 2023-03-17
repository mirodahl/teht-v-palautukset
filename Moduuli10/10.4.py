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
car_table = PrettyTable()


class Car:
    car_count = 0

    def __init__(self, reg_plate, top_spd):
        self.reg_plate = reg_plate
        self.top_spd = top_spd
        self.cur_spd = 0
        self.trav_dist = 0
        Car.car_count += 1
        print(f"{Car.car_count}. Auto luotu, rekno: {reg_plate}, huippunopeus {top_spd}")

    def accelerate(self, change):
        self.cur_spd = self.cur_spd + change
        if self.cur_spd > self.top_spd:
            self.cur_spd = self.top_spd
        if self.cur_spd < 0:
            self.cur_spd = 0
        return self.cur_spd

    def travel(self, hours):
        change = self.cur_spd * hours
        self.trav_dist = self.trav_dist + change
        return self.trav_dist

    def __str__(self):
        return "{}".format(self.reg_plate)


class Race:
    def __init__(self, race_name, race_dist, cars):
        self.race_name = race_name
        self.race_dist = race_dist
        self.race_over = False
        self.cars = cars
        print(f"Kisa {race_name} aloitettu! Kisan pituus {race_dist} kilometriä.")

    def hour_pass(self):
        if self.race_over is False:
            for car in cars:
                car.accelerate(random.randint(-15, 10))
                car.travel(1)
                return self.race_finished()

    def race_finished(self):

        for car in cars:
            if car.trav_dist == self.race_dist:
                self.race_over = True
                print("Kilpailu ohi! Tässä tulokset:")
                print(str(f"Reg NO  | Top spd | Speed now | Total Distance"))
                print(str(f"{cars[0]}  | {float_top_spd[0]}   |   {float_cur_spd[0]}     |     {float_trav_dist[0]}"))
                print(str(f"{cars[1]}  | {float_top_spd[1]}   |   {float_cur_spd[1]}     |     {float_trav_dist[1]}"))
                print(str(f"{cars[2]}  | {float_top_spd[2]}   |   {float_cur_spd[2]}     |     {float_trav_dist[2]}"))
                print(str(f"{cars[3]}  | {float_top_spd[3]}   |   {float_cur_spd[3]}     |     {float_trav_dist[3]}"))
                print(str(f"{cars[4]}  | {float_top_spd[4]}   |   {float_cur_spd[4]}     |     {float_trav_dist[4]}"))
                print(str(f"{cars[5]}  | {float_top_spd[5]}   |   {float_cur_spd[5]}     |     {float_trav_dist[5]}"))
                print(str(f"{cars[6]}  | {float_top_spd[6]}   |   {float_cur_spd[6]}     |     {float_trav_dist[6]}"))
                print(str(f"{cars[7]}  | {float_top_spd[7]}   |   {float_cur_spd[7]}     |     {float_trav_dist[7]}"))
                print(str(f"{cars[8]}  | {float_top_spd[8]}   |   {float_cur_spd[8]}     |     {float_trav_dist[8]}"))
                print(str(f"{cars[9]} | {float_top_spd[9]}   |   {float_cur_spd[9]}     |     {float_trav_dist[9]}"))
                return
            else:
                self.race_over = False
                print("Kilpailu on vielä kesken.")
                self.live_situation()
                return self.hour_pass()

    def live_situation(self):

        if self.race_over is False:
            print(str(f"Reg NO  | Top spd | Speed now | Total Distance"))
            print(str(f"{cars[0]}  | {float_top_spd[0]}   |   {float_cur_spd[0]}     |     {float_trav_dist[0]}"))
            print(str(f"{cars[1]}  | {float_top_spd[1]}   |   {float_cur_spd[1]}     |     {float_trav_dist[1]}"))
            print(str(f"{cars[2]}  | {float_top_spd[2]}   |   {float_cur_spd[2]}     |     {float_trav_dist[2]}"))
            print(str(f"{cars[3]}  | {float_top_spd[3]}   |   {float_cur_spd[3]}     |     {float_trav_dist[3]}"))
            print(str(f"{cars[4]}  | {float_top_spd[4]}   |   {float_cur_spd[4]}     |     {float_trav_dist[4]}"))
            print(str(f"{cars[5]}  | {float_top_spd[5]}   |   {float_cur_spd[5]}     |     {float_trav_dist[5]}"))
            print(str(f"{cars[6]}  | {float_top_spd[6]}   |   {float_cur_spd[6]}     |     {float_trav_dist[6]}"))
            print(str(f"{cars[7]}  | {float_top_spd[7]}   |   {float_cur_spd[7]}     |     {float_trav_dist[7]}"))
            print(str(f"{cars[8]}  | {float_top_spd[8]}   |   {float_cur_spd[8]}     |     {float_trav_dist[8]}"))
            print(str(f"{cars[9]} | {float_top_spd[9]}   |   {float_cur_spd[9]}     |     {float_trav_dist[9]}"))
            return

###pääohjelma alkaa

#luodaan autot


for i in range(10):
    cars.append(Car("ABC- " + str(i+1), random.randint(100, 200)))

float_top_spd = [float(car.top_spd) for car in cars]
float_cur_spd = [float(car.cur_spd) for car in cars]
float_trav_dist = [float(car.trav_dist) for car in cars]

#kisan kulku funktio


def race_go():
    while race.race_over is False:
        race.hour_pass()
        return

#luodaan suuri romuralli


race = Race("Suuri romuralli", 8000, cars)

race_go()




