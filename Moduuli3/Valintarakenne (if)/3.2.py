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
print("Ole hyvä ja valitse mieleisesi hyttiluokka")
get_cabinclass = int(input("1 = LUX, 2 = A, 3 = B tai 4 = C: "))
if int(get_cabinclass) == (1 or 2 or 3 or 4):
 print("Kiitos valinnastasi!")
elif int(get_cabinclass) > 4:
 print("Virheellinen hyttiluokka!")

#muokattu or lauseke joka ei noudattanut syntaksia, palautteen perusteella