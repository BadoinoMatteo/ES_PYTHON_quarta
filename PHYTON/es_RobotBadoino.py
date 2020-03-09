def main():
    piastrelle = dimPavimento()
    mat = formazionePavimento(piastrelle)
    dict = costruiscoMatrice(piastrelle, mat)

def dimPavimento():
    nodo = int(input("inserisci la dimensione del pavimento"))
    return nodo


def formazionePavimento(piastrelle):
    mat = []
    for a in range(0, piastrelle):
        for b in range(0, piastrelle):
            num = int(input(f"inserisci se la cella {a} {b} è libera o occupata :\n 0 --> cella libera \n 1 --> cella occupata \n "))
            if num == 0:
                mat.append(True)
            else:
                mat.append(False)


    return mat

def costruiscoMatrice (piastrelle , matBool):
    dict = {}
    numNodi = 1
    for a in range(0, piastrelle):
        for b in range(0, piastrelle):
            collegamenti = []
            if matBool[a][b] != False :
                if a-1 >= 0:
                    if matBool[a-1][b] != False: collegamenti.append(matBool[a-1][b])
                if b-1 >= 0:
                    if matBool[a][b-1]!=False:collegamenti.append(matBool[a][b-1])
                if a+1 >= 0:
                    if matBool[a+1][b] != False: collegamenti.append(matBool[a+1][b])
                if b+1 >= 0:
                    if matBool[a][b+1]!=False:collegamenti.append(matBool[a][b+1])
            dict[numNodi] = collegamenti
            numNodi += 1
    print(dict)
    return dict

if __name__ == '__main__':
    main()
