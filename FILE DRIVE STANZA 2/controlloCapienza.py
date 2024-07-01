import countdown

def controlloCapienzaAttuale(attrazione, clientiInSospeso, famiglie, tazze, bruco, covo, raptor, space, blue, numFamiglie, ristoro):
    
    if attrazione.capienzaAttuale > 0:
        print(f"Inizia il giro della giostra {attrazione.nome} in: ")
        countdown.count_down(3, attrazione, clientiInSospeso, famiglie, tazze, bruco, covo, raptor, space, blue, numFamiglie, ristoro)     