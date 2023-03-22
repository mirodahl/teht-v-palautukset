#Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
# Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
# Käyttäjälle on näytettävä pelkkä vitsin teksti.

#HTTP-yhteyskäytäntö määrittelee viisi pyynnöissä yleisesti käytettyä operaatiota:
#GET lukee sisältökohteen
#PUT korvaa olemassa olevan sisältökohteen
#POST luo uuden sisältökohteen
#PATCH muokkaa olemassa olevaa sisältökohdetta
#DELETE poistaa olemassa olevan sisältökohteen

import requests
import json

try:
        request = "https://api.chucknorris.io/jokes/random"
        answer = requests.get(request).json()
        print(json.dumps(answer['value']))
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")