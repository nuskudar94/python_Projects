class Onske:
    def __init__(self,beskrivelse,antall,minpris):
        self._beskrivelse=beskrivelse
        self._antall=antall
        self._minpris=minpris


    def passer(self,maxpris):
        bool=True
        if self._minpris > maxpris or self._antall==0:
            bool=bool
        else :
            bool=False

        return bool


    def valgt(self):
        self._antall=-1

        return self._beskrivelse


    def __str__(self):

        return self._beskrivelse, self._minpris
