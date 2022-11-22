# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.

user_word = input("Introduce una palabra: ")
user_word = user_word.upper()
palabra_sin_vocales = ""
for letter in user_word:
    # Completa el cuerpo del bucle for.
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    else:
        palabra_sin_vocales = palabra_sin_vocales + letter
        
print(palabra_sin_vocales)
print()


#  or letter == "E" or letter == "I" or letter == "O" or letter == "U"