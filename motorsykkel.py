class Motorsykkel:

    def __init__(self,km,merke,reg_Nummer):

        self._km=0
        self._merke=merke
        self._reg_Nummer=reg_Nummer

    def kjor(self,km):
        self._km=+km

    def hent_kilometerstand(self):
        return self._km

    def skriv_ut(self):
        print()
        print(self._merke)
        print(self._reg_Nummer)
        print(self._km)
        print()
