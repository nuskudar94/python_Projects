#Lager bruker navn med fornavn og etternavn
def lagBrukernavn(full_navn):

    navn=full_navn.split(" ") #splitter med blank
    return navn[0].lower()+navn[1][0].lower()

lagBrukernavn("Kari Nordamn")
#lager epost ,tar to parameter
def lagEpost(bruker_navn,suffix):
    return bruker_navn+"@"+suffix

print(lagEpost("karin","outlook.com"))
# skriver ut eposter og tar et epost ordbok
def skrivUtEposter(epostBok):

    for element in epostBok.keys():
        print(lagEpost(element,epostBok[element]))

bok_epost={"olan":"ifi.uio.no","karin":"student.matnat.uio.no"}
skrivUtEposter(bok_epost)

bruker_ordbok={} #tom ordbok skal fylles med bruker

bruker_svar=input("Vil du fortsette?")
#while-løkke fortsetter om bruker svarer ja
while bruker_svar=="Ja":
    bruker_krav=input("Skriv en bokstav med i,p eller s")
    #om kravet er i,ny bruker lagres i ordbok
    if bruker_krav=="i":
        navn_fra_bruker=input("Skriv et navn")
        epost_suffix=input("Skriv epost suffix")
        uio_bruker_navn=lagBrukernavn(navn_fra_bruker)
        bruker_ordbok[uio_bruker_navn]=epost_suffix
        #print(bruker_ordbok)
    # om det er p ,får du epost
    elif bruker_krav=="p":
        skrivUtEposter(bruker_ordbok)
        #om det er s, sluttes programmet
    elif bruker_krav=="s":
        break


# bruker_svar = ""
# while bruker_svar != "s":
#     bruker_krav=input
