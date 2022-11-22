blocks = int(input("Ingresa el número de bloques: "))
height = int()

while blocks > 0 and blocks > height:
    height = height + 1
    blocks = blocks - height

print("La altura de la pirámide:", height)