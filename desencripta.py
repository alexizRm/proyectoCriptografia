from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

f = open ("textocifrado.txt","r")

mensaje = f.read ()
key = RSA.importKey(open("llaveprivada.pem","r").read())
cifrado = PKCS1_OAEP.new(key)
deciframensaje = cifrado.decrypt(mensaje)

print deciframensaje
