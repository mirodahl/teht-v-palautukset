#Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa
# sitä vastaavan säätilan tekstin
# sekä lämpötilan Celsius-asteina. Perehdy rajapinnan dokumentaatioon riittävästi.
# Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

#api call: https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
#api a2061d23796da1bbbaa2a3443766ed9d

import requests
import json

search = input("Anna haettava paikkakunta: ")

try:
        request = "https://api.openweathermap.org/data/2.5/weather?q="+search+"&units=metric&appid=5b78d00bef03aee5575482775fdca0e9"
        answer = requests.get(request).json()
        #print(answer)
        print(json.dumps(f"Current Weather: {answer['weather'][0]['description']}"))
        print(json.dumps(f"Temperature: {answer['main']['temp']}c"))
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")