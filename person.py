class Person :
    #Konstruktør initialiserer navn,alder,og hobby liste
    def __init__(self,navn,alder):
        self._navn=navn
        self._alder=alder
        self._hobbyer=[]
    #Metoden legger hobbyer til tom liste
    def leggTilHobby(self,leggHobby):
        self._hobbyer.append(leggHobby)
    #Skriver ut hobbyer
    def skrivHobbyer(self):
        for hobby in self._hobbyer:
            print(hobby)
    #Skriver ut all info om bruker
    def skrivUt(self):
        print(self._navn)
        print(self._alder)
        self.skrivHobbyer()
