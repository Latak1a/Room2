# BONUS 5: Scrivi un codice che crei 20 liste con list comprehension fatte in questo modo:
# [numeroVittorie, numeroPareggi, numeroSconfitte]
# con ciascun valore estratto a sorte tra 0 e 10
# Sviluppa poi un algoritmo per ordinare queste 20 liste trovando il primo, secondo e terzo posto


import random
max = 0
min = 0
risultati = [[random.randint(0,10), random.randint(0,10), random.randint(0,10)] for k in range(20)]
#for i in range(3):
    
print(risultati)

