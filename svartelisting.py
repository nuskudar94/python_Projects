def bestem_laan ():
	#Henter ut kunde_ID
	kunde_ID=int(input("Hva er kunde-ID-en din?"))

	#Lagrer svarte_liste mengden
	svarte_liste={23894, 29741, 10961, 22768, 22803, 11993, 24409, 9312, 29405, 6638, 738, 29964, 11967, 13443, 11534, 26228, 6867, 23027, 29137, 14084, 452, 15594, 22765, 25487}

	#Sjekker om kunde ID finnes i svarte liste
	if (kunde_ID in svarte_liste) :
		print("Kan ikke få lån")
	else :
		print("kan få lån")

#Kaller prosedyren
bestem_laan()

"""
Hvorfor passer det fint å bruke en mengde for å 
representere svartelistede kunder? 
Kunne man evt brukt en liste eller en ordbok?

-Fordi mengder inneholder bare unike verdier og 
kunde_ID må være unik for hver kunde.

"""