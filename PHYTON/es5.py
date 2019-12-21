import random

nameLista=['BEST fra' , 'Bado', 'Gianlu', 'Simo']

Lista2=[2,6,4,5]

nameLista=nameLista+Lista2
print(nameLista)
for num, student in enumerate(nameLista):
    print(f"{num} - {student}")

#print(nameLista[2:4])

print(f"Viene interrogato:{nameLista[random.randint(0, len(nameLista)-1)]}")

##