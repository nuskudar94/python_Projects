class Sang :
    def __init__(self,artist,tittel):
        self._artist=artist
        self._tittel=tittel


    def spill(self):
        print("Spiller",self._tittel,";",self._artist)

    def sjekk_artist(self,navn):
        artisten=self._artist.lower().strip().split()
        navnet=navn.lower().strip().split()

        #for element in artisten:


        return [element for element in artisten if element in navnet]

    def sjekk_tittel(self,tittel):
        if self._tittel.lower() == tittel.lower():
            return True
        else:
            return False


    def sjekk_artist_og_tittel(self,artist,tittel):
        if self.sjekk_artist(artist) and self.sjekk_tittel(tittel) == True:
            return True
        else :
            return False

    def __str__(self):
        return f'Sang(Tittel={self._tittel}, Artist={self._artist})'
