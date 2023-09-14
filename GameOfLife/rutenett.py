from random import randint
from celle import Celle

class Rutenett:
    def __init__(self, rader, kolonner):
        self._ant_rader=rader
        self._ant_kolonner=kolonner
        self._rutenett=[]
        self._lag_tomt_rutenett()

    def _lag_tomt_rutenett(self):
        for i in range(self._ant_rader):
            self._rutenett.append(self._lag_tom_rad())

    def _lag_tom_rad(self):
        tom_rad_liste=[]
        for i in range(self._ant_kolonner):
            tom_rad_liste.append(None)

        return tom_rad_liste

    def fyll_med_tilfeldige_celler(self):
        for rad1 in range(self._ant_rader):
            #self.lag_celle(self._ant_rader,self._ant_kolonner)
            for kolon1 in range(self._ant_kolonner) :
                self.lag_celle(rad1,kolon1)

    def lag_celle(self, rad, kol):
        celle1 = Celle()

        var1 = randint(0,2)

        if var1 == 1:
            celle1.sett_levende()
        else:
            celle1.sett_doed()

        self._rutenett[rad][kol]=celle1

    def hent_celle(self, rad, kol):
        # celle1 =None
        # try:
        #     celle1=self._rutenett[rad][kol]
        # except IndexError:
        #     celle1=None


        # if rad <= self._ant_rader and rad >= 0 and kol > 0 and kol<=self._ant_kolonner:
        #     celle1=self._rutenett[rad][kol]
        # else:
        #     celle1=None
        celle1=None
        if rad not in range(self._ant_rader):
            celle1=None
        elif kol not in range(self._ant_kolonner):
            celle1=None
        else:
            celle1=self._rutenett[rad][kol]

        return celle1

    def tegn_rutenett(self):
        for rad in self._rutenett:
            for celle in rad:
                print(celle.hent_status_tegn(),end=" ")
            print()
    def _sett_naboer(self, rad, kol):
        celle1 =self.hent_celle(rad,kol)
        nabo=self.hent_celle(rad-1,kol-1)
        if nabo is not None :
            celle1.legg_til_nabo(nabo)
        nabo=self.hent_celle(rad-1,kol)
        if nabo is not None :
            celle1.legg_til_nabo(nabo)
        nabo=self.hent_celle(rad-1,kol+1)
        if nabo is not None :
            celle1.legg_til_nabo(nabo)
        nabo=self.hent_celle(rad,kol-1)
        if nabo is not None :
            celle1.legg_til_nabo(nabo)
        nabo=self.hent_celle(rad,kol+1)
        if nabo is not None :
            celle1.legg_til_nabo(nabo)
        nabo=self.hent_celle(rad+1,kol-1)
        if nabo is not None :
            celle1.legg_til_nabo(nabo)
        nabo=self.hent_celle(rad+1,kol)
        if nabo is not None :
            celle1.legg_til_nabo(nabo)
        nabo=self.hent_celle(rad+1,kol+1)
        if nabo is not None :
            celle1.legg_til_nabo(nabo)




            # nabo1=self.hent_celle(rad-1,kol-1)
            # celle1.legg_til_nabo(nabo1)




    def koble_celler(self):
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner) :
                self._sett_naboer(rad,kol)

    def hent_alle_celler(self):
        celle_lister=[]
        for rad in self._rutenett:
            for kol in rad:
                celle_lister.append(kol)

        return celle_lister


    def antall_levende(self):
        antall_levende_celler=0
        for rad in self._rutenett:
            for kol in rad:
                if kol.er_levende():
                    antall_levende_celler+=1

        return antall_levende_celler


class Verden:
    def _init_(self, rader, kolonner):
        self._generasjonsnummer = 0
        self._rutenett = Rutenett(rader, kolonner)
        self._rutenett.fyll_med_tilfeldige_celler()
        self._rutenett.koble_celler()

# tegner rutenett, og skriver ut generasjonsnummeret og antall levende celler

    def tegn(self):
        self._rutenett.tegn_rutenett()
        print("Antall levende celler: ", self._rutenett.antall_levende())
        print("Generasjonsnummer: ",self._generasjonsnummer)

#   henter alle celler i rutenett, og teller levende naboer
#   oppdaterer status på hver celle når alle celler  i rutenett kommer på nytt
    def oppdatering(self):
        alle_celler = self._rutenett.hent_alle_celler()
        for celle in alle_celler:
            celle.tell_levende_naboer()
            celle.oppdater_status()

        self._generasjonsnummer += 1
