num=0
ancora=True
lista= []
while ancora==True:
    num=input("inserisci un numero")
    lista.append(num)
    S=input("vuoi inserire ancora qualcosa")  
    if S=='n' :
        ancora=False
print(lista)