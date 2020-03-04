def main():
    nodi = numNodi()
    grafo = usertomat(nodi)
    dict = mattodict(grafo)
    mat = dicttomat(dict, nodi)


def numNodi():
    nodo = int(input("inserisci il numero di nodi che compongono il grafo non orientato pesato"))
    return nodo


def usertomat(numNodi):
    grafo = []
    for i in range(1, numNodi + 1):
        vicinanze = [int(i) for i in input(f"Inserire le vicinanze del nodo {i} (separate dalla ,) ").split(',')]
        colonna = [0 for dim in range(0, numNodi)]
        for j in vicinanze:
            if j != i:
                colonna[j - 1] = float(input(f"Inserire il peso tra il nodo {i} e il nodo {j}"))
        grafo.append(colonna)
    print(grafo)
    return grafo


def mattodict(grafo):
    dict = {}
    for i in range(0, len(grafo)):
        chiave = i + 1;
        occ = []
        pesi = []
        for c in range(0, len(grafo)):
            if grafo[i][c] > 0:
                occ.append(c + 1)
                pesi.append(grafo[i][c])
            dict[chiave] = {"neighbors": occ,  "weights": pesi}

    print(dict)
    return dict


def dicttomat(dict, nodo):
    mat = []
    for chiave, valore in dict.items():
        colonna = [0 for i in range(0, nodo)]
        peso=valore["weights"]
        vicinanza=valore["neighbors"]
        for c , x in zip(vicinanza, peso):
            colonna[c - 1] = x
        mat.append(colonna)
    print(mat)
    return mat


if __name__ == '__main__':
    main()
