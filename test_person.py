from person import Person

#Tar input fra bruker
navn_input = input("Skriv et navn")
alder_input = input("Skriv alder")

person1 = Person(navn_input,alder_input) #oppretter et objekt

kravBruker= input("Vil du legge til hobbyer ?")

#Spør brukeren om å legge til hobby
while kravBruker=="Ja":
        hobitil=input("Skriv et hobby")
        person1.leggTilHobby(hobitil)
        kravBruker=input("Vil du legge til hobby?")
        if kravBruker=="Nei":
            person1.skrivUt()
