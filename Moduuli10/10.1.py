#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen
# numeron. Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas.
# Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
# metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa,
# että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat,
# missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten,
# että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja
# sen jälkeen takaisin alimpaan kerrokseen.
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

elevator = Elevator(1, 10)
elevator.go_floor(5)
elevator.go_floor(7)
elevator.go_floor(1)
