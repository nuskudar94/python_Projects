class Celle:
    # Konstruktør
    def __init__(self):
        self._status="doed"
        self._naboer=[]
        self._ant_levende_naboer=0

    def sett_doed(self):
        self._status="doed"

    def sett_levende(self):
        self._status="levende"

    def legg_til_nabo(self, nabo):
        self._naboer.append(nabo)


    def er_levende(self):
        bool=True
        if self._status=="levende":
            bool=True
        else:
            bool=False
        return bool

    def hent_status(self):
        return self._status

    def hent_status_tegn(self):
        tegn="O"
        if self._status=="levende":
            tegn=tegn
        elif self._status=="doed":
            tegn="."

        return tegn

    def tell_levende_naboer(self):
        self._ant_levende_naboer=0
        for nabo in self._naboer:
            if nabo.er_levende() ==True:
                self._ant_levende_naboer+=1


        return self._ant_levende_naboer

    def oppdater_status(self):

            if self._status=="levende" :
                if self._ant_levende_naboer < 2 :
                    self.sett_doed()
                elif self._ant_levende_naboer > 3 :
                    self.sett_doed()

            else:

                if self._ant_levende_naboer == 3:
                    self.sett_levende()

    def __str__(self):
        return f'Celle(Status={self._status},Sanger={self._sanger})'
