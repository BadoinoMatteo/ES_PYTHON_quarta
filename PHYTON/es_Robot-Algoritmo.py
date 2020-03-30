def main():
    usati=[]
    piastrelle = dimPavimento()
    mat = formazionePavimento(piastrelle)
    matAlgoritmo=preparaMatriceAlgoritmo(mat)
    source= int (input("inserisci nodo partenza"))
    dest=int (input("inserisci nodo arrivo"))
    usati=algoritmoDijkstra(matAlgoritmo, source, dest)
    print(usati)

def algoritmoDijkstra(matrice, source, dest):
    usati=[]
    dist = [1 for _ in range(source, dest)]
    dist[0] = 0
    succ=[b for b in range(source, dest)]
    while len(succ)!=0:
        nodoMin = min(dist)
        nodo = succ.pop(dist.index(nodoMin))
        dist.remove(nodoMin)
        usati.append(nodo)
        for vicini in matrice[nodo]:
            if vicini >0 and matrice[nodo].index(vicini) in succ:
                if vicini + nodoMin < dist[succ.index((matrice[nodo].index(vicini)))]:
                    dist[succ.index((matrice[nodo].index(vicini)))]=vicini+nodoMin
            matrice[nodo][matrice[nodo].index(vicini)] =0
    return usati

def dimPavimento():
    nodo = int(input("inserisci la dimensione del pavimento"))
    return nodo


def formazionePavimento(piastrelle):
    mat = []
    for a in range(0, piastrelle):
        riga=[]
        for b in range(0, piastrelle):
            num = int(input(f"inserisci se la cella {a} {b} è libera o occupata :\n 0 --> cella libera \n 1 --> cella occupata \n "))
            if num == 0:
                riga.append(True)
            else:
                riga.append(False)
        mat.append(riga)
    creaNodi(mat)
    print(mat)
    return mat

def creaNodi(pav):
    nNodi = 1
    for r in range(0, len(pav)):
        for c in range(0, len(pav)):
            if pav[r][c]:
                pav[r][c] = nNodi
                nNodi += 1

def costruiscoMatrice (piastrelle , matBool):
    dict = {}
    numNodi = 1
    offset=1
    for a in range(0, piastrelle):
        for b in range(0, piastrelle):
            collegamenti = []
            if matBool[a][b] != False :
                if a-offset >= 0:
                    if matBool[a-offset][b] != False:
                        collegamenti.append(matBool[a-1][b])
                if b-offset >= 0:
                    if matBool[a][b-offset]!=False:
                        collegamenti.append(matBool[a][b-1])
                if a+offset < len(matBool) :
                    if matBool[a+offset][b] != False:
                        collegamenti.append(matBool[a+1][b])
                if b+offset < len(matBool) :
                    if matBool[a][b+offset]!=False:
                        collegamenti.append(matBool[a][b+1])
            dict[numNodi] = collegamenti
            numNodi += 1
    print(dict)
    return dict

def preparaMatriceAlgoritmo(mat):
    for a in range(0,len(mat)):
        for b in range(0 , len(mat)):
            if mat[a][b] == False:
                mat[a][b]=0
    print(mat)
    return mat

if __name__ == '__main__':
    main()