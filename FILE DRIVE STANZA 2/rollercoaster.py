#Importiamo il modulo esterno per randomizzare attrazioni e nomi e cognomi delle famiglie
import random
from matplotlib import pyplot as plt
import randomizza
# import spostamenti
import spostamenti2
from classi import *
import creaFamiglie
import time

p2 = Punto_Cartesiano(20, 20)
p3 = Punto_Cartesiano(20, 30)
p4 = Punto_Cartesiano(20, 40)
p5 = Punto_Cartesiano(30, 20)
p6 = Punto_Cartesiano(30, 30)
p7 = Punto_Cartesiano(30, 40)
p8 = Punto_Cartesiano(50, 50)

#Randomizza le attrazioni desiderate degli umani
#listaAttrazioniBambini, listaAttrazioniRagazzi = randomizza.randomizza_lista()

#Crea il ristoro
ristoro = Ristoro([p8.x, p8.y], "Hot Dog store", 0, 10, [])

#Crea le Attrazioni
bruco = Attrazione([p2.x, p2.y], "Bruco", True, capienzaMassima= 5)
tazze = Attrazione([p3.x, p3.y], "Tazze", True,capienzaMassima= 5)
covo = Attrazione([p4.x, p4.y], "Covo dei pirati", True, capienzaMassima= 5)

raptor = Attrazione([p5.x, p5.y], "Raptor", False, capienzaMassima= 5)
space = Attrazione([p6.x, p6.y], "Space Vertigo", False, capienzaMassima= 5)
blue = Attrazione([p7.x, p7.y], "Blue Tornado", False, capienzaMassima= 5)

attrazioni = [bruco, tazze, covo, raptor, space, blue]

# Dichiaro il numero di famiglie da creare
numFamiglie = 20
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
# spostamenti.spostamenti(clientiInSospeso, tazze, bruco, covo, raptor, space, blue, numFamiglie, clientiInSospeso, ristoro)
spostamenti2.spostamenti(clientiInSospeso, attrazioni, ristoro)
