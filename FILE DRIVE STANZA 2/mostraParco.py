from matplotlib import pyplot as plt

def mostraParco(attrazioni, clientiInSospeso, ristoro):
    fig, axs = plt.subplots(figsize=(10, 10))
    
    labels = set()
    for index, attrazione in enumerate(attrazioni):
        axs.scatter(attrazione.posizione[0], attrazione.posizione[1], s=100, edgecolors=f'C{index}', facecolors=f'C{index}')
        if attrazione.nome not in labels:
            labels.add(attrazione.nome)
            axs.scatter([], [], s=100, edgecolors=f'C{index}', facecolors=f'C{index}', label=f'{attrazione.nome}')
        
        for cliente in attrazione.clientiInAttesa:
            axs.scatter(cliente.posizione[0], cliente.posizione[1], s=30, edgecolors='Black', facecolors='Black')
            if cliente.nome not in labels:
                labels.add(cliente.nome)
                axs.scatter([], [], s=30, edgecolors='Black', facecolors='Black', label=f'{cliente.nome}')
    
    axs.scatter(ristoro.posizione[0], ristoro.posizione[1], s=100, edgecolors='C7', facecolors='C7', label='Ristoro')
    
    axs.legend()
    plt.show()
