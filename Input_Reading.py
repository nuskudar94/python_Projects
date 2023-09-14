"""Vi har en navnAlder.txt fil. Definer en funksjon som tar en parameter som er text filen.
 Vi skal lage en ordbok.navn er nøkkelverdien, alder er innholdverdien.
 Programmet returnerer alderen i ordboken   """
def navn_alder(navn_filen):

    navn_bok={}
    min_fil=open(navn_filen)

    for linje in min_fil:

        biter =linje.split(",")
        navn=biter[0]
        alder=int(biter[1])

        navn_bok[navn]=alder

    return navn_bok.values()

print(navn_alder("navnAlder.csv"))
