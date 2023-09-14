from hund import Hund
#Tester Hund klassen
def hovedprogram():
    max = Hund(5,15) #oppretter et objekt fra HUnd klasse

    #Kaller metoder 
    max.spis(5)
    print(max.hent_vekt())
    max.spis(2)
    print(max.hent_vekt())
    max.spring()
    print(max.hent_vekt())
    max.spring()
    print(max.hent_vekt())
    # max.spis(5)
    # print(max.hent_vekt())
    # max.spis(2)
    # print(max.hent_vekt())

hovedprogram()
