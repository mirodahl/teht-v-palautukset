#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes
# käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm
app_running = True
print("Muunnetaan tuumia senttimetreiksi!")
print("Voit lopettaa ohjelman antamalla negatiivisen tuumamäärän.")
conversion = int(input("Syötä muunnettava tuumamäärä: "))
cents = int(conversion) * 2.54
print(f"Annettu määrä sentteinä on {cents}")
while int(conversion) > 0:
    if conversion > 0:
        conversion = int(input("Syötä muunnettava tuumamäärä: "))
        cents2 = int(conversion) * 2.54
        print(f"Annettu määrä sentteinä on {cents2}")
    else:
        print("Näkemiin")
        app_running = False