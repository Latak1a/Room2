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

import random as rd
import datetime, os

# 1. Chiedo all'utente di scegliere tra sasso, carta e forbici
opzioni = ['sasso', 'carta', 'forbici']

statistiche = {
    'vittorie': 0,
    'pareggi': 0,
    'sconfitte': 0
}

def acquisisciNickname() -> str:
    while True:
        nickname: str = input("Inserisci il tuo nickname [il nickname non può contenere caratteri non alfanumerici]: ")
        if nickname.isalnum():
            return nickname
        else:
            print("Il nickname immesso contiene caratteri non alfanumerici!")

def acquisisciScelta() -> str:
    while True:
        scelta = input("Scegli tra sasso, carta e forbici: ")
        if scelta in opzioni:
            return scelta
        print(f"Hai digitato '{scelta}' mentre le opzioni ammissibili sono solo {opzioni}")

def estraiOpzione(opzioni: list[str] = ['sasso', 'carta', 'forbici']) -> str:
    return rd.choice(opzioni)

def giocaSassoCartaForbici(opzioni: list = ['sasso', 'carta', 'forbici']) -> dict[str,int]:
    
    statistiche = {
    'vittorie': 0,
    'pareggi': 0,
    'sconfitte': 0
    }
    
    # Chiedo all'utente di immettere un nickname ammissibile
    nickname = acquisisciNickname()
    
    prosegui = '' # flag che indica quando l'utente vuole uscire dal gioco

    while prosegui != 'N':
        scelta = acquisisciScelta()

        # 2. Estrai a sorte uno tra 'sasso', 'carta' e 'forbici'
        estrazione = estraiOpzione() 
        print(f"Ho estratto: {estrazione}")

        condizioniVittoria = [
            scelta == 'sasso' and estrazione == 'forbici',
            scelta == 'carta' and estrazione == 'sasso',
            scelta == 'forbici' and estrazione == 'carta',
        ]

        # 3. Scopri chi ha vinto
        if estrazione == scelta:
                print("Pareggio!")
                statistiche['pareggi'] += 1
        elif any(condizioniVittoria):
            print("Hai vinto!")
            statistiche['vittorie'] += 1
        else:
            print("Hai perso!")
            statistiche['sconfitte'] += 1

        messaggio = f'Ecco le tue statistiche {nickname}'
        print(f"{messaggio:=^40}")
        print(f"Vittorie : {statistiche['vittorie']}\nPareggi : {statistiche['pareggi']}\nSconfitte : {statistiche['sconfitte']}")
        prosegui = input("Vuoi giocare un'altra manche? [N-No, altrimenti prosegui]: ")

    return statistiche, nickname # restituisce una tupla di due elementi (statistiche e nickname)

# BONUS: registra i dati della partita su un file di testo, decidendo quale sia il formato migliore
def scriviStatistiche(nomeFile, statistiche, nickname):
    # Se non esiste la cartella 'Statistiche' la creo
    if not os.path.isdir('Statistiche'):
        os.mkdir('Statistiche')

    messaggioDaScrivereSuFile = f"{nickname}\n{statistiche['vittorie']},{statistiche['pareggi']},{statistiche['sconfitte']}"
    with open(f"Statistiche/{nomeFile}", mode = 'w') as file:
        file.write(messaggioDaScrivereSuFile)

# BONUS 2: prevedi e testa una funzione per poter leggere da un file di testo i dati di una partita e visualizzarli
def leggiStatistiche(nomeFile):
    with open(f"Statistiche/{nomeFile}", mode = 'r') as file:
        nickname = file.readline()[:-1]
        contenuto = file.read().split(',')
        contenuto = list(map(int, contenuto))
        # Anologo a 
        #contenuto = [int(elemento) for elemento in contenuto]
        
    statisticheLette = {}
    statisticheLette['vittorie'] , statisticheLette['pareggi'] , statisticheLette['sconfitte'] = contenuto
    messaggio = f'Ecco le tue statistiche {nickname}'
    print(f"{messaggio:=^40}")
    print(f"Vittorie : {statistiche['vittorie']}\nPareggi : {statistiche['pareggi']}\nSconfitte : {statistiche['sconfitte']}")

