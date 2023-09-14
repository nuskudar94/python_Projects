
#Addisjon funksjonen
def addisjon (num1,num2) :
    return num1 + num2
#subtraksjon funksjonen
def subtraksjon (num1,num2) :
    return num2 - num1
#Divisjon funksjonen
def divisjon (num1,num2) :
    return num1 / num2

assert addisjon(5,3) == 8
assert addisjon(-5,-3) == -8
assert addisjon(5,-3) == 2

assert subtraksjon(4,5) == 1
assert subtraksjon(-4,-5) == -1
assert subtraksjon(4,-5) == -9

assert divisjon(15,3) == 5
assert divisjon(-15,-3) == 5
assert divisjon(15,-3) == -5

def tommerTilCm (antallTommer) :
    #assert sjekker om tommer er større
    assert antallTommer > 0, "antallTommer må være større enn 0"
    return  (antallTommer)*(2.54)

assert tommerTilCm(5) == 12.70

#funksjonen beregner og skriver ut resultater
def skrivBeregninger():
    print("Utregnninger:")
    tall1=float(input("Skriv inn tall 1: "))
    tall2=float(input("Skriv inn tall 2: "))

    print("Resultat av summering: ",addisjon(tall1,tall2))
    print("Resultat av subtraksjon: ",subtraksjon(tall1,tall2))
    print("Resultat av divisjon: ",divisjon(tall1,tall2))

    print("Konvertering fra tommer til cm:")
    tall3=float(input("Skriv inn et tall: "))
    print("Resultat",tommerTilCm(43))
#assert sjekker om det fungerer greit
assert skrivBeregninger(), "Fungerer greit"
