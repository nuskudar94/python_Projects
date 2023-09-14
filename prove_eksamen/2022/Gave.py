from onske import Onske

class Onskeliste:
    def __init__(self):
        self._onske_liste=onske_liste[]


    def nytt_onske(self,onske,beskrivelse,antall,minpris):
        onske=Onske(beskrivelse,antall,minpris)
        self._onske_liste.append(onske)


    def hent_onsker(self,makspris):
        ny_liste=[]
        for onske in self._onske_liste:
            if onske.passer(makspris):
                ny_liste.append(str(onske))
            else:
                ny_liste.append("Ikke valgbart")

        return ny_liste
    def onske_oppfylles(tall):
        return self._onske_liste[tall].valgt()

class Gave:
    def __init__(self,beskrivelse,giver):
        self._beskrivelse=beskrivelse
        self._giver=giver


    def __str__(self):
        return self._giver , self._beskrivelse


class Juleferiekalender:
    def __init__(self,antall_dager):
        self._antall_dager = antall_dager
        dag_nr=25
        self._gave_ordbok={}

        for i in range(antall_dager):
            self._gave_ordbok[dag_nr]=None
            dag_nr+=1
            if dag_nr==32:
                dag_nr=1

    def ny_gave(self,beskrivelse,giver,dagen):
        self._gave_ordbok[dagen]=Gave(beskrivelse,giver)

    def hent_dagens_gave(self,dagnummer):
        gave= self._gave_ordbok[dagnummer]
        if gave =! None:
            if 1 > dagnummer < 25:
                return dagnummer, ".Januar", str(gave)
            if 24 < dagnummer > 32 :
                return dagnummer, ".desember", str(gave)

        else:
            return "Det er ikke på den dagen"

    def hent_ant_dager(self):
        return len(self._gave_ordbok)

class Julegavefikser:
    def __init__(self,antall_dager):

        self._juleferiekalender=Juleferiekalender(antall_dager)
        self._onskeliste=Onskeliste()
        self._neste_dag=25


    def les_onsker_fra_filen(self,filnavn):
        open_fil=open(filnavn)
        for linje in open_fil:
            liste=linje.strip().split(";")
            self._onskeliste.nytt_onske(liste[0],liste[1],liste[2])



    def velg_gave(self,giver):
        maxpris=int(input("Hva er maxpris for deg ?"))
        tilpasset_onsker=self._onskeliste.hent_onsker(maxpris)
        tall=int(input("Hvilket tall vil du velge"))
        gave=self._onskeliste.onske_oppfylles(tall)

        dag=int(input("Hvilken dag med nummer vil du gi gaven ?"))
        self._juleferiekalender.ny_gave(tall,giver,dag)

    def ny_dag(self):
        info_gave=self._juleferiekalender.hent_dagens_gave(self._neste_dag)
        self._neste_dag+=1
        if self._neste_dag==32:
            self._neste_dag=1

        return info_gave
