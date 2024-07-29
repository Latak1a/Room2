from clientiServiti import *
import countdownListaAttesa
from classi import *




#Funzione che sposti le persone verso la prima attrazione desiderata
def spostamenti(famiglie: list, tazze, bruco, covo, raptor, space, blue, numFamiglie:int, clientiInSospeso:list, ristoro):
    
    
    #print(f"La posizione iniziale del bambino è {famiglie[0]["Bambino"]}")
    
    #Crea il ciclo for per spostare tutti gli umani alla loro prima attrazione desiderata
    # per bambino
    for i in range(0, numFamiglie):
    
        if (len(famiglie[i]["Bambino"]["attrazioniDesiderate"]) > 0 and famiglie[i]["Bambino"]["attrazioniDesiderate"][0] == "tazze" and famiglie[i]["Bambino"]["attrazioniDesiderate"][0] not in tazze.clientiInAttesa):
            famiglie[i]["Bambino"]["Posizione Iniziale"] = tazze.posizione
            famiglie[i]["Adulto"]["Posizione Iniziale"] = tazze.posizione
            
            #Cancello l'attrazione desiderata
            del(famiglie[i]["Bambino"]["attrazioniDesiderate"][0])
            
            if len(tazze.clientiServiti) != tazze.capienzaMassima:
                tazze.clientiServiti.append(famiglie[i]["Bambino"])
                tazze.clientiServiti.append(famiglie[i]["Adulto"])
                #Richiamo la funzione che appende alla lista clienti serviti il nome dell'umano
                clientiServiti("tazze", tazze, bruco, covo, raptor, space, blue, clientiInSospeso, famiglie, numFamiglie, ristoro)
            else:
                tazze.clientiInAttesa.append(famiglie[i]["Bambino"])
                tazze.clientiInAttesa.append(famiglie[i]["Adulto"])
                #Richiamo la funzione che appende alla lista clienti serviti il nome dell'umano
                clientiServiti("tazze", tazze, bruco, covo, raptor, space, blue, clientiInSospeso, famiglie, numFamiglie, ristoro)
                
            # print(f"{tazze.clientiServiti =}\n{tazze.clientiInAttesa}")
            
            
        elif len(famiglie[i]["Bambino"]["attrazioniDesiderate"]) > 0 and famiglie[i]["Bambino"]["attrazioniDesiderate"][0] not in bruco.clientiInAttesa and famiglie[i]["Bambino"]["attrazioniDesiderate"][0] == "bruco":
            famiglie[i]["Bambino"]["Posizione Iniziale"] = bruco.posizione
            famiglie[i]["Adulto"]["Posizione Iniziale"] = bruco.posizione
            
            del(famiglie[i]["Bambino"]["attrazioniDesiderate"][0])
            
            if len(bruco.clientiServiti) != bruco.capienzaMassima:
                bruco.clientiServiti.append(famiglie[i]["Bambino"])
                bruco.clientiServiti.append(famiglie[i]["Adulto"])
                #Richiamo la funzione che appende alla lista clienti serviti il nome dell'umano
                clientiServiti("bruco", tazze, bruco, covo, raptor, space, blue, clientiInSospeso, famiglie, numFamiglie, ristoro)
            else:
                bruco.clientiInAttesa.append(famiglie[i]["Bambino"])
                bruco.clientiInAttesa.append(famiglie[i]["Adulto"])
                #Richiamo la funzione che appende alla lista clienti serviti il nome dell'umano
                clientiServiti("bruco", tazze, bruco, covo, raptor, space, blue, clientiInSospeso, famiglie, numFamiglie, ristoro)
            
            
        elif len(famiglie[i]["Bambino"]["attrazioniDesiderate"]) > 0 and famiglie[i]["Bambino"]["attrazioniDesiderate"][0] not in bruco.clientiInAttesa and famiglie[i]["Bambino"]["attrazioniDesiderate"][0] == "covo dei pirati":
            famiglie[i]["Bambino"]["Posizione Iniziale"] = covo.posizione
            famiglie[i]["Adulto"]["Posizione Iniziale"] = covo.posizione
            del(famiglie[i]["Bambino"]["attrazioniDesiderate"][0])
            
            if len(covo.clientiServiti) != covo.capienzaMassima:
                covo.clientiServiti.append(famiglie[i]["Bambino"])
                covo.clientiServiti.append(famiglie[i]["Adulto"])
                #Richiamo la funzione che appende alla lista clienti serviti il nome dell'umano
                clientiServiti("covo dei pirati", tazze, bruco, covo, raptor, space, blue, clientiInSospeso, famiglie, numFamiglie, ristoro)
            else:
                covo.clientiInAttesa.append(famiglie[i]["Bambino"])
                covo.clientiInAttesa.append(famiglie[i]["Adulto"])
                #Richiamo la funzione che appende alla lista clienti serviti il nome dell'umano
                clientiServiti("covo dei pirati", tazze, bruco, covo, raptor, space, blue, clientiInSospeso, famiglie, numFamiglie, ristoro)
        else:
           famiglie[i]["Bambino"]["Posizione Iniziale"] = ristoro.posizione 
           famiglie[i]["Adulto"]["Posizione Iniziale"] = ristoro.posizione 
           ristoro.clientiRistoro.append(famiglie[i]["Bambino"])   
           ristoro.clientiRistoro.append(famiglie[i]["Adulto"]) 
      
        #per ragazzo
        if len(famiglie[i]["Ragazzo"]["attrazioniDesiderate"]) > 0 and famiglie[i]["Ragazzo"]["attrazioniDesiderate"][0] not in raptor.clientiInAttesa and famiglie[i]["Ragazzo"]["attrazioniDesiderate"][0] == "Raptor":
            famiglie[i]["Ragazzo"]["Posizione Iniziale"] = raptor.posizione
            
            del(famiglie[i]["Ragazzo"]["attrazioniDesiderate"][0])
            
            if len(raptor.clientiServiti) != raptor.capienzaMassima:
                raptor.clientiServiti.append(famiglie[i]["Ragazzo"])
                
                #Richiamo la funzione che appende alla lista clienti serviti il nome dell'umano
                clientiServiti("Raptor", tazze, bruco, covo, raptor, space, blue, clientiInSospeso, famiglie, numFamiglie, ristoro)
            else:
                raptor.clientiInAttesa.append(famiglie[i]["Ragazzo"])
               
                #Richiamo la funzione che appende alla lista clienti serviti il nome dell'umano
                clientiServiti("Raptor", tazze, bruco, covo, raptor, space, blue, clientiInSospeso, famiglie, numFamiglie, ristoro)
            
        elif len(famiglie[i]["Ragazzo"]["attrazioniDesiderate"]) > 0 and famiglie[i]["Ragazzo"]["attrazioniDesiderate"][0] not in space.clientiInAttesa and famiglie[i]["Ragazzo"]["attrazioniDesiderate"][0] == "Space Vertigo":
            famiglie[i]["Ragazzo"]["Posizione Iniziale"] = space.posizione
            
            del(famiglie[i]["Ragazzo"]["attrazioniDesiderate"][0])
            
            if len(space.clientiServiti) != space.capienzaMassima:
                space.clientiServiti.append(famiglie[i]["Ragazzo"])
                
                #Richiamo la funzione che appende alla lista clienti serviti il nome dell'umano
                clientiServiti("Space Vertigo", tazze, bruco, covo, raptor, space, blue, clientiInSospeso, famiglie, numFamiglie, ristoro)
            else:
                space.clientiInAttesa.append(famiglie[i]["Ragazzo"])
                
                #Richiamo la funzione che appende alla lista clienti serviti il nome dell'umano
                clientiServiti("Space Vertigo", tazze, bruco, covo, raptor, space, blue, clientiInSospeso, famiglie, numFamiglie, ristoro)
            
        elif len(famiglie[i]["Ragazzo"]["attrazioniDesiderate"]) > 0 and famiglie[i]["Ragazzo"]["attrazioniDesiderate"][0] not in space.clientiInAttesa and famiglie[i]["Ragazzo"]["attrazioniDesiderate"][0] == "Blue Tornado":
            famiglie[i]["Ragazzo"]["Posizione Iniziale"] = blue.posizione
            del(famiglie[i]["Ragazzo"]["attrazioniDesiderate"][0])
            
            if len(blue.clientiServiti) != blue.capienzaMassima:
                blue.clientiServiti.append(famiglie[i]["Ragazzo"])
                
                #Richiamo la funzione che appende alla lista clienti serviti il nome dell'umano
                clientiServiti("Blue Tornado", tazze, bruco, covo, raptor, space, blue, clientiInSospeso, famiglie, numFamiglie, ristoro)
            else:
                blue.clientiInAttesa.append(famiglie[i]["Ragazzo"])
                
                #Richiamo la funzione che appende alla lista clienti serviti il nome dell'umano
                clientiServiti("Blue Tornado", tazze, bruco, covo, raptor, space, blue, clientiInSospeso, famiglie, numFamiglie, ristoro)
        else:
           famiglie[i]["Ragazzo"]["Posizione Iniziale"] = ristoro.posizione
           ristoro.clientiRistoro.append(famiglie[i]["Ragazzo"])
           
           #print(f"Il Ragazzo {famiglie[i]["Ragazzo"]["Nome"]} {famiglie[i]["Ragazzo"]["Cognome"]}, si trova in posizione {famiglie[i]["RAgazzo"][famiglie[i]["Ragazzo"]["Posizione Iniziale"]]}")
       
        
        
        if famiglie[i]["Componenti"] == 4:
            #per ragazzo2
            if len(famiglie[i]["Ragazzo2"]["attrazioniDesiderate"]) > 0 and famiglie[i]["Ragazzo2"]["attrazioniDesiderate"][0] not in raptor.clientiInAttesa and famiglie[i]["Ragazzo2"]["attrazioniDesiderate"][0] == "Raptor":
                famiglie[i]["Ragazzo2"]["Posizione Iniziale"] = raptor.posizione
                
                del(famiglie[i]["Ragazzo2"]["attrazioniDesiderate"][0])
                
                if len(raptor.clientiServiti) != raptor.capienzaMassima:
                    raptor.clientiServiti.append(famiglie[i]["Ragazzo2"])
                    
                    #Richiamo la funzione che appende alla lista clienti serviti il nome dell'umano
                    clientiServiti("Raptor", tazze, bruco, covo, raptor, space, blue, clientiInSospeso, famiglie, numFamiglie, ristoro)
                else:
                    raptor.clientiInAttesa.append(famiglie[i]["Ragazzo2"])
                
                    #Richiamo la funzione che appende alla lista clienti serviti il nome dell'umano
                    clientiServiti("Raptor", tazze, bruco, covo, raptor, space, blue, clientiInSospeso, famiglie, numFamiglie, ristoro)
                
            elif len(famiglie[i]["Ragazzo2"]["attrazioniDesiderate"]) > 0 and famiglie[i]["Ragazzo2"]["attrazioniDesiderate"][0] not in space.clientiInAttesa and famiglie[i]["Ragazzo2"]["attrazioniDesiderate"][0] == "Space Vertigo":
                famiglie[i]["Ragazzo2"]["Posizione Iniziale"] = space.posizione
                
                del(famiglie[i]["Ragazzo2"]["attrazioniDesiderate"][0])
                
                if len(space.clientiServiti) != space.capienzaMassima:
                    space.clientiServiti.append(famiglie[i]["Ragazzo2"])
                    
                    #Richiamo la funzione che appende alla lista clienti serviti il nome dell'umano
                    clientiServiti("Space Vertigo", tazze, bruco, covo, raptor, space, blue, clientiInSospeso, famiglie, numFamiglie, ristoro)
                else:
                    space.clientiInAttesa.append(famiglie[i]["Ragazzo2"])
                    
                    #Richiamo la funzione che appende alla lista clienti serviti il nome dell'umano
                    clientiServiti("Space Vertigo", tazze, bruco, covo, raptor, space, blue, clientiInSospeso, famiglie, numFamiglie, ristoro)
                
            elif len(famiglie[i]["Ragazzo2"]["attrazioniDesiderate"]) > 0 and famiglie[i]["Ragazzo2"]["attrazioniDesiderate"][0] not in space.clientiInAttesa and famiglie[i]["Ragazzo2"]["attrazioniDesiderate"][0] == "Blue Tornado":
                famiglie[i]["Ragazzo2"]["Posizione Iniziale"] = blue.posizione
                del(famiglie[i]["Ragazzo2"]["attrazioniDesiderate"][0])
                
                if len(blue.clientiServiti) != blue.capienzaMassima:
                    blue.clientiServiti.append(famiglie[i]["Ragazzo2"])
                    
                    #Richiamo la funzione che appende alla lista clienti serviti il nome dell'umano
                    clientiServiti("Blue Tornado", tazze, bruco, covo, raptor, space, blue, clientiInSospeso, famiglie, numFamiglie, ristoro)
                else:
                    blue.clientiInAttesa.append(famiglie[i]["Ragazzo2"])
                    
                    #Richiamo la funzione che appende alla lista clienti serviti il nome dell'umano
                    clientiServiti("Blue Tornado", tazze, bruco, covo, raptor, space, blue, clientiInSospeso, famiglie, numFamiglie, ristoro)
            else:
                famiglie[i]["Ragazzo"]["Posizione Iniziale"] = ristoro.posizione
                ristoro.clientiRistoro.append(famiglie[i]["Ragazzo"])
    
    
