# En prosedyre som predikerer om kunden skal betale lån eller ikke
def enkel_prediksjon() :
	#Her spør vi kunden om alder,kjønn,status og gjeld 
	alder=int(input("Hvor gammel er du?"))
	kjønn=input("Er du man eller kvinne?")
	sivil_status=input("Er du gift eller singel?")
	gjeld=int(input("Hvor mye gjeld har du?"))

	#Skriver ut totalt sett hva kunden er
	print("Du er en " + sivil_status + " på " ,alder , " år med " , gjeld , " kr i gjeld.")

	#Her predikerer programmet om kunden skal betale lån eller ikke
	# basert på kundeinformasjon 
	if ((kjønn=="man") and (sivil_status=="singel") and (gjeld>100000)):
		print("vil ikke betale")
	elif((kjønn=="man") and (alder<25) and (gjeld>200000)):
		print("vil ikke betale")
	elif((sivil_status=="singel") and (kjønn=="kvinne") and (alder<28) and (gjeld>300000)):
		print("vil ikke betale")
	else :
		print("vil betale")

#Her kaller vi prosedyren
enkel_prediksjon()

