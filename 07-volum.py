# Laget av Tobias Lekman Skjelland
# Dato: 24.09.24
# 2ITA

# lager en function som jeg kaller volum_kalk hvor jeg legger inn ett parameter som jeg kaller bruker_hoyde
def volum_kalk(bruker_hoyde):        
    # ganger med 2 høyde sider
    a4_bredde = 21 - bruker_hoyde * 2
    a4_lengde = 29.7 - bruker_hoyde * 2

    if a4_bredde <= 0 or a4_lengde <= 0:
        return 0
    
    volum = a4_bredde * a4_lengde * bruker_hoyde
    # returnerer volum
    return volum    

#
bruker_hoyde = float(input("Skriv inn ønsket høyde på esken: "))

volum = volum_kalk(bruker_hoyde)
print(f"Volumet av esken med høyde {bruker_hoyde:.1f} cm er: {volum:.2f} cm3")

# spør bruker om de vil se optimal høyde for maks volum på esken
se_optimal = input("Vil du se optimal høyde for maks volum? (ja/nei): ")                

# hvis bruker skriver ja så kjører denne if setningen også kjører while løkken under
if se_optimal.lower() == "ja":      # hvis bruker skriver ja
    optimal_hoyde = 0               # starter på null
    maks_volum  = 0                 # starter på null

    hoyde = 0.1                     # starter med minimum

while hoyde <= 10.5:                # gjør om høyde til maks høyde
    volum = volum_kalk(hoyde)       # kaller på volum_kalk funksjonen hvor det regnes ut volum til esken

    if volum > maks_volum:      
        maks_volum = volum
        optimal_hoyde = hoyde

    hoyde += 0.1

# printer ut den optimale høyden hvor jeg kaller på optimal_hoyde
print(f"Den optimale høyden for maksimal volum er {optimal_hoyde:.1f} cm")
print(f"Maksimalt volum er: {maks_volum:.2f} cm3")






