#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random
diceresult = 0

print("Heitän noppaa niin kauan kunnes saan määrittämäsi nopan suurimman suurimman silmäluvun")
dicesides = int(input("Anna nopan tahkojen määrä: "))


def noppa():
    return random.randint(1, dicesides)

result = noppa()
while result != dicesides:
    print("Heitän uudestaan")
    result = noppa()
    if result == dicesides:
        print(result)
        result = noppa()

        break