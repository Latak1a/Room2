from clientiServiti import *
import countdownListaAttesa
from classi import *
import countdown
import mostraParco



#Funzione che sposti le persone verso la prima attrazione desiderata
def spostamenti(clientiInSospeso, attrazioni, ristoro):
    #mostraParco.mostraParco(attrazioni, clientiInSospeso, ristoro)
    max_ripetizioni = 10
    
    for ripetizione in range(max_ripetizioni):
        
        for attrazione in attrazioni:
            if attrazione.tempoAttesa == 0:
                for cliente in attrazioni.clientiServiti[:]:
                    attrazione.clientiServiti.remove(cliente)
                    clientiInSospeso.append(cliente)
                    
                attrazione.capienzaAttuale = attrazione.capienzaMassima
                
                while attrazione.capienzaAttuale > 0 and len(attrazione.clientiInAttesa) > 0:
                    cliente = attrazione.clientiInAttesa.pop(0) # p.s: la funzione pop restituisce ciò che toglie da una lista ;)
                    attrazione.clientiServiti.append(cliente)
                    attrazione.capienzaAttuale -= 1
                
                if attrazione.capienzaAttuale == 0:
                    attrazione.tempoAttesa = 5
                else:
                    attrazione.tempoAttesa -= 1
            
            
            for cliente in clientiInSospeso[:]:
                if len(cliente.attrazioniDesiderate) > 0:
                    clientiInSospeso.remove(cliente)
                    
                    for attrazione in attrazioni:
                        if attrazione.nome == cliente.attrazioniDesiderate[0]:
                    
                            if attrazione.capienzaAttuale > 0:
                                attrazione.clientiServiti.append(cliente)
                                attrazione.capienzaAttuale -= 1
                            else:
                                attrazione.clientiInAttesa.append(cliente)
                        
                    cliente.attrazioniDesiderate.pop(0)
            print(f"Iterazione n. {ripetizione} ---\n")
            print(f"Clienti in Sospeso: \n{clientiInSospeso} ------------\n")
            
        for attrazione in attrazioni:
            print(attrazione)
            scelta = input(f"Premi invio per passare alla ripetizione n. {ripetizione + 1}: ")
    
            
            
        # if len(clientiInSospeso) != 0:
            
        #     for attrazione in attrazioni:
                #Se il tempo di attesa o la capienzaAttuale dell'attrazione sono pari a 0 la giostra finisce il suo giro
                #Quindi svuoto i clienti serviti e li riporto ai clienti in sospeso
                # if attrazione.tempoAttesa == 0:
                #     print(f"{attrazione.tempoAttesa =} ")
                #     print(f"Fine giro: {attrazione.nome}")
                #     if attrazione.capienzaAttuale == 0:
                #         for index, clienti in enumerate(attrazione.clientiServiti):
                                        
                #             clientiInSospeso.append(attrazione.clientiServiti[index].pop())
                #             print(clientiInSospeso)
                #             print(attrazione.clientiServiti)
                                            
                    
                #         attrazione.capienzaAttuale = attrazione.capienzaMassima
                #         attrazione.tempoAttesa = 5
                    
                #         while attrazione.capienzaAttuale > 0 and len(attrazione.clientiInAttesa) > 0:
                            
                #             cliente = attrazione.clientiInAttesa.pop(0) # p.s: la funzione pop restituisce ciò che toglie da una lista ;)
                #             attrazione.clientiServiti.append(cliente)
                #             attrazione.capienzaAttuale -= 1
                #             attrazione.tempoAttesa -= 1
                #     else:
                #         attrazione.tempoAttesa -= 1
                            
                #     print(f"Inizio giro: {attrazione.nome}")
                        
                
                            
                            
                        
                        # if attrazione.nome == cliente.attrazioniDesiderate[0]:
                        #     if len(cliente.attrazioniDesiderate) > 0 or cliente.tipo != "Adulto":
                        #         persona = clientiInSospeso.pop(0)
                            
                        #         attrazione.clientiInAttesa.append(persona)
                        #         cliente.attrazioniDesiderate.pop(0)
                        #         attrazione.tempoAttesa -= 1
                        #     else:
                        #         print("ciao")
                    
        #         print(f"\n{attrazione}")
                
        # print(input("Premi invio per continuare")) 
                                    
                       
                                
                               
                                    
                    #                     attrazione.clientiServiti.append(cliente)
                    #                     attrazione.capienzaAttuale -= 1
                    #                     clientiInSospeso.remove(cliente)
                                        
                    #                     #Sposta la posizione del cliente
                    #                     cliente.posizione[0] = attrazione.posizione[0] + 5
                    #                     cliente.posizione[1] = attrazione.posizione[1] + 5
                    #                     #print(cliente)
                    #                     attrazione.tempoAttesa -= 1
                    #                     print(f"1   {attrazione.tempoAttesa =} {attrazione.nome}")
                                        
                    #             else:
                    #                 #GIOSTRA PIENA
                    #                 attrazione.clientiInAttesa.append(cliente)
                    #                 clientiInSospeso.remove(cliente)
                                    
                    #                 #SpOSTARE LA POSIZIONE DEL CLIENTE
                    #                 cliente.posizione[0] = attrazione.posizione[0] + 5
                    #                 cliente.posizione[1] = attrazione.posizione[1] + 5
                    #                 cliente.attrazioniDesiderate.pop(0)
                    #                 #print(cliente)
                                    
                    #                 print(f"2   {attrazione.tempoAttesa =} {attrazione.nome}")
                                    
                    #                 if attrazione.tempoAttesa == 0 :
                                        
                    #                     print(f"Inizio giro: {attrazione.nome}")
                    #                     print(f"Fine giro: {attrazione.nome}")
                                        
                                        
                                        
                                        
                    #                     attrazione.tempoAttesa = 5    
                    #                 elif attrazione.tempoAttesa != 0 and len(attrazione.clientiInAttesa) == 0:
                    #                     attrazione.tempoAttesa -= 1
                                    
                    # else:
                    #     clientiInSospeso.remove(cliente)
                    #     ristoro.clientiRistoro.append(cliente)
                        
                    #     #SOSTARE LA POSIZIONE DEL CLIENTE
                    #     cliente.posizione[0] = ristoro.posizione[0] + 5
                    #     cliente.posizione[1] = ristoro.posizione[1] + 5
                    #     #print(cliente)
                       
                        
                # 
                    
        
                 
                       
    #mostraParco.mostraParco(attrazioni, clientiInSospeso, ristoro)
    
        
    
     
     
     
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
 
    
    

   
    
