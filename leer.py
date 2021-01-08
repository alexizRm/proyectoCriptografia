print("Hola para desencritar ingresa la frase")
frase = input()

datos == frase
with open("datos.txt") as fname:
	datos = fname.readlines()
	for linea in lineas:
		datos.append(linea.strip('\n'))
print (datos)
