def sjekk_reise(reise):
    lengden=len(reise)
    gyldig=True
    for travel in reise:
        dest=travel[0]
        ny_dest=travel[1]


def samlet_vaksinasjon(krav_hvert_land):
    samlet_liste=[]
    for liste in krav_hvert_land:
        for vaksiner in liste:
            if vaksiner is not samlet_liste:
                samlet_liste.append(vaksiner)

    return samlet_liste

def forkort(setning, fjern):
    setning_v2 = ""
    for ord in setning.split():
        if not ord=="en":
            setning_v2 = setning_v2 + ord + ""

    return setning_v2


def sjekk_om_fyord(setning,fyord,synonym_liste):
    setning_liste=setning.split()

    for string in setning_liste:
        for lister in synonym_liste:
            if fyord in lister and string in lister:
                return True

            else:
                return False
