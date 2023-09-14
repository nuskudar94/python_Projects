class Dato :
    #KOnstruktøren initialiserer dag,måned år
    def __init__(self,ny_dag,ny_maaned,nytt_ar):
        self._dag=15
        self._maaned=ny_maaned
        self._ar=nytt_ar

    # def hent_dag(self):
    #     return self._dag
    #returnerer år
    def hent_aar(self):
        return self._ar
    #Lager og returnerer en dato
    def lagDato(self):

        #datos=self._dag + '.' + self._maaned +"."+ self._ar
        return str(self._dag)+"."+str(self._maaned)+"."+str(self._ar)

        #Metoden sjekker om dagen er bestemt dag
    def sjekkDag(self,dag):
        if dag == self._dag :
            return True
        else:
            return False
