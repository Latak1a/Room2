# BONUS 5: Scrivi un codice che crei 20 liste con list comprehension fatte in questo modo:
# [numeroVittorie, numeroPareggi, numeroSconfitte]
# con ciascun valore estratto a sorte tra 0 e 10
# Sviluppa poi un algoritmo per ordinare queste 20 liste trovando il primo, secondo e terzo posto

#Importo il modulo random
import random

def vincitori(df3 ):
    #nickname = ["a", "b", "c", "d", "e","f","g","h","i","l","m","n","o","p","q","r","s","t","u","v","z"]
    

    #variabile che crea con la list comprehension
    #risultati = [[random.choice(nickname),  random.randint(0,10), random.randint(0,10), random.randint(0,10), 0] for k in range(20)]
    risultati = []

    for i in range(len(df3)):
                nickname = df3.iloc[i]["Nickname"]
                vittorie = df3.iloc[i]["Vittorie"]
                pareggi = df3.iloc[i]["Pareggi"]
                sconfitte = df3.iloc[i]["Sconfitte"]
                score = df3.iloc[i]["Score"]
                risultati.append([nickname, vittorie, pareggi, sconfitte, score])

    #for elemento in risultati:
    #    elemento[4] = elemento[1]*3 + elemento[2] + (elemento[1]-elemento[3]) 
    
    
    podio = [[0, 0],[0, 0],[0, 0]]
    for index, elemento in enumerate(risultati):
        
        if elemento[4] > podio[0][1]:
            if elemento[4] > podio[1][1]:
                if elemento[4] > podio[2][1]:
                    podio[2][0] = index
                    podio[2][1] = elemento[4]   
                else:
                    podio[1][0] = index
                    podio[1][1] = elemento[4]  
            else:   
                podio[0][0] = index
                podio[0][1] = elemento[4] 
    
    print(f"Statistiche partite: {risultati}")
            
    print(f"Il Podio:\nOro: {risultati[podio[2][0]][0]} con {podio[2][1]} punti! \nArgento: {risultati[podio[1][0]][0]} con {podio[1][1]} punti!\nBronzo: {risultati[podio[0][0]][0]} con {podio[0][1]} punti!\n")
            


