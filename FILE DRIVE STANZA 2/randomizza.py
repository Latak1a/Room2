import random

def randomizza_lista():
    stringheBambini = random.sample(["tazze", "bruco", "covo dei pirati"], len(["tazze", "bruco", "covo dei pirati"]))
    stringheRagazzi = random.sample(["Raptor", "Blue Tornado", "Space Vertigo"], len(["Raptor", "Blue Tornado", "Space Vertigo"]))
    return stringheBambini, stringheRagazzi