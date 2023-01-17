##Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
##Vuosi on karkausvuosi, jos se on jaollinen neljällä.
##Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.
year = int(input("Anna vuosiluku: "))

if int(year) / 400 == 0:
    print("Vuosi on karkausvuosi")
elif int(year) / 100 == 0:
    print("Vuosi ei ole karkausvuosi")
elif int(year) / 4 == 0:
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")


#JOS
#vuosi on jaollinen 400: lla, niin vuosi ON karkausvuosi
#MUUTEN JOS
#vuosi on jaollinen 100: lla, niin vuosi EI OLE karkausvuosi
#MUUTEN JOS
#vuosi on jaollinen 4: llä, niin vuosi ON karkausvuosi
#MUUTEN
#vuosi EI OLE karkausvuosi