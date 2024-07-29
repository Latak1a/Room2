import random
#Definisco la classe PuntoCartesiano
class Punto_Cartesiano:
    # Definisco il costruttore della classe Punto_Cartesiano
    # N.B: il costruttore di una classe deve sempre chiamarsi __init__ 
   
    def __init__(self, x, y):
        """
        costruisce un oggetto di tipo Punto_Cartesiano inizializzando gli attributi x e y a 0.0
        """
        self.x: float = x
        self.y: float = y
        
        def __str__(self):
            return f"({self.x:.2f};{self.y:.2f})"
        
        # Puoi definire un attributo di istanza di una classe con la sintassi:
        # self.<nome_attributo> = <valore_attributo>
        
#Definisco la classe Umano
class Umano:
    def __init__(self, 
                 posizione: Punto_Cartesiano, 
                 nome: str, 
                 cognome: str, 
                 tipo: str, 
                 attrazioniDesiderate:list[str]):
        
        #posizione(PuntoCartesiano)    
        self.posizione = posizione
        #nome(str)
        self.nome: str = nome
        #cognome(str)
        self.cognome: str = cognome
        #tipo(str) es. bambino, ragazzo o adulto
        self.tipo: str = tipo
        #lista attrazioniDesiderate(list[str])
        self.attrazioniDesiderate = attrazioniDesiderate
            #if tipo == "bambino" ->attrazioniDesiderate Class Bambino
            #if tipo == "ragazzo" -attrazioniDesiderate Class Ragazzo
    def __str__(self):
        return f"Umano: nome: {self.nome} -- cognome: {self.cognome} -- tipo: {self.tipo} -- attrazioniDesiderate: {self.attrazioniDesiderate} -- posizione: {self.posizione}"
   
#Definisco la classe Bambino(Umano)         
class Bambino(Umano):
    def __init__(self, posizione, nome, cognome):
        super().__init__(posizione, 
                         nome, 
                         cognome, 
                         tipo = "Bambino", 
                         attrazioniDesiderate = random.sample(["tazze", "bruco", "covo dei pirati"], len(["tazze", "bruco", "covo dei pirati"])))
    
        
#Definisco la classe Ragazzo(Umano)
    #elabora lista attrazioniDesiderate["Raptor", "Blue Tornado", "Space Vertigo"]
class Ragazzo(Umano):
    def __init__(self, posizione, nome, cognome):
        super().__init__(posizione, 
                         nome, 
                         cognome, 
                         tipo = "Ragazzo", 
                         attrazioniDesiderate = random.sample(["Raptor", "Blue Tornado", "Space Vertigo"], len(["Raptor", "Blue Tornado", "Space Vertigo"])))
        
    
#Definisco la classe Adulto(Umano)
class Adulto(Umano):
    def __init__(self, 
                 posizione, 
                 nome, 
                 cognome):
        super().__init__(posizione, 
                         nome, 
                         cognome, "Adulto", [])
        
#Definisco la classe Location
class Location:
    #Attributi:
    def __init__(self, posizione, nome):
        #nome(str)
        #definisco la posizione come PuntoCartesiano
        self.posizione = posizione
        self.nome = nome
    
        return f"Location: {self.nome} -- Posizione: {self.posizione}"
        
#Definisco la classe Ristoro(Location)
class Ristoro(Location):
    def __init__(self, posizione: Punto_Cartesiano, nome: str, capienzaAttuale: int, capienzaMassima: int, clientiRistoro: list[Umano]):
        super().__init__(posizione, nome)
        self.capienzaAttuale = capienzaAttuale
        self.capienzaMassima = capienzaMassima
        self.clientiRistoro = clientiRistoro
        
    def __str__(self):
        return f'Risoro : "{self.nome}" ---> Clienti Presenti: {len(self.clientiRistoro)}'    
        
#Definisco la classe Attrazione(Location)
class Attrazione(Location):
    def __init__(self, posizione: Punto_Cartesiano, nome: str, perBambini: bool, capienzaAttuale: int, capienzaMassima: int, tempoAttesa:int = 0):
        super().__init__(posizione, nome)
        self.perBambini = perBambini
        self.capienzaAttuale = capienzaMassima
        self.capienzaMassima = capienzaMassima
        self.tempoAttesa = tempoAttesa
        self.clientiServiti: list[Umano] = [] 
        self.clientiInAttesa:list[Umano] = []
        
    def __str__(self):
        return f'Attrazione "{self.nome}" ---> Clienti Serviti: {len(self.clientiServiti)} | Clienti in Attesa: {len(self.clientiInAttesa)}'
