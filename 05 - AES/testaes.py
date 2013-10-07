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


cyphered = [] #cada bloco eh um elemento da lista
cyphered.append("Texto para teste")

key = b'essasenhaehfraca'
cipher = AES.new(key, AES.MODE_ECB)
for block in cyphered:
    cyphered = cipher.encrypt(block)#criptografa bloco
    for c in cyphered: #imprime cada caracter em ascii
        print hex(ord(c))

                       
