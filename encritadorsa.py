#Este programa se encarga de encriptar un mensaje ingresado por el usuario

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

print "Hola Ususario, usted esta entrando a el encriptador de mensajes"
print "Ingrese el mensaje que desea encriptar:"
texto = raw_input()

mensaje = texto
key = RSA.importKey(open("llavepublica.pem","r").read())#
cifrado =PKCS1_OAEP.new(key)
cifrarmensaje =cifrado.encrypt(mensaje)

f = open ("textocifrado.txt", "w")
f.write (cifrarmensaje)
f.close
