##Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja
##tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
##Tehtävässä on käytettävä if/elif/else-toistorakennetta.

##LUX on parvekkeellinen hytti yläkannella.
##A on ikkunallinen hytti autokannen yläpuolella.
##B on ikkunaton hytti autokannen yläpuolella.
##C on ikkunaton hytti autokannen alapuolella.
##Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.

print("Tervetuloa laivalle!")
print("Meillä on seuraavat hyttiluokat tarjolla: LUX, A, B ja C")
print("LUX on parvekkeellinen hytti yläkannella")
print("A on ikkunallinen hytti autokannen yläpuolella")
print("B on ikkunaton hytti autokannen yläpuolella")
print("C on ikkunaton hytti autokannen alapuolella")

cabin_class = input("Ole hyvä ja valitse mieleisesi hyttiluokka: ")

print("Kiitos valinnastasi!") if input == "LUX" or "A" or "B" or "C" else print("Virheellinen hyttiluokka!")

#if input == "LUX" or "A" or "B" or "C":
#    print("Kiitos valinnastasi!")
#    else:
#    print("Virheellinen hyttiluokka!")