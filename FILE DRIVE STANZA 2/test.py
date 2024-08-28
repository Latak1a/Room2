import random
import math

def xy_attesa():
    d = 3
    angolo = random.choice(list(range(0,180, 3)))

    x = 20 + d * math.cos(angolo)
    y = 10 + d * math.sin(angolo)
    
    return math.floor(x), math.floor(y)

print(xy_attesa())























#questo ciclo for serve per stampare a video
# for keyword in famiglie:
#     componenti = keyword["Componenti"]
#     print(componenti)

#     if componenti == 3:
#         famiglia: str = keyword["Famiglia"]
#         adulto: list = keyword["Adulto"]
#         bambino: list = keyword["Bambino"]
#         ragazzo: list = keyword["Ragazzo"]
#         nomeAdulto: str = adulto["Nome"]
#         nomeBambino: str = bambino["Nome"]
#         nomeRagazzo: str = ragazzo["Nome"]
#         cognomeAdulto:str = adulto["Cognome"]
#         cognomeBambino:str = bambino["Cognome"]
#         cognomeRagazzo:str = ragazzo["Cognome"]
#         posizioneAdulto: list = adulto["Posizione Iniziale"]
#         posizioneBambino: list = bambino["Posizione Iniziale"]
#         posizioneRagazzo: list = ragazzo["Posizione Iniziale"]
#         attrazioni_desiderate_Adulto: list = adulto["attrazioniDesiderate"]
#         attrazioni_desiderate_Bambino: list = bambino["attrazioniDesiderate"]
#         attrazioni_desiderate_Ragazzo: list = ragazzo["attrazioniDesiderate"]
        
#         print(f"Famiglia: {famiglia}")
#         print(f"{nomeAdulto} {cognomeAdulto}, Attrazione desiderata: {attrazioni_desiderate_Adulto}, Posizione: {posizioneAdulto}")    
#         print(f"{nomeBambino} {cognomeBambino}, Attrazione desiderata: {attrazioni_desiderate_Bambino}, Posizione: {posizioneBambino}")     
#         print(f"{nomeRagazzo} {cognomeRagazzo}, Attrazione desiderata: {attrazioni_desiderate_Ragazzo}, Posizione: {posizioneRagazzo}")
#     else:
#         famiglia: str = keyword["Famiglia"]
#         adulto: list = keyword["Adulto"]
#         bambino: list = keyword["Bambino"]
#         ragazzo: list = keyword["Ragazzo"]
#         nomeAdulto: str = adulto["Nome"]
#         nomeBambino: str = bambino["Nome"]
#         nomeRagazzo: str = ragazzo["Nome"]
#         cognomeAdulto:str = adulto["Cognome"]
#         cognomeBambino:str = bambino["Cognome"]
#         cognomeRagazzo:str = ragazzo["Cognome"]
#         posizioneAdulto: list = adulto["Posizione Iniziale"]
#         posizioneBambino: list = bambino["Posizione Iniziale"]
#         posizioneRagazzo: list = ragazzo["Posizione Iniziale"]
        
#         attrazioni_desiderate_Adulto: list = adulto["attrazioniDesiderate"]
#         attrazioni_desiderate_Bambino: list = bambino["attrazioniDesiderate"]
#         attrazioni_desiderate_Ragazzo: list = ragazzo["attrazioniDesiderate"]
#         ragazzo2: list = keyword["Ragazzo2"]
#         nomeRagazzo2: str = ragazzo2["Nome"]
#         cognomeRagazzo2:str = ragazzo2["Cognome"]
#         posizioneRagazzo2: list = ragazzo2["Posizione Iniziale"]
#         attrazioni_desiderate_Ragazzo2: list = ragazzo2["attrazioniDesiderate"]
        
#         print(f"Famiglia: {famiglia}")
#         print(f"{nomeAdulto} {cognomeAdulto}, Attrazione desiderata: {attrazioni_desiderate_Adulto}, Posizione: {posizioneAdulto}")    
#         print(f"{nomeBambino} {cognomeBambino}, Attrazione desiderata: {attrazioni_desiderate_Bambino}, Posizione: {posizioneBambino}")     
#         print(f"{nomeRagazzo} {cognomeRagazzo}, Attrazione desiderata: {attrazioni_desiderate_Ragazzo}, Posizione: {posizioneRagazzo}")
#         print(f"{nomeRagazzo2} {cognomeRagazzo2}, Attrazione desiderata: {attrazioni_desiderate_Ragazzo2}, Posizione: {posizioneRagazzo2}\n")