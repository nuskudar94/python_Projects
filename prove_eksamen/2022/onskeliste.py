from onske import Onske

class Onskeliste:
    def __init__(self):
        self._onske_liste=onske_liste[]


    def nytt_onske(self,beskrivelse,antall,minpris):
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
