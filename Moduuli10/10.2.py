#Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
# Hissien lista tallennetaan talon ominaisuutena.
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.
class House:

    def __init__(self, lowest, uppest, floors):
        # luodaan lista talon hissejä varten
        self.elevators = []
        # luodaan uudet hissit ja lisätään ne listaan
        for nro in range(floors):
            elevator = Elevator(lowest, uppest)
            # hissit menevät nyt listassa indekseihin 1, 2, 3, ...
            self.elevator.insert(nro+1, elevator)