def aggiornaStatisticheComplete(statistiche, nickname):
    # Se non esiste la cartella 'Statistiche' la creo
    if not os.path.isdir('Statistiche'):
        os.mkdir('Statistiche')

    nomeFile = f"Statistiche/statisticheComplete.txt"

    if os.path.isfile(nomeFile):    
        with open(nomeFile, mode = 'r+') as file:
            #file.write(messaggioDaScrivereSuFile)
            # Leggo tutte le righe del file e le salvo dentro alla lista 'righe'
            righe = file.readlines()

            # Tolgo il '\n' da ciascuna riga
            righe = [riga.strip('\n') for riga in righe]

            # Separo ciascuna riga nei dati che la compongono
            righe = [riga.split(',') for riga in righe] # [[nickname1,vittorie1,pareggi1,sconfitte1], ..., [nicknameN,vittorieN,pareggiN,sconfitteN]]
            nuovoGiocatore = True
            file.seek(0)
        
            for indiceRiga, giocatore in enumerate(righe):
                if giocatore[0] == nickname:
                    giocatore[1] = statistiche['vittorie'] + int(giocatore[1])
                    giocatore[2] = statistiche['pareggi'] + int(giocatore[2])
                    giocatore[3] = statistiche['sconfitte'] + int(giocatore[3])
                    nuovoGiocatore = False
                
                if indiceRiga == 0:
                    messaggio = f"{giocatore[0]},{giocatore[1]},{giocatore[2]},{giocatore[3]}"
                else:
                    messaggio = f"\n{giocatore[0]},{giocatore[1]},{giocatore[2]},{giocatore[3]}"
                
                file.write(messaggio)

            primoPosto = righe[0]
            secondoPosto = righe[0]
            terzoPosto = righe[0]

            for giocatore in righe:
                if giocatore[1] > primoPosto[1]:
                    primoPosto = giocatore
                elif giocatore[1] == primoPosto[1]:
                    if giocatore[3] < primoPosto[3]:
                        primoPosto = giocatore
                    elif giocatore[3] == primoPosto[3]:
                        if giocatore[2] < primoPosto[2]:
                            primoPosto = giocatore
                            
                    

            if nuovoGiocatore:
                messaggio = f"\n{nickname},{statistiche['vittorie']},{statistiche['pareggi']},{statistiche['sconfitte']}" 
                file.write(messaggio)  
    else:
        with open(nomeFile, mode = 'w') as file:
            file.write(f"{nickname},{statistiche['vittorie']},{statistiche['pareggi']},{statistiche['sconfitte']}")

# --- MAIN CODE ---
# Gioco una manche dopo l'altra fino a quando l'utente non vuole smettere
statistiche, nickname = giocaSassoCartaForbici(opzioni = opzioni)


# Salvo le statistiche dell'utente
dataCorrente = datetime.datetime.now()
nomeFile = f"{dataCorrente.year}_{dataCorrente.month}_{dataCorrente.day}_{dataCorrente.hour}_{dataCorrente.minute}.txt"
scriviStatistiche(nomeFile = nomeFile, statistiche = statistiche, nickname = nickname)
aggiornaStatisticheComplete(statistiche, nickname)

# Leggo le statistiche dell'utente appena salvate
leggiStatistiche(nomeFile = nomeFile)


# BONUS 3: i dati di ciascuna partita devono essere salvati in un file txt che riporta la data 
# e l'ora della fine della partita (ad esempio se la partita finisce il 14/06/2024 alle 20:02, dovrà chiamarsi
#                                   "2024_06_14_20_02.txt")

# BONUS 4: prevedi una funzione per poter accedere a tutti i dati delle partite salvate e fare una statistica dei giocatori.
#          Prevedi quindi di chiedere il nickname del giocatore prima di avviare la partita. Il nickname dovrà comparire 
#          tra i dati del .txt 

# BONUS 5: Scrivi un codice che crei 20 liste con list comprehension fatte in questo modo:
# [numeroVittorie, numeroPareggi, numeroSconfitte]
# con ciascun valore estratto a sorte tra 0 e 10
# Sviluppa poi un algoritmo per ordinare queste 20 liste trovando il primo, secondo e terzo posto