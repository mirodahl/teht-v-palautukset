#Kirjoita while-toistorakennetta käyttävä ohjelma,
# joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

number = 1
times = 1000
print("Tulostetaan kolmella jaollisia lukuja")
while number <= times:
    number = number + 1
    if number % 3 == 0:
        print(f"{number}")
