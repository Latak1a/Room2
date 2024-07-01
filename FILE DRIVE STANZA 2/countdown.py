import time
import spostamenti



def count_down(starting_number: int, attrazione, clientiInSospeso, famiglie, tazze, bruco, covo, raptor, space, blue, numFamiglie, ristoro) -> None :
    """
    Implements a simple countdown from <starting_number> to 0
    """
    for second in range(starting_number, 0 , -1):
        time.sleep(1)
        print(f"-{second}")
        
        
    time.sleep(1)
    print(attrazione)
    attrazione.clientiInAttesa.extend([])
    attrazione.clientiServiti.extend([])

    print(attrazione)

    print(ristoro)  
