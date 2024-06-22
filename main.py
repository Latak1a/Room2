# Utilizzando il modulo random, realizza il gioco del sasso, carta, forbici:
# - sasso vince su forbici
# - carta vince su sasso
# - forbici vince su carta
# - ogni simbolo pareggia contro ogni simbolo uguale

# Implementate l'algoritmo:
# - definendo una funzione per giocare
# - permettendo all'utente di scegliere tra sasso, carta e forbici
# - registrando il numero di vittorie, pareggi e sconfitte
# - continuando a far giocare l'utente fino a quando non decide di smettere

#Importo il modulo random
import random
import pandas as pd

def nicknameCheck():
    while True:
        nickname = input("Inserisci il tuo nickname (solo alfanumerico): ")
        if nickname.isalnum():
            return nickname
        else:
            print("Riprova! Caratteri non validi!")

def gioco():
    pareggi = 0
    vittorie = 0
    sconfitte = 0
    opzioni = ["sasso", "carta", "forbice"]
    
    nickname = nicknameCheck()
    
        
    while True:
        
        sceltaIA = random.choice(opzioni)
        scelta = input("Scegli tra 'sasso', 'carta', 'forbice' o fine per terminare: ")
        print(f"{scelta =}") #print di debug
        print(f"{sceltaIA =}") #print di debug
        if scelta in opzioni:
            if scelta == sceltaIA:
                risultato = "Pareggio"
                pareggi += 1
                print(f"{risultato =} -- Hai pareggiato fin ora {pareggi} volte") # PRINT DI DEBUG PER IL PAREGGIO
                
                
            elif scelta == "sasso" and sceltaIA == "forbice" or scelta == "carta" and sceltaIA == "sasso" or scelta == "forbice" and sceltaIA == "carta":
                risultato = "Vittoria"
                vittorie += 1
                print(f"{risultato =} -- Hai vinto fin ora {vittorie} volte")
                
            elif scelta == "fine":
                break
                
            else:
                risultato = "Sconfitta"
                sconfitte +=1
                print(f"{risultato =} -- Hai perso fin ora {sconfitte} volte")
                
        elif scelta == "fine":
            print(f"I risultati finali sono:\n{vittorie =}, {pareggi =}, {sconfitte =}")
            
            dictRisultati = {"Nickname": [nickname],"Vittorie": [vittorie], "Pareggi": [pareggi], "Sconfitte": [sconfitte]}
            #Creo il dataframe
            df = pd.DataFrame(data = dictRisultati)
            print(df)
            
            break
                
        else:
            print("Scegli una delle opzioni possibili!")    
         
           
                
            
gioco()
# BONUS: registra i dati della partita su un file di testo, decidendo quale sia il formato migliore

# BONUS 2: prevedi e testa una funzione per poter leggere da un file di testo i dati di una partita e visualizzarli

# BONUS 3: i dati di ciascuna partita devono essere salvati in un file txt che riporta la data 
# e l'ora della fine della partita (ad esempio se la partita finisce il 14/06/2024 alle 20:02, dovrà chiamarsi
#                                   "2024_06_14_20_02.txt")

# BONUS 4: prevedi una funzione per poter accedere a tutti i dati delle partite salvate e fare una statistica dei giocatori.
#          Prevedi quindi di chiedere il nickname del giocatore prima di avviare la partita. Il nickname dovrà comparire 
#          tra i dati del .txt 