# Laget av Tobias Lekman Skjelland
# Dato: 24.09.24
# 2ITA

# lager en funksjon som jeg kaller på i if setningen under
def celsius_til_fahrenheit(celsius):                    
    return (celsius * 9/5) + 32
    # konvertere celsius til fahrenheit                         

def fahrenheit_til_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# input hvor bruker skal skrive celsius eller fahrenheit
valg = input("Vil du konvertere fra celsius til fahrenheit eller fahrenheit til celsius. Skriv c eller f:  ")   

# hvis bruker velger c (celsius) så kjører linjene under c
if valg == "c":
    celsius = float(input("Skriv inn temperaturen i Celsius: "))
    # input i float hvor bruker skal skrive inn temperatur i celsius
    fahrenheit = celsius_til_fahrenheit(celsius)
    # kaller på celsius funksjonen øverst
    print(f"{celsius} grader celsius tilsvarer {fahrenheit:.2f} grader fahrenheit")
    # printer ut resultat av celsius og fahrenheit utregningen utifra hva bruker skriver inn i input

# hvis ikke bruker velger c, men velger f (fahrenheit) så kjører linjene under f
elif valg == "f":
    fahrenheit = float(input("Skriv inn temperaturen i fahrenheit: "))
    celsius = fahrenheit_til_celsius(fahrenheit)
    print(f"{fahrenheit} grader fahrenheit tilsvarer {celsius:.2f} grader celsius")
        
# hvis ikke bruker skriver inn c eller f så kjører denne printen
else:   
    print("Ugydlig valg, du må skrive 'celsius eller fahrenheit' ")
    # hvis bruker skriver noe annent enn c eller f så er det ugyldig

