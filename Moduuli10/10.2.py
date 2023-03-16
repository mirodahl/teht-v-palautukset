#Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
# Hissien lista tallennetaan talon ominaisuutena.
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.
class Elevator:

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
            self.elevator.insert(nro+1, elevator)

    def elevator_go(self, elevator_no, destination_floor):
        for i in range(destination_floor):


house = House(1, 5, 5)