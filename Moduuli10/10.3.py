#Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi
# palohälytys,
# joka käskee kaikki hissit pohjakerrokseen.
# Jatka pääohjelmaa siten, että talossasi tulee palohälytys.
import random
class Elevator:
    fire_alarm = False
    def __init__(self, lowest, uppest):
        self.lowest = lowest
        self.uppest = uppest
        self.floor = lowest
        print(f"Hissi luotu, alin kerros: {lowest}, ylin kerros: {uppest}")

    def floor_up(self):
        self.floor = self.floor + 1
        print(f"Hissi on kerroksessa {self.floor}")
        return

    def floor_down(self):
        self.floor = self.floor - 1
        print(f"Hissi on kerroksessa {self.floor}")
        return

    def go_floor(self, new_floor):
        # siirrytään ylöspäin
        while new_floor > self.floor:
            if new_floor >= self.uppest:
                new_floor = self.uppest
                #print("Hissi on ylimmässä kerroksessa.")
            self.floor_up()
        # siirrytään alaspäin
        while new_floor < self.floor:
            if new_floor <= self.lowest:
                new_floor = self.lowest
                #print("Hissi on alimmassa kerroksessa.")
            self.floor_down()
        print(f"Hissi on saapunut kerrokseen {self.floor}")
        print("Hissi on perillä.")
        return

class House:

    def __init__(self, lowest, uppest, floors):
        # luodaan lista talon hissejä varten
        self.elevators = []
        # luodaan uudet hissit ja lisätään ne listaan
        for nro in range(floors):
            elevator = Elevator(lowest, uppest)
            # hissit menevät nyt listassa indekseihin 1, 2, 3, ...
            self.elevators.insert(nro+1, elevator)
    def house_elevator_go(self, elevator_no, destination):
        if elevator_no in self.elevators:
            Elevator.go_floor(destination)
        else:
            print("Kai sinä tiedät kuinka monta hissiä sinulla on...")

    def firealarm(self):
        firesensor = random.randint(1, 5)
        if firesensor == 5:
            fire_alarm = True
            if fire_alarm == True:
                print("Palohälytys! Kaikki hissit palaavat automaattisesti alimpaan kerrokseen!")
                for elevator in range(self.elevators):
                    Elevator.go_floor(elevator.lowest)


house = House(1, 5, 5)
house.house_elevator_go(1, 1)