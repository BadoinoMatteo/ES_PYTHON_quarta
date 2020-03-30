def main():
    nodi=numNodi()
    grafo=usertomat(nodi);
    dict=mattodict(grafo)
    mat=dicttomat(dict,nodi)

def numNodi():
    nodo = int(input("inserisci il numero di nodi che compongono il grafo non orientato"))
    return nodo

def usertomat(numNodi):
    mat = []
    for i in range(1, numNodi + 1):
        vicinanze = [int(i) for i in input(f"Inserire le vicinanze del nodo {i} (separate dalla ,) ").split(',')]
        colonna = [0 for dim in range(0, numNodi)]
        for cont in vicinanze:
            if cont != i:
                colonna[cont - 1] = 1
        mat.append(colonna)
    print(mat)
    return mat



def mattodict(grafo):
    dict={}
    for i in range(0, len(grafo)):
        chiave= i +1;
        occ= []
        for c in range(0,len(grafo)):
            if grafo[i][c]==1:
                occ.append(c+1)
            dict[chiave]=occ;
    print(dict)
    return dict

def dicttomat(dict, nodo):
    mat=[]
    for chiave, valore in dict.items():
        colonna=[0 for i in range(0,nodo)]
        for c in valore:
            colonna[c-1]=1
        mat.append(colonna)
    print(mat)
    return mat


if __name__=='__main__':
    main()