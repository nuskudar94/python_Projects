

def hastighet(fart):
      if fart <= 60:
         return "fart:",fart
      else:
          return "fart:over",fart



def sjekkVerdier(tallene,min,max):
    bool=None
    for tall in tallene:
        if tall>min and tall<max:
              bool=True
        else:
              bool=False

    return bool


def hovedprogram():

    obj1=Node("a")
    obj1.settInnHoyre(obj2)
    obj1.settInnVenstre(obj3)
    obj2=Node("b")
    obj3=Node("c")


#barn{"Halfdan":"Harald","Christian":"Hans","Harald":"Eirik"}
#harald halfdanin ilk dogan cocugu.
#personer=arverekke("Harald","Eirik",barn)  > Halfdan Harald Eirik
def arverekke(forfader,etterkommer,forstefodte):
    #forstefodte er en dict,
    arverekken_liste=[]
    arverekken_liste.append(forfader)
    arverekken_liste.append()

class Bud:
    def __init__(self,budgiver,budStr):
        self._budgiver=budgiver
        if budStr<=0 :
            self._budStr=1 


    def hentBudgiver(self):
        return self._budgiver

    def hentBudStr(self):
        return self._budStr



class Annonse:
    def __init__(self,annTekst):
        self._annTekst=annTekst
        self._budListe=[]


    def hentTekst(self):
        return self._annTekst

    def giBud(self,hvem,belop):
        nyttBud=Bud(hvem,belop)
        self._budListe.append(nyttBud)


    def antBud(self):
        return len(self._budListe)

    def hoyesteBud(self):
         
        hoyBud=self._budliste[0] 
        for bud in self._budListe:
            if bud.hentBudStr()>hoyBud.hentBudStr():
                hoyBud=bud 
                if hoyBud.hentBudStr()==bud.hentBudStr():
                    if self._budListe.index(hoyBud)<self._budListe.index(bud):
                        hoyBud=hoyBud
                    else:
                        hoyBud=bud 

        return hoyBud 


    def kraftBud(self,hvem,belop,max):
        etBud=self.giBud(hvem,belop)



class Kategori:
    def __init__(self,katNavn):
        self._katList=[]
        self._katNavn=katNavn 

    def nyAnnonse(self,annTekst):
        nyAnnonse=Annonse(annTekst)
        self._katList.append(nyAnnonse)
        return str(nyAnnonse)


    def hentAnnonser(self):
        return self._katList






class Bruktmarked:
    def __init__(self):
        self._dictBruktmarked={}


    def nyKategori(self,katNavn):
        
         
        if katNavn not in self._dictBruktmarked.keys():
            nyKategori=Kategori(katNavn)
            self._dictBruktmarked[katNavn]=nyKategori
            return nyKategori  
        else:
            return None   


    def finnKategori(self,katNavn):
        if katNavn in self._dictBruktmarked.keys():
            return self._dictBruktmarked[katNavn]
        else:
            return None







                






