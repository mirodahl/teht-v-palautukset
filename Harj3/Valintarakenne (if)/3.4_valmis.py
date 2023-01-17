##Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
##Vuosi on karkausvuosi, jos se on jaollinen neljällä.
##Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.
year = int(input("Anna vuosiluku: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Annettu vuosi oli karkausvuosi.")
else:
    print("Annettu vuosi ei ole karkausvuosi")


#JOS
#vuosi on jaollinen 400: lla, niin vuosi ON karkausvuosi
#MUUTEN JOS
#vuosi on jaollinen 100: lla, niin vuosi EI OLE karkausvuosi
#MUUTEN JOS
#vuosi on jaollinen 4: llä, niin vuosi ON karkausvuosi
#MUUTEN
#vuosi EI OLE karkausvuosi

#'''
#Eri vuosilukuja, joilla voit testata koodiasi:
#2000: ON
#1900: EI ole
#2023: EI ole
#2024: ON
#'''