# Laget av Tobias Lekman Skjelland
# Dato: 24.09.24
# 2ITA

import math                                                         # importerer math modulen fordi jeg skal bruke math.pi

h = int(input("Skriv inn høyde: "))                                 # bruker skriver inn høyde
b = int(input("Skriv inn din bredde: "))                            # bruker skriver inn bredde

def areal_rektangel(h, b):                                          # definerer def funksjonen med parametere h og b
    return h * b                                                    # returnerer areal ved å gange høyde med bredde


areal = areal_rektangel(h, b)                                       # deklarerer variabelen areal med parametere h oh b
print("Areal av rektangel = ", areal)                               # printer ut areal av rektangel til bruker

def areal_sirkel(r):                                                # definerer def funksjonen med parameteren r
    return math.pi * r * r                                          # regner ut areal av sirkel med pi

sirkel_radius = int(input("Skriv inn radiusen til sirkel: "))       # input hvor bruker skal skrive inn radius til sirkel

a_sirkel = areal_sirkel(sirkel_radius)                              # deklarerer variabelen a_sirkel som jeg kaller på igjen i printen
print("Areal av sirkel = ", a_sirkel)                               # printer areal av sirkel hvor jeg legger inn variabelen a_sirkel i printen

