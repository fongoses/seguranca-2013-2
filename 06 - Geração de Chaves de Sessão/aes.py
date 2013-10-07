## Universidade Federal do Rio Grande do Sul - Instituto de Informatica
## Departamento de Informatica Aplicada
## Seguranca em Sistemas de Computacao - 2013/2
## Professor: Raul Fernando Weber
## Alunos: Luiz Gustavo Frozi e  Mario Gasparoni Junior
##
## Desafio 5
##
## 
## Script que executa forca bruta sobre o AES.
from Crypto.Cipher import AES
from Crypto import Random


cyphered = [] #cada bloco eh um elemento da lista
cyphered.append("E6A2C84DE51FA7619BA0A3DA6C306F4B".decode("hex"))
cyphered.append("137CB914B18F1DD6E7BF45C5634FE31E".decode("hex"))
cyphered.append("801F7E836873C2843BBB19AB5DA1BDAE".decode("hex"))
cyphered.append("5953C59D28F702E00EE59FB883DE9C67".decode("hex"))
cyphered.append("14DAAA8628744A46A5E39E2A909AFF4D".decode("hex"))
cyphered.append("37CCF46ED9B29423E986B53B498D9562".decode("hex"))
cyphered.append("1610AAD8EBF8E2805B19F58F9F5930A9".decode("hex"))
cyphered.append("52C88E7E5054B7C0F5A93688FF863E00".decode("hex"))
cyphered.append("AF0335ECC7FA9B3AA8895D986A1FC72E".decode("hex"))
cyphered.append("232064A8C864608D46E619763776EA4E".decode("hex"))
cyphered.append("1580712BE23F5C623C595510B9397146".decode("hex"))
cyphered.append("7C04CE1EB8CD98EF5069EF001010A7E8".decode("hex"))
cyphered.append("5ACB7367B5A09EAAEE48332BC04207E3".decode("hex"))
cyphered.append("90075010AB98FC75BB4EF1B8A021136B".decode("hex"))
cyphered.append("0C5A3FB8084865F8F20909D4F7364684".decode("hex"))
cyphered.append("0950E37C20DAF88DCB1D61BF7169FFE8".decode("hex"))
cyphered.append("96AF75E1AFF231FC9F02B3F58E1713C7".decode("hex"))

minChar = 33
maxChar = 126
minCharWhitespace = 32

def isBadString(text):
    for c in text:
        if ((ord(c) <minCharWhitespace) or (ord(c) >maxChar)):
            return 1    
    return 0  

for i in range(minChar,maxChar):    
    for j in range(minChar,maxChar):
        for k in range(minChar,maxChar):
            for l in range(minChar,maxChar):
                for m in range(minChar,maxChar):
                    key = b'Key2Group25'+chr(i)+chr(j)+chr(k)+chr(l)+chr(m)
                    cipher = AES.new(key, AES.MODE_ECB)
                    for block in cyphered:
                        plain = cipher.decrypt(block)#decifra bloco
                        if (isBadString(plain) == 0):
                            print "Key: " +key
                            print plain
                        else:
                            break
                    
                       
