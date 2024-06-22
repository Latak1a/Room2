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

def gioco():
    pareggio = 0
    vincita = 0
    perdita = 0
    while True:
        
        sceltaIA = random.choice(["sasso", "carta", "forbice"])
        scelta = input("Scegli tra 'sasso', 'carta', 'forbice': ")
        print(f"{scelta =}")
        print(f"{sceltaIA =}")
        if scelta in ["sasso", "carta", "forbice"]:
            if scelta == sceltaIA:
                risultato = "Pareggio"
                pareggio += 1
                print(f"{risultato =} -- Hai pareggiato fin ora {pareggio} volte")
                
            elif scelta == "sasso" and sceltaIA == "forbice" or scelta == "carta" and sceltaIA == "sasso" or scelta == "forbice" and sceltaIA == "carta":
                risultato = "Vincita"
                vincita += 1
                print(f"{risultato =} -- Hai vinto fin ora {vincita} volte")
                
            else:
                risultato = "Perdita"
                perdita +=1
                print(f"{risultato =} -- Hai perso fin ora {perdita} volte")
                
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