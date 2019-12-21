def push(stack, element):
    stack.append(element)
    return stack

def pop(stack):
    element=stack.pop()
    return stack,element

pila=[1,2,"ciao", 4, "tre"]
pila=push(pila, 9)
print(pila)
pila, _=pop(pila)
print(pila)