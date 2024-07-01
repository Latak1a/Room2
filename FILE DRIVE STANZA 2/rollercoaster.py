#Importiamo il modulo esterno per randomizzare attrazioni e nomi e cognomi delle famiglie
import random
from matplotlib import pyplot as plt
import randomizza
import spostamenti
from classi import *
import creaFamiglie
import time

maxRipetizioni = 10

p2 = Punto_Cartesiano(10, 10)
p3 = Punto_Cartesiano(10, 20)
p4 = Punto_Cartesiano(10, 30)
p5 = Punto_Cartesiano(20, 10)
p6 = Punto_Cartesiano(20, 20)
p7 = Punto_Cartesiano(20, 30)
p8 = Punto_Cartesiano(35, 35)


#Randomizza le attrazioni desiderate degli umani
listaAttrazioniBambini, listaAttrazioniRagazzi = randomizza.randomizza_lista()

#Crea il ristoro
ristoro = Ristoro([p8.x, p8.y], "Hot Dog store", 0, 10, [])

#Crea le Attrazioni
bruco = Attrazione([p2.x, p2.y], "Bruco", True, 4, 4, 0)
tazze = Attrazione([p3.x, p3.y], "Tazze", True, 4, 4, 5)
covo = Attrazione([p4.x, p4.y], "Covo", True, 4, 4, 5)

raptor = Attrazione([p5.x, p5.y], "Raptor", False, 4, 4, 5)
space = Attrazione([p6.x, p6.y], "Space Vertigo", False, 4, 4, 5)
blue = Attrazione([p7.x, p7.y], "Blue Tornado", False, 4, 4, 5)

# Dichiaro il numero di famiglie da creare
numFamiglie = 4
clientiInSospeso = []
#Definisco la funzione per creare 4 famiglie con nomi e cognomi randomici, inoltre aggiungiamo la possibilità di randomizzare
#il fatto se le famiglie sono composte da 3 o 4 persone (un ragazzo in più)    
clientiInSospeso: list [Umano] = creaFamiglie.creaFamiglie(numFamiglie, clientiInSospeso)

    
secondi = 3

print("Benvenuti al rollercoaster!")

#Apertura parco giochi
time.sleep(secondi)
print("Start")


#Richiamo la funzione di spostamento
spostamenti.spostamenti(clientiInSospeso, tazze, bruco, covo, raptor, space, blue, numFamiglie, clientiInSospeso, ristoro)

print(f"{len(tazze.clientiServiti) = }") 
print(f"{len(bruco.clientiServiti) = }") 
print(f"{len(covo.clientiServiti) = }") 
print(f"{len(raptor.clientiServiti) = }") 
print(f"{len(blue.clientiServiti) = }") 
print(f"{len(space.clientiServiti) = }") 
print(clientiInSospeso)

# for keyword in famiglie:
#     famiglia = keyword["Famiglia"]
#     componenti = keyword["Componenti"]
#     print(componenti)


#Stampo la capienzaAttuale di tutte le attrazioni
# print(f"{tazze.capienzaAttuale = }, {tazze.clientiServiti = }, {tazze.clientiInAttesa = }")   
# print(f"{bruco.capienzaAttuale = }, {bruco.clientiServiti = }, {bruco.clientiInAttesa = }")
# print(f"{covo.capienzaAttuale = }, {covo.clientiServiti = }, {covo.clientiInAttesa = }")
# print(f"{raptor.capienzaAttuale = }, {raptor.clientiServiti = }, {raptor.clientiInAttesa = }")
# print(f"{space.capienzaAttuale = }, {space.clientiServiti = }, {space.clientiInAttesa = }")
# print(f"{blue.capienzaAttuale = }, {blue.clientiServiti = }, {blue.clientiInAttesa = }")