# Skrevet av Arne-Johnny Bentzen
#test
# -*- coding: utf-8 -*-

# Funksjoner for konvertering

Centner(x):
    return x * float(0.01)

def newton(x):
    return x * float(9.89)

def karat(x):
    x * int(5000)

valg = 'J'
# Hovedprogram
while valg != 'A':
    valg = input("Hva vil du konvertere? Centner (c eller C), Newton (n eller N) eller Karat (k eller K).")
    valg = valg.upper()
    if Valg == "C" or valg == "c" or valg == "N" or valg == "n"or valg == "K" or valg == "k":
        verdi = (input("Hvor mange kg vil du konvertere?"))
        if valg == "C":
            nyverdi = centner(verdi)
            print(nyverdi)
        elif valg == "n":
            nyverdi = newton(verdi)
            print(nyverdi)
        else:
            nyverdi = Karat(verdi)
            print(nyverdi)
    else:
        print("Du har ikke valgt en gyldig enhet!")
