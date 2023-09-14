def prediksjon_med_historikk ():
	
	#Her spør vi kunden om alder,kjønn,status og gjeld, utdanning
	alder=int(input("Hvor gammel er du?"))
	kjønn=input("Er du man eller kvinne?")
	sivil_status=input("Er du gift eller singel?")
	gjeld=int(input("Hvor mye gjeld har du?"))
	utdanning=input("Hva nivå utdanning har du? Svar med ukjent, grunnskole, hoeyskole eller universitet")

	#Skaper en tom ordbok
	intekt ={}

	#Sjekker utdanningsnivå og legger til intekt ordbok
	if (utdanning == "ukjent") :
		intekt["ukjent"]=300000
	elif utdanning == "grunnskole":
		intekt["grunnskole"]=260000
	elif utdanning=="hoeyskole":
		intekt["hoeyskole"]=500000
	elif utdanning=="universitet":
		intekt["universitet"]=700000

	#Skaper en tom liste
	betalingHistorikken= [] 

	#Her spør Kunden om betalinghistorikken og legger til listen
	historikken_forrigeMnd=betalingHistorikken.append(input(" Har du betalt gjelden din i forrige måned ? Svar med betalt eller ikke_betalt"))


	historikken_månedenFør=betalingHistorikken.append(input("Har du betalt gjelden din i måneden før ? Svar med betalt eller ikke_betalt"))

	historikken_toMånedersiden=betalingHistorikken.append(input("Har du betalt gjelden din for måneder siden ? Svar med betalt eller ikke_betalt"))

	#Skriver ut  betaling historikk
	print(betalingHistorikken)

	#Sjekker kravene og predikerer kundens situasjon
	if ((kjønn=="man") and (sivil_status=="singel") and (gjeld>100000)):
		print("vil ikke betale")
	elif((kjønn=="man") and (alder<25) and (gjeld>200000)):
		print("vil ikke betale")
	elif((sivil_status=="singel") and (kjønn=="kvinne") and (alder<28) and (gjeld>300000)):
		print("vil ikke betale")
	elif(betalingHistorikken.count("ikke_betale")>1):
		print("vil ikke betale")
	elif kjønn=="man" and gjeld*3>intekt[utdanning]:
		print("vil betale")
	else :
		print("vil betale")

#Kaller prosedyren
prediksjon_med_historikk()