#funksjonen lager ordbok, tar max_temp fil som parameter
def lageBok (fil_navn_month):
    bok_lagt= {}
    min_fil = open(fil_navn_month)
    #Løkken går gjennom linjenne og legger til ordboken
    for linje in min_fil :
        biter = linje.split(",")
        #print(biter)
        month = biter[0]
        #print(month)
        temp = float(biter[1])
        #print(temp)
        bok_lagt[month] = temp

    return bok_lagt

max_temp_bok=lageBok("max_temperatures_per_month.csv")
print(max_temp_bok)

#prosedyren tar to parameter.en fil og en ordbok
def tempVarsel(temp_Ordbok,fil_daglig_temp):
    min_fil = open(fil_daglig_temp)
    #max_temp=0
    #Her lagres det innholdverdien
    months_temp=temp_Ordbok.values()
    #Løkken går gjennom linjene
    for linje in min_fil :

        biter =linje.split(",")
        month=biter[0] #Måneder
        dag=biter[1]    #Dager
        temp=float(biter[2]) #temperaturer
        #Løkken går gjennom max temperaturer og oppdaterer ny max verdi
        for temps in months_temp:
            if temps < temp :
                temp_Ordbok[month]=temp


        # for months in months_temp:
        #     if temp > temp_Ordbok[months]:
        #         print(temp_Ordbok[months])
        #         temp_Ordbok[months]=temp
        #print(temp)






                #print("Ny varmerekord på", dag, month," : ",temp, " grader Celcius (gammel varmerekord var ", value," grader Celcius")

    return temp_Ordbok

max_daily_fil="max_daily_temperature_2018.csv"
print(tempVarsel(max_temp_bok,max_daily_fil))
