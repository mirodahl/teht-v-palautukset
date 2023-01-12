##säteestä pinta-ala A= pi r potenssiin 2
import math
#pi = 3.14

r = input("Anna ympyrän säde: ")
r = int(r)

area = math.pi * r * r
area = str(area)

print("Ympyrän pinta-ala on:" + area )