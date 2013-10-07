## Universidade Federal do Rio Grande do Sul - Instituto de Informatica
## Departamento de Informatica Aplicada
## Seguranca em Sistemas de Computacao - 2013/2
## Professor: Raul Fernando Weber
## Alunos: Luiz Gustavo Frozi e  Mario Gasparoni Junior
##
##
## 
## Script para executar o teste de algoritmo do professor.

from Crypto.Cipher import AES
from Crypto import Random


plain = [] #cada bloco eh um elemento da lista
plain.append("Texto para teste")
cyp = "A506A19333F306AC2C62CBE931963AE7".decode("hex") #texto em hexadecimal fornecido pelo professor
key = b'essasenhaehfraca'
cipher = AES.new(key, AES.MODE_ECB)
for block in plain:
    cyphered = cipher.encrypt(block)#criptografa bloco
    for c in cyphered: #imprime cada caracter em ascii
        print hex(ord(c))

    decyphered=cipher.decrypt(cyphered)
    print decyphered


decyphered=cipher.decrypt(cyp)
print decyphered
                       
