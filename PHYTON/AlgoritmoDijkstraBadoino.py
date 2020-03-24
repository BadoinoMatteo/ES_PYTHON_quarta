def algoritmoDijkstra(matrice, source):
    usati=[]
    dist = [10000000 for _ in range(source, len(matrice))]
    dist[source]=0
    succ=[b for b in range(0, len(matrice))]
    while len(succ)!=0:
        nodoMin=min(dist)
        nodo = succ.pop(dist.index(nodoMin))
        dist.remove(nodoMin)
        usati.append(nodo)
        for Vicini in matrice[nodo]:
            if Vicini >0 and matrice[nodo].index(Vicini) in succ:
                if Vicini + nodoMin < dist[succ.index((matrice[nodo].index(Vicini)))]:
                    dist[succ.index((matrice[nodo].index(Vicini)))]=Vicini+nodoMin
            matrice[nodo][matrice[nodo].index(Vicini)] =0
    return usati

def formaMatrice():
    mat = []
    nodi = int(input("inserisci il numero dei nodi"))
    for a in range(0, nodi):
        colonna = [0 for a in range(0, nodi)]
        for j in range(0, nodi):
            if j!=a:
                colonna[j] = int(input(f"Inserire il peso tra il nodo {a} e il nodo {j}"))
        mat.append(colonna)
    return mat, nodi


def main():
    matriceAdiacenze = []
    usati=[]
    matriceAdiacenze, numNodi = formaMatrice()
    print(matriceAdiacenze)
    source=0
    usati=algoritmoDijkstra(matriceAdiacenze, source)
    print(usati)


if __name__ == '__main__':
    main()
