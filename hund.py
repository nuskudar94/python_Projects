class Hund:
    #Konstruktøren initialiserer alder,metthet og vekt
    def __init__(self,alder,vekt):
        self._metthet=10
        self._alder=alder
        self._vekt=vekt

    #metoden henter alder
    def hent_alder(self):
        return self._alder
    #Henter vekt
    def hent_vekt(self):
        return self._vekt

    #modifiserer metthet og vekt
    def spring(self):
        self._metthet -=1

        if self._metthet < 5:
            self._vekt -= 1

    #modifiserer metthet og vekt 
    def spis(self,tall):
        self._metthet += tall

        if self._metthet > 7 :
            self._vekt +=1