def spostamentoFineGiro(attrazione, clientiInSospeso, famiglie, tazze, bruco, covo, raptor, space, blue, numFamiglie, ristoro):
    
    for i in range(len(attrazione.clientiServiti)):
        clientiInSospeso.append(attrazione.clientiServiti.pop())
        attrazione.capienzaAttuale = attrazione.capienzaMassima
        for elemento in attrazione.clientiInAttesa:
            secondi = 5
            countdownListaAttesa(secondi)
            attrazione.clientiServiti.append(elemento)
            controlloCapienza.controlloCapienzaAttuale(attrazione, clientiInSospeso)
    spostamenti(famiglie, tazze, bruco, covo, raptor, space, blue, numFamiglie, clientiInSospeso, ristoro)
        
        
        
        
        
        
        # while len(attrazione.clientiServiti) <= attrazione.capienzaMassima:
        #     if len(attrazione.clientiInAttesa) != 0:
        #         attrazione.clientiServiti.append(attrazione.clientiInAttesa[0])
        #         controlloCapienza.controlloCapienzaAttuale(attrazione, clientiInSospeso)
        #     else:
        #         spostamenti(famiglie, tazze, bruco, covo, raptor, space, blue, numFamiglie, clientiInSospeso)
                
        
        
#entrano persone fino a 4 su clientiServiti
#vengono inseriti nella lista clientiInAttesa
# da lista clientiInAttesa riempe clientiServiti fino a 4
#Se capienzaAttuale == 0 allora parte la giostra
#i clientiServiti vanno nella lista clientiInSospeso
#capienzaAttuale torna ad essere a 4
 
    
    

   
    
