'''Este programa se encarga de crear una llave publica y privada y la graba en un
archivo .pem'''

from Crypto.PublicKey import RSA#Importacion de la clase RSA

llave = RSA.generate(2048)#Creacion de la llave

f = open("llaveprivada.pem","w")#Abrimos el archivo para escritura
f.write(llave.exportKey('PEM'))#Escribimos en el archivo la llave
f.close#Cerramos el archivo

f = open("llavepublica.pem","w")#Abrimos el archivo para escritura
f.write(llave.publickey().exportKey('PEM'))#Escribimos en el archivo la llave
f.close#Cerramos el archivo
