import matplotlib as plt

def mostraParco(ristoro, bruco, tazze, covo, raptor, space, blue):
    plt.xlim(0, 50)
    plt.ylim(0, 50)

    plt.plot(ristoro.posizione[0], ristoro.posizione[1], color = "Green", marker ="o")
    plt.text(ristoro.posizione[0] - 5, (ristoro.posizione[1] - 3),ristoro.nome)
    
    plt.plot(bruco.posizione[0], bruco.posizione[1], color ="red", marker = "o")
    plt.text(bruco.posizione[0] - 2, (bruco.posizione[1] - 3),bruco.nome)
    plt.plot(tazze.posizione[0], tazze.posizione[1], color ="red", marker = "o")
    plt.text(tazze.posizione[0] - 2, (tazze.posizione[1] - 3),tazze.nome)
    plt.plot(covo.posizione[0], covo.posizione[1], color ="red", marker = "o")
    plt.text(covo.posizione[0] - 2, (covo.posizione[1] - 3),covo.nome)

    plt.plot(raptor.posizione[0], raptor.posizione[1], color ="red", marker = "o")
    plt.text(raptor.posizione[0] - 2, (raptor.posizione[1] - 3),raptor.nome)
    plt.plot(space.posizione[0], space.posizione[1], color ="red", marker = "o")
    plt.text(space.posizione[0] - 5, (space.posizione[1] - 3),space.nome)
    plt.plot(blue.posizione[0], blue.posizione[1], color ="red", marker = "o")
    plt.text(blue.posizione[0] - 5, (blue.posizione[1] - 3),blue.nome)
    plt.show()