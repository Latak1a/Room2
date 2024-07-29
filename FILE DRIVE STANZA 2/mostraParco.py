from matplotlib import pyplot as plt

def mostraParco(attrazioni, clientiInSospeso, ristoro):
    fig, ax = plt.subplots(figsize=(10, 10))
    
    labels = set()
    for index, attrazione in enumerate(attrazioni):
        ax.scatter(attrazione.posizione[0], attrazione.posizione[1], s=100, edgecolors=f'C{index}', facecolors=f'C{index}')
        if attrazione.nome not in labels:
            labels.add(attrazione.nome)
            ax.scatter([], [], s=100, edgecolors=f'C{index}', facecolors=f'C{index}', label=f'{attrazione.nome}')
        
        for cliente in attrazione.clientiInAttesa:
            ax.scatter(cliente.posizione[0], cliente.posizione[1], s=30, edgecolors='Black', facecolors='Black')
            if cliente.nome not in labels:
                labels.add(cliente.nome)
                ax.scatter([], [], s=30, edgecolors='Black', facecolors='Black', label=f'{cliente.nome}')
    
    ax.scatter(ristoro.posizione[0], ristoro.posizione[1], s=100, edgecolors='C7', facecolors='C7', label='Ristoro')
    
    for cliente in clientiInSospeso:
        ax.scatter(cliente.posizione[0], cliente.posizione[1], s=30, edgecolors='Black', facecolors='Black')
        if cliente.nome not in labels:
            labels.add(cliente.nome)
            ax.scatter([], [], s=30, edgecolors='Black', facecolors='Black', label=f'{cliente.nome}')
    
    ax.legend()
    plt.show()
