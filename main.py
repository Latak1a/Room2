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
import datetime
import os

# MAIN DISORDINATO

def statistiche():
    
    #legge ogni file presente in dir /statistiche
    for element in os.listdir("./Statistiche/"):
        vittorie = 0
        pareggi = 0
        sconfitte = 0
        score = 0
        df3 = pd.DataFrame()
        if element != "StatisticheGiocatore.csv":
            
            nickname = element.strip(".csv")  
            df1 = pd.read_csv("./Statistiche/" + element)
           
            for i in range(len(df1)):
            
                vittorie += df1.iloc[i]["Vittorie"]
                pareggi += df1.iloc[i]["Pareggi"]
                sconfitte += df1.iloc[i]["Sconfitte"]
                score += df1.iloc[i]["Score"]
            dictGiocatori = {"Nickname": nickname,"Vittorie": [vittorie], "Pareggi": [pareggi], "Sconfitte": [sconfitte], "Score":  [score]}
            print(dictGiocatori)
            df2 = pd.DataFrame(data = dictGiocatori)    
            df3 = pd.concat([df2, df3])
            
    if not os.path.isfile("./Statistiche/StatisticheGiocatore.csv"):
        df3.to_csv(path_or_buf = "./Statistiche/StatisticheGiocatore.csv", 
                    index = False, 
                    columns = ["Nickname", 'Vittorie', "Pareggi", "Sconfitte", "Score"])
        print(f"{df3 =}")
    else:
        #os.remove("./Statistiche/StatisticheGiocatore.csv")
        
        
        df3.to_csv(path_or_buf = "./Statistiche/StatisticheGiocatore.csv",
            index = False,
            columns = ["Nickname", 'Vittorie', "Pareggi", "Sconfitte", "Score"])
        print(f"{df3 =}")


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
    
    #Ciclo while che gestisce la partita e salva la partita in un DataFrame che poi salva su un file csv
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
                print(f"{risultato =} -- Hai vinto fin ora {vittorie} volte")# PRINT DI DEBUG PER LE VITTORIE
                
            elif scelta == "fine":
                break
                
            else:
                risultato = "Sconfitta"
                sconfitte +=1
                print(f"{risultato =} -- Hai perso fin ora {sconfitte} volte")# PRINT DI DEBUG PER LE SCONFITTE
            
                
        elif scelta == "fine":
            print(f"I risultati finali sono:\n{vittorie =}, {pareggi =}, {sconfitte =}")
            
            # Accedo alla data e all'ora corrente (cioè creo un oggetto datetime)
            dataCorrente = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
            
            #Creo lo score
            score = (vittorie * 3) + (pareggi) + (vittorie-sconfitte)
            
            #Creo un dizionario per la creazione di un DataFrame
            dictRisultati = {"Data": [dataCorrente],"Vittorie": [vittorie], "Pareggi": [pareggi], "Sconfitte": [sconfitte], "Score": [score]}
            
            #Creo il dataframe
            df = pd.DataFrame(data = dictRisultati)
            # print(df)
            
            # Se non esiste la cartella 'Statistiche' la creo
            if not os.path.isdir('Statistiche'):
                os.mkdir('Statistiche')
                
            if not os.path.isfile('Statistiche/'+ nickname + ".csv"):
 
                #Trasformo il DataFrame in un file csv con la data come <nome_file>
                df.to_csv(path_or_buf = "Statistiche/" + nickname + ".csv",
                    index = False,
                    columns = ["Data", 'Vittorie', "Pareggi", "Sconfitte", "Score"])
            else:
                df1 = pd.read_csv('Statistiche/' + nickname + ".csv")
                # print(f"Primo DF1: {df1 =}")
                df1 = pd.concat([df, df1])
                # print(f"Secondo DF1: {df1 =}")
                
                df1.to_csv(path_or_buf = "Statistiche/" + nickname + ".csv",
                    index = False,
                    columns = ["Data", 'Vittorie', "Pareggi", "Sconfitte", "Score"])                   
            statistiche()
            break      
        else:
            print("Scegli una delle opzioni possibili!") 
      

gioco()



#leggo il file Statistiche giocatori, se in una delle righe è presente il nickname allora sostituisco la riga
#se non esiste creo la riga, poi metto in ordine di punto??

    



    


# BONUS: registra i dati della partita su un file di testo, decidendo quale sia il formato migliore

# BONUS 2: prevedi e testa una funzione per poter leggere da un file di testo i dati di una partita e visualizzarli

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