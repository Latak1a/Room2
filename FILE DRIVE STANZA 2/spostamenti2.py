from clientiServiti import *
import countdownListaAttesa
from classi import *
import countdown
import mostraParco
import math
import random

def xy_attesa(attrazione):
    
    d = 3
    angolo = random.choice(list(range(0,180, 3)))

    x = int(attrazione.posizione[0] + d * (math.cos(angolo)))
    y = int(attrazione.posizione[1] + d * (math.sin(angolo)))
     
    return x, y

def xy_serviti(attrazione):
    
    d = 3
    angolo = random.choice(list(range(180, 360, 3)))
    
    x = int(attrazione.posizione[0] + d * (math.cos(angolo)))
    y = int(attrazione.posizione[1] + d * (math.sin(angolo)))
    
    return x, y
    

#Funzione che sposti le persone verso la prima attrazione desiderata
def spostamenti(clientiInSospeso, attrazioni, ristoro):
    
    
    max_ripetizioni = 20
    
    for ripetizione in range(max_ripetizioni):
        mostraParco.mostraParco(attrazioni, clientiInSospeso, ristoro)
        for attrazione in attrazioni[:]:
            if attrazione.tempoAttesa == 0:
                for cliente in attrazione.clientiServiti[:]:
                    attrazione.clientiServiti.remove(cliente)
                    clientiInSospeso.append(cliente)
                    cliente.posizione[0] = 1
                    cliente.posizione[1] = 1
                    print(cliente.posizione)
                    
                attrazione.capienzaAttuale = attrazione.capienzaMassima
                
        print(f"\n --- Iterazione N.:{ripetizione} PRE CLIENTI IN SOSPESO ---\n")
        #print(f"\n---- ClientiInSospeso: \n{clientiInSospeso}------------\n")
        
        for attrazione in attrazioni[:]:
            print(attrazione)
        
        for cliente in clientiInSospeso[:]:
            if len(cliente.attrazioniDesiderate) > 0:
                clientiInSospeso.remove(cliente)
                
                for attrazione in attrazioni:
                    if attrazione.nome == cliente.attrazioniDesiderate[0]:
                
                        if attrazione.capienzaAttuale > 0:
                            attrazione.clientiServiti.append(cliente)
                            attrazione.capienzaAttuale -= 1
                            cliente.posizione[0], cliente.posizione[1] = xy_serviti(attrazione)
                            print(cliente.posizione)
                            
                        else:
                            attrazione.clientiInAttesa.append(cliente)
                            cliente.posizione[0], cliente.posizione[1] = xy_attesa(attrazione)
                            print(cliente.posizione)
                    
                cliente.attrazioniDesiderate.pop(0)
            else:
                clientiInSospeso.remove(cliente)
                cliente.posizione[0] = ristoro.posizione[0]
                cliente.posizione[1] = ristoro.posizione[1]
                ristoro.clientiRistoro.append(cliente)
                
                    
        for attrazione in attrazioni[:]:
            if attrazione.tempoAttesa == 0:
                
                while attrazione.capienzaAttuale > 0 and len(attrazione.clientiInAttesa) > 0:
                    cliente = attrazione.clientiInAttesa.pop(0) # p.s: la funzione pop restituisce ciò che toglie da una lista ;)
                    attrazione.clientiServiti.append(cliente)
                    attrazione.capienzaAttuale -= 1
                    cliente.posizione[0], cliente.posizione[1] = xy_serviti(attrazione)
                    print(cliente.posizione)
                
                if attrazione.capienzaAttuale == 0:
                    attrazione.tempoAttesa = 5
            else:
                attrazione.tempoAttesa -= 1
            
  
            print(f"Iterazione n. {ripetizione} ---\n")
            #print(f"Clienti in Sospeso: \n{len(clientiInSospeso[:])} ------------\n")
            
        
        for attrazione in attrazioni:
            print(attrazione)
            
        #scelta = input(f"Premi invio per passare alla ripetizione n. {ripetizione + 1}: ")
    