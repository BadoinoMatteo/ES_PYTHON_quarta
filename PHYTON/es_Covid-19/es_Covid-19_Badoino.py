def dict():
    dict={}
    data = open('data.txt', 'r')
    lines = (data.readlines())
    for line in lines:
        riga=line.split(" ")
        chiave=riga.pop(0)
        contagiati=[]
        for i in riga:
            contagiati=riga
        dict[chiave]=contagiati
    data.close()
    print(dict)
    return dict

def dicttomat(dict):
    mat=[]
    for _, n in dict.items():
        mat.append(n)
    print(mat)
    return mat

def pazienteZero(mat):
    pazientiZero=[]
    for e in len(mat):
        for i in len(mat):
            if mat[e][i+1]>0 :
                pazientiZero.append(mat[e][i])
    print(pazientiZero)




def main():
    d=dict()
    mat=dicttomat(d)
    pazienteZero(mat)


if __name__=='__main__':
    main()
