#Toteuta seuraava luokkahierarkia Python-kielellä:
# Julkaisu voi olla kirja tai lehti.
# Jokaisella julkaisulla on nimi.
# Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
# Kirjoita luokkiin myös tarvittavat alustajat.
# Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot.
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä)
# ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.
books = []
magazines = []
class Publish:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        print(f"Teos {name} luotu.")

class Magazine(Publish):
    magazine_count = 0
    def __init__(self, name, author):
        Magazine.magazine_count += 1
        Publish.__init__(self, name, author)

    def mag_details(self):
        for magazine in magazines:
            return print(f"Lehden nimi: {self.name}, Päätoimittaja {self.author}")


class Book(Publish):
    book_count = 0
    def __init__(self, name, author, pages):
        Book.book_count += 1
        Publish.__init__(self, name, author)
        self.pages = pages

    def book_details(self):
        for book in books:
            return print(f"Kirjan nimi: {self.name}, Kirjailija {self.author}, Sivujen lkm; {self.pages}")

books.append(Book("Hytti n:o 6", "Rosa Liksom", 200))
magazines.append(Magazine("Aku Ankka", "Aki Hyyppä"))

for book in books:
    book.book_details()

for magazine in magazines:
    magazine.mag_details()
