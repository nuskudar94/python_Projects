def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)

def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print (b)
    print (a)

hovedprogram()

"""
Programmet kaller funksjonen hovedprogram først, kompileren begynner med hovedprogram,opprettes a,b.Også skriver ut b som er 0.
b blir like a, begge to blir 42. programmet kaller minFunksjon som ikke tar parameter.For-løkken defineres som itererer 3 ganger.
C defineres på linje 3, skrives ut på linje 4, legges 1 til c på linje 5.b defineres som 10.På linje 7 gir programmet feilmelding at a ikke er definert i funksjonen
Det vil si NameError, og programmet slutter.
"""
