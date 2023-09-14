from motorsykkel import Motorsykkel

def hovedprogram():
    obj1 = Motorsykkel(0,"Toyota",564356)
    obj2 = Motorsykkel(0,"Ford",34534)
    obj3 = Motorsykkel(0,"Tesla",345345)

    obj1.skriv_ut()
    #assert obj1.hent_kilometerstand()==6
    obj2.skriv_ut()
    obj3.skriv_ut()

    obj3.kjor(10)
    print(obj3.hent_kilometerstand())
    obj3.skriv_ut()

hovedprogram()
