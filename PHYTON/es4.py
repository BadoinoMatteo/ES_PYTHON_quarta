# date due liste creare una terza lista che contenga gli elementi comuni delle due

lista1={1,2,4,7,9}
lista2={3,6,1,9,2,1}
lista3=[]

for i in lista1:
        if i in lista2:
            lista3.append(i)
print (lista3)
