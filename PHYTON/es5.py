import random

nameLista=['BEST fra' , 'Bado', 'Gianlu', 'Simo']

for num, student in enumerate(nameLista):
    print(f"{num} - {student}")

print(f"Viene interrogato:{nameLista[random.randint(0, len(nameLista)-1)]}")