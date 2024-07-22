import random
from classi import *

#Creo una lista di congomi
lista_cognomi = ["Rossi", "Bianchi", "Verdi", "Ricci", "Ferrari", "Conti", "Galli", "Marini", "Bruno", "Barbieri", "Lombardi", "Moretti", "Romano", "Colombo", "Marchetti", "Gentile", "Caruso", "Villa", "Pellegrini", "Santoro"]


def creaFamiglie(numFamiglie, clientiInSospeso: list):
    
    for i in range(numFamiglie):
        p1 = Punto_Cartesiano(5, 1 + i)
        posizioneIniziale = [p1.x,p1.y]
        randomRagazzi = random.randint(1,2)
        if randomRagazzi == 1:
            
            lista_nomi = ["Marco", "Giulia", "Luca", "Sofia", "Andrea", "Alessia", "Matteo", "Chiara", "Francesco", "Emma", "Gabriele", "Martina", "Davide", "Alice", "Lorenzo", "Greta", "Simone", "Valentina", "Federico", "Elena"]
            cognome = random.choice(lista_cognomi)
            lista_cognomi.remove(cognome)
            nomeAdulto = random.choice(lista_nomi)
            lista_nomi.remove(nomeAdulto)
            nomeBambino = random.choice(lista_nomi)
            lista_nomi.remove(nomeBambino)
            nomeRagazzo = random.choice(lista_nomi)
            adulto = Adulto(posizioneIniziale, nomeAdulto, cognome)
            posizioneIniziale = [p1.x + 1 , p1.y]
            bambino = Bambino(posizioneIniziale, nomeBambino, cognome)
            posizioneIniziale = [p1.x + 2 , p1.y]
            ragazzo = Ragazzo(posizioneIniziale, nomeRagazzo, cognome)
            
            clientiInSospeso.append(adulto)
            clientiInSospeso.append(bambino)
            clientiInSospeso.append(ragazzo)
        
                    
        else:
            lista_nomi = ["Marco", "Giulia", "Luca", "Sofia", "Andrea", "Alessia", "Matteo", "Chiara", "Francesco", "Emma", "Gabriele", "Martina", "Davide", "Alice", "Lorenzo", "Greta", "Simone", "Valentina", "Federico", "Elena"]
            cognome = random.choice(lista_cognomi)
            lista_cognomi.remove(cognome)
            nomeAdulto = random.choice(lista_nomi)
            lista_nomi.remove(nomeAdulto)
            nomeBambino = random.choice(lista_nomi)
            lista_nomi.remove(nomeBambino)
            nomeRagazzo = random.choice(lista_nomi)
            nomeRagazzo2 = random.choice(lista_nomi)
            adulto = Adulto(posizioneIniziale, nomeAdulto, cognome) 
            posizioneIniziale = [p1.x + 1 , p1.y]
            bambino = Bambino(posizioneIniziale, nomeBambino, cognome)
            posizioneIniziale = [p1.x + 2 , p1.y]
            ragazzo = Ragazzo(posizioneIniziale, nomeRagazzo, cognome)
            posizioneIniziale = [p1.x + 3 , p1.y]
            ragazzo2 = Ragazzo(posizioneIniziale,nomeRagazzo2,cognome)
            
            clientiInSospeso.append(adulto)
            clientiInSospeso.append(bambino)
            clientiInSospeso.append(ragazzo)
            clientiInSospeso.append(ragazzo2)
    for index, element in enumerate(clientiInSospeso):
        print(f"{clientiInSospeso[index]}")  
    #print(clientiInSospeso[0:])      
    return clientiInSospeso  

    
  