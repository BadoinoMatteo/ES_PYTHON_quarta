import random

def push(stack, element):
    stack.append(element)
    return stack

def pop(stack):
    element=stack.pop()
    return stack,element

class carta(object):

    def __init__(self, seme, numero):
        self.seme=seme 
        self.numero=numero

    def stampa(self):
        print (f"la carta è {self.numero} di  {self.seme} ")


Mazzo=[]
Coppato=[]
Semi=["C", "P", "D", "F"]
for i in range(1,14):
    for s in Semi:
        push(Mazzo, carta(s, i))

for i in Mazzo:
    i.stampa()

numero=random.randint(1,10)
x=0
print(numero)

for i in range(numero,53):
    _,element=pop(Mazzo)
    push(Coppato, element)


for n in Coppato:
    n.stampa()
        
