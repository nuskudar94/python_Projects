def beregn_score(valg_spiller1,valg_spiller2):
	#beregner score med if setninger og skorer legges til score list
    score=[""]*2
    if valg_spiller1=="samarbeid" and valg_spiller2=="samarbeid":
            score[0]=5
            score[1]=5
    elif valg_spiller1=="samarbeid" and valg_spiller2=="svik":
            score[0]=0
            score[1]=5
    elif valg_spiller1=="svik" and valg_spiller2=="svik":
            score[0]=1
            score[1]=1
    else:
            score[0]=5
            score[1]=0
    return score


    
sc=beregn_score("samarbeid","svik")
print(sc)

def spill_slemt(all_valgene):
	#Programmet avgjør neste valg basert på hvor mange spill det har vært
	
	if len(all_valgene)<=5:
		return "samarbeid"
	elif len(all_valgene)>5:
		return "svik"
		
all_valgene= spill_slemt(["samarbeid","samarbeid","samarbeid","samarbeid","samarbeid","svik","svik","svik","svik","svik"])
print(all_valgene)	
	
def spill_snilt(all_valg):
	#Programmet teller antall svik og samarbeid, og avgjør neste valg basert på antall svik og samarbeid
	counter_sam=0
	counter_svik=0
	for valg in all_valg:
		if valg=="samarbeid":
			counter_sam+=1
		elif valg=="svik":
			counter_svik+=1

	if counter_svik > counter_sam :
		return "svik"
	else:
		return "samarbeid"

all_valg= spill_snilt(["svik","samarbeid","svik","samarbeid","svik","samarbeid","svik","samarbeid","svik","samarbeid"])
print(all_valg)

def utfor_spill():
	#Programmet  gjør 10 spill med forrige prosedyrer og avgjør hvem som har høyest poeng
    slemme_Valg=[""]*10
    snille_Valg=[""]*10
    counterSlemme=0
    counterSnille=0
    
    valgSlemt=["samarbeid","svik"]
    valgSnill=["svik","samarbeid"]
    
    for i in range(0,10):

        slemme_Valg[i] = spill_slemt(valgSlemt)
        snille_Valg[i] = spill_snilt(valgSnill)
        


    for j in range(10):
        
        if snille_Valg[j] == "samarbeid" and slemme_Valg[j] == "samarbeid":
            
            counterSlemme+=3
            counterSnille+=3

        elif snille_Valg[j] == "svik" and slemme_Valg[j] == "svik":
            counterSnille+=1
            counterSlemme+=1

        elif snille_Valg[j] == "samarbeid" and slemme_Valg[j] == "svik":
            counterSlemme+=5

        else :
            counterSnille+=5
    

    
    if counterSlemme >= counterSnille:
        print("Slemme")
    else:
        print("Snille")
       
utfor_spill()

def utfor_spill_uendelig():
    #Programmet spør brukeren om et nytt spill og bestemmer om hvem som har høyest poeng
    ny_spill=input("Vil du spille på nytt ? Ja eller Nei")
    
    valgSlemt=["samarbeid","svik"]
    valgSnill=["svik","samarbeid"]
    counterSlemme=0
    counterSnille=0
    
    if ny_spill=="Ja":
        if spill_snilt(valgSnill) == "samarbeid" and spill_slemt(valgSlemt) == "samarbeid":
            
        	counterSlemme+=3
        	counterSnille+=3

        elif spill_snilt(valgSnill) == "svik" and spill_slemt(valgSlemt) == "svik":
            counterSnille+=1
            counterSlemme+=1

        elif spill_snilt(valgSnill) == "samarbeid" and spill_slemt(valgSlemt) == "svik":
            counterSlemme+=5

        else :
            counterSnille+=5
    else:
        return
    
    
    if counterSlemme >= counterSnille:
        print("Slemme")
    else:
        print("Snille")


utfor_spill_uendelig()
		