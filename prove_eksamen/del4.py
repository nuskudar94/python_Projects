class Emne:
    def __init__(self,emnekode,studenter,rettere):
        self._emnekode=emnekode
        self._studenter_ordbok=studenter
        self._rettere=rettere
        self._obliger={}


    def administer(self):
        print(self._emnekode)
        meny=input("Svar med kode her\
        O: Ny oblig \
        F: Frist ute, start retting \
        L: Lag eksamensliste \
        A: Avslutt").upper().strip()

    def _opprettOblig(self):
        gi_frist=input("Gi frist på formen ååmmdd")
        oblignavn= "oblig" +


class Student:

    def __init__(self,bruker_navn,fullt_navn):
        self._bruker_navn=bruker_navn
        self._fullt_navn=fullt_navn
        self._resultater={}

    def register(self,oblig,resultat):

        self._resultater[oblig]=resultat


    def altGodkjent(self,antObliger):
        verdi=True
        for resultat in self._resultater.values():
            if resultat == 1 :
                verdi=verdi
            else:
                verdi=False

        return verdi


class Retter :
    def __init__(self,brukern_retter):
        self._brukern_retter=brukern_retter


    def vurder(self,besvarelse_fil):
        return 1

class Oblig:
    def __init__(self,oblig_id,leverings_frist):
        self._oblig_id=oblig_id
        self._leverings_frist=leverings_frist
        self._rettet=False

    def fordelRetting(besvarelser_ordbok,retter_liste):
        Retter.vurder()


    def klarForRetting(self,idag_dato):
        if self._leverings_frist < idag_dato and self._rettet == False:
            return True
        else:
            return False

    def hentBesvarelser(self,fil_besvar):
        besvar_ordbok={}
        apne_fil=open(fil_besvar)

        for linje in apne_fil:
            data=linje.split()
            if len(data)>1:
                besvar_ordbok[data[0]]=data[1]

        return besvar_ordbok
