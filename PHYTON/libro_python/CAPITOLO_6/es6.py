"""
1. Go through this program and write a comment above each line explaining it.
2. Find all the places where a string is put inside a string. There are four places.
3. Are you sure there are only four places? How do you know? Maybe I like lying.
4. Explain why adding the two strings w and e with + makes a longer string.

2. line : 17,26,44,53
3. no anche alle linee 33 e 34 vengono concatenate 2 stringhe
4. w dienta una stringa più lunga perchè viene concatenata con e attraverso l'operatore +

stringhe non modificabili es: S= "c | i | a | o |"
                                  0   1   2   3       s[1]= "b" non posso farlo
                                                      snow= S[0:1] + "b" s[2]

"""

#assegno alla variabile types_of_people 10
types_of_people = 10

#assegno alla variabile x la f-string "There are {types_of_people} types of people."
x = f"There are {types_of_people} types of people."

# assegno alla variabile bynary la stringa binary 
binary = "binary"

# assegno alla variabile do_not la stringa don't
do_not = "don't"

#assegno alla variabile y la f-string Those who know {binary} and those who {do_not}.
y = f"Those who know {binary} and those who {do_not}."

#stampo la variabile x e la variabile y 
print(x)
print(y)

#stampo tramite f-string le f-string x e y
print(f"I said: {x}")
print(f"I also said: '{y}'")

#assegno alla variabile booleana hilarious false
hilarious = False

#assegno alla variabile joke_evaluation la stringa Isn't that joke so funny?!
#la parentesi graffe servono per concatenare la stringa successivamente
joke_evaluation = "Isn't that joke so funny?! {}"

#stampo la variabile jojoke_evaluation concatenata attraverso format alla variabile booleana hilarious
print(joke_evaluation.format(hilarious))

#assegno alla variabile w la stringa This is the left side of...
w = "This is the left side of..."

#assegno alla variabile e la stringa a string with a right side.
e = "a string with a right side."

#stampo la variabile w concatenata alla variabile e attraverso il +
print(w + e)