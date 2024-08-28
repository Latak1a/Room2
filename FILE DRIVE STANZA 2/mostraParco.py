from matplotlib import pyplot as plt

def mostraParco(attrazioni, clientiInSospeso, ristoro):
    fig, axs = plt.subplots(figsize=(10, 10))
    
    
    
    
    axs.scatter(ristoro.posizione[0], ristoro.posizione[1], s=100, edgecolors='C7', facecolors='C7', label='Ristoro')
    for index, attrazione in enumerate(attrazioni):
        axs.scatter(attrazione.posizione[0], attrazione.posizione[1], s=150, edgecolors=f'C{index}', facecolors=f'C{index}', label= f"{attrazione.nome}")
        
        
    for cliente in clientiInSospeso[:]:
        axs.scatter(cliente.posizione[0], cliente.posizione[1], s=30, edgecolors= "Black", facecolors="Black")
        
            
    for attrazione in attrazioni[:]:
        for cliente in attrazione.clientiServiti[:]:
            axs.scatter(cliente.posizione[0], attrazione.posizione[1], s=30, edgecolors= "Black", facecolors= "Green")
        for cliente in attrazione.clientiInAttesa[:]:   
            axs.scatter(cliente.posizione[0], attrazione.posizione[1], s=30, edgecolors= "Black", facecolors= "Yellow")
    
    for cliente in ristoro.clientiRistoro[:]:
        axs.scatter(cliente.posizione[0], attrazione.posizione[1], s=30, edgecolors= "Black", facecolors= "Green")
        
        
    axs.legend()
    plt.show()
