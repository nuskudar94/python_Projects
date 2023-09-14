from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def les_fil (self,filnavn):
        sang_liste=open(filnavn)

        for  linje in sang_liste:
            biter = linje.strip().split(";")

            self._sanger.append(Sang(biter[1],biter[0]))


    def legg_til_sang(self,ny_sang):
        self._sanger.append(ny_sang)

    def fjern_sang(self,sang):
        for sang1 in self._sanger:
            if sang is sang1:
                self._sanger.remove(sang)


    def spill_sang(self,sang):
        # sang her objekt fra Sang
        #liste=Spilleliste(sang)
        sang.spill()


    def spill_alle(self):
        for sang in self._sanger:
            print(sang)

    def finn_sang(self,tittel):
         sang=None
         for sang in self._sanger:

             if tittel in str(sang):
                 sang = sang
             else:
                 sang=None

         return sang









    def hent_artist_utvalg(self,artistnavn):
        artist_liste=[]
        artist_ls=artistnavn.split()
        for sang in self._sanger:
            if artistnavn in str(sang):
                artist_liste.append(sang)

        return artist_liste



    def __str__(self):
        return f'Spilleliste(Navn={self._navn},Sanger={self._sanger})'
