import math  ##tuodaan tarvittu kirjasto

def laske_ala(r):
    return math.pi * r * r  ##säteestä pinta-ala A= pi r potenssiin 2

def main():
    print("Lasketaan ympyrän pinta-alan antamasi säteen avulla.")
    sade = input("Syota sade. \n")
    sade = float(input) ##borkee tässä kohtaa

    ala = laske_ala(sade)
    print("Ympyrän pinta-ala on %.4f.")
    sade = input("Syota sade. \n")
    sade = float(input)

main()