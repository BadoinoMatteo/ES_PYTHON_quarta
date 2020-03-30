def dict():
    dict={}
    data = open('data.txt', 'r')
    lines = (data.readlines())
    for line in lines:
        riga=line.split(' ')
        chiave=int(riga.pop(0))
        contagiati=[int(n) for n in riga]
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


def Elimina(lista):
    for i in lista:
        if lista.count(i) > 1:
            lista.remove(i)
            Elimina(lista)
    return lista


def trovaPazienteZero(dict):
    listaPazientiZero = []
    for p in range(0, len(dict)):
        listaPazientiZero.append(trova(p, dict))
    return Elimina(listaPazientiZero)



def trova(find, dict):
    tro = False
    for key, val in dict.items():
        if find in val:
            tro = True
            return trova(key, dict)
    if tro == False: return find




def main():
    d=dict()
    mat=dicttomat(d)
    print(trovaPazienteZero(d))


if __name__=='__main__':
    main()
