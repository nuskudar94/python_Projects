from dato import Dato
#metoden tester Dato klassen
def hovedprogram():
    #oppretter dato objekt
    dato1 = Dato(15,10,2022)
    #printer år
    print(dato1.hent_aar())

    #sjekker bestemt dato
    if dato1.sjekkDag(15):
        print("Loenningsdag")
    elif dato1.sjekkDag(1):
        print("Ny maaned,mye muligheter")
    #lagrer datoen og printer det
    datoen = dato1.lagDato()
    print(datoen)
hovedprogram()
