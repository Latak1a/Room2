from clientiServiti import *
import countdownListaAttesa
from classi import *
import countdown




#Funzione che sposti le persone verso la prima attrazione desiderata
def spostamenti(clientiInSospeso, attrazioni, ristoro):
    max_ripetizioni = 3
    
    for ripetizioni in range(max_ripetizioni):
        
        if len(clientiInSospeso) != 0:
            for attrazione in attrazioni:
                # print(f"\n{attrazione}")
                # print(f"{attrazione.nome =}")
                for cliente in clientiInSospeso:
                    # print(cliente)
                    if len(cliente.attrazioniDesiderate) > 0 and cliente.tipo != "Adulto":
                                                
                            # print(f"{len(cliente.attrazioniDesiderate) =}")
                            # print(f"{cliente.attrazioniDesiderate[0] =}")
                            
                            if attrazione.nome == cliente.attrazioniDesiderate[0]:
                                # print(attrazione.capienzaAttuale)
                                # print(attrazione.capienzaMassima)
                                
                                
                                if attrazione.capienzaAttuale != 0:
                                    
                                        attrazione.clientiServiti.append(cliente)
                                        attrazione.capienzaAttuale -= 1
                                        clientiInSospeso.remove(cliente)
                                        
                                    
                                else:
                                    attrazione.clientiInAttesa.append(cliente)
                                    clientiInSospeso.remove(cliente)
                                    
                                cliente.attrazioniDesiderate.pop(0)
                                    
                                print("giostra partita")
                                clientiInSospeso.append(clientiServiti[0:])
                                attrazione.clientiServiti = []
                                
                    else:
                        clientiInSospeso.remove(cliente)
                        ristoro.clientiRistoro.append(cliente)
                
                #        
       
                    
    print(input("Premi invio per continuare"))                    

    
        
    
     
     
     
    #  for ripetizione in range(max_ripetizioni):
    # for nomeAttrazione, attrazione in dizionarioAttrazioni.items():
        
    #     # Sposto tutti i clienti dalla lista clientiInSospeso alle appropriate attrazioni
    #     for cliente in clientiInSospeso[:]:
    #         # Solo se il cliente ha ancora attrazioni desiderate...
    #         if len(cliente.attrazioniDesiderate) > 0:
    #             # Rimuovo dalla lista clientiInSospeso
    #             clientiInSospeso.remove(cliente)
    #             # E se l'attrazione ha ancora posti liberi...
    #             if dizionarioAttrazioni[cliente.attrazioniDesiderate[0]].capienzaAttuale > 0:
    #                 # ... allora lo aggiungo ai clientiServiti
    #                 dizionarioAttrazioni[cliente.attrazioniDesiderate[0]].clientiServiti.append(cliente)
    #             else: # ...altrimenti...
    #                 # ... lo aggiungo ai clientiInAttesa
    #                 dizionarioAttrazioni[cliente.attrazioniDesiderate[0]].clientiInAttesa.append(cliente)

    #             # Rimuovo la prima attrazione desiderata
    #             cliente.attrazioniDesiderate.pop(0)
   
#entrano persone fino a 4 su clientiServiti
#vengono inseriti nella lista clientiInAttesa
# da lista clientiInAttesa riempe clientiServiti fino a 4
#Se capienzaAttuale == 0 allora parte la giostra
#i clientiServiti vanno nella lista clientiInSospeso
#capienzaAttuale torna ad essere a 4
 
    
    

   
    
