import controlloCapienza
# Funzione da modificare: bloccare l'inserimento in lista quando capienza Attuale è uguale a 0 
# ciclo while capienzaAttuale != 0 poi append Clienti in attesa

def clientiServiti(attrazione, tazze, bruco, covo, raptor, space, blue, clientiInSospeso, famiglie, numFamiglie, ristoro):
    
    if attrazione == "tazze":
        #Diminuisco il valore di capienzaAttuale di 1
        tazze.capienzaAttuale = tazze.capienzaMassima - len(tazze.clientiServiti)
        controlloCapienza.controlloCapienzaAttuale(tazze, clientiInSospeso, famiglie, tazze, bruco, covo, raptor, space, blue, numFamiglie, ristoro)
    elif attrazione == "bruco":
        bruco.capienzaAttuale = bruco.capienzaMassima - len(bruco.clientiServiti)
        controlloCapienza.controlloCapienzaAttuale(bruco, clientiInSospeso, famiglie, tazze, bruco, covo, raptor, space, blue, numFamiglie, ristoro)
    elif attrazione == "covo dei pirati": 
        covo.capienzaAttuale = covo.capienzaMassima - len(covo.clientiServiti)
        controlloCapienza.controlloCapienzaAttuale(covo, clientiInSospeso, famiglie, tazze, bruco, covo, raptor, space, blue, numFamiglie, ristoro)
    elif attrazione == "Raptor":
        raptor.capienzaAttuale = raptor.capienzaMassima - len(raptor.clientiServiti)
        controlloCapienza.controlloCapienzaAttuale(raptor, clientiInSospeso, famiglie, tazze, bruco, covo, raptor, space, blue, numFamiglie, ristoro)
    elif attrazione == "Space Vertigo":
        space.capienzaAttuale = space.capienzaMassima - len(space.clientiServiti)
        controlloCapienza.controlloCapienzaAttuale(space, clientiInSospeso, famiglie, tazze, bruco, covo, raptor, space, blue, numFamiglie, ristoro)
    else:
        blue.capienzaAttuale = blue.capienzaMassima - len(blue.clientiServiti)
        controlloCapienza.controlloCapienzaAttuale(blue, clientiInSospeso, famiglie, tazze, bruco, covo, raptor, space, blue, numFamiglie, ristoro)

     