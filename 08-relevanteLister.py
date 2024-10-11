# Laget av Tobias Lekman Skjelland
# Dato: 4.10.24
# 2ITA

gangetabell = []

while True:                                                    
    try: 
        tall = int(input("Oppgi et tall fra 1 til 10: "))                     # Be brukeren om å oppgi et tall mellom 1 og 10

        if tall < 1 or tall > 10:                                             # Sjekk om tallet er utenfor gyldig rekkevidde
            print("Tallet må være mellom 1 og 10")
            continue                                                          # hvis tallet er ugyldig, så starter løkken på nytt            

        for i in range(1, 11):                                                # Gå gjennom tallene fra 1 til 10
            resultat = tall * i                                               # Regner ut resultatet av gangestykket
            gangetabell.append(resultat)                                      # Legg til resultatet i gangetabell listen

        print("Her er", tall, "gangen:")                                      # Skriv ut overskriften for gangetabellen
        for resultat in gangetabell:                                          # Gå gjennom hvert resultat
            print(resultat)                                                   # Skriv ut hvert resultat

    except ValueError:                                                        # Hvis brukeren skriver noe annet enn et tall
        print("Du må skrive et tall")                                         # Printer ut en feilmelding                            

    break                                                                     # Avslutter løkken