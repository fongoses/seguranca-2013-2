## Universidade Federal do Rio Grande do Sul - Instituto de Informatica
## Departamento de Informatica Aplicada
## Seguranca em Sistemas de Computacao - 2013/2
## Professor: Raul Fernando Weber
## Alunos: Luiz Gustavo Frozi e  Mario Gasparoni Junior
##
## Desafio 5
##
## 
## Script que executa força bruta sobre o AES.
from Crypto.Cipher import AES
from Crypto import Random


cyphered = [] #cada bloco eh um elemento da lista
cyphered.append("E6A2C84DE51FA761")
cyphered.append("9BA0A3DA6C306F4B")
cyphered.append("137CB914B18F1DD6")
cyphered.append("E7BF45C5634FE31E")
cyphered.append("801F7E836873C284")
cyphered.append("3BBB19AB5DA1BDAE")
cyphered.append("5953C59D28F702E0")
cyphered.append("0EE59FB883DE9C67")
cyphered.append("14DAAA8628744A46")
cyphered.append("A5E39E2A909AFF4D")
cyphered.append("37CCF46ED9B29423")
cyphered.append("E986B53B498D9562")
cyphered.append("1610AAD8EBF8E280")
cyphered.append("5B19F58F9F5930A9")
cyphered.append("52C88E7E5054B7C0")
cyphered.append("F5A93688FF863E00")
cyphered.append("AF0335ECC7FA9B3A")
cyphered.append("A8895D986A1FC72E")
cyphered.append("232064A8C864608D")
cyphered.append("46E619763776EA4E")
cyphered.append("1580712BE23F5C62")
cyphered.append("3C595510B9397146")
cyphered.append("7C04CE1EB8CD98EF")
cyphered.append("5069EF001010A7E8")
cyphered.append("5ACB7367B5A09EAA")
cyphered.append("EE48332BC04207E3")
cyphered.append("90075010AB98FC75")
cyphered.append("BB4EF1B8A021136B")
cyphered.append("0C5A3FB8084865F8")
cyphered.append("F20909D4F7364684")
cyphered.append("0950E37C20DAF88D")
cyphered.append("CB1D61BF7169FFE8")
cyphered.append("96AF75E1AFF231FC")
cyphered.append("9F02B3F58E1713C7")

def isBadString(text):
    for c in text:
        if ((ord(c) <33) or (ord(c) >126)):
            return 1    
    return 0  

for i in range(33,126):    
    for j in range(33,126):
        for k in range(33,126):
            for l in range(33,126):
                for m in range(33,126):
                    key = b'Key2Group25'+chr(i)+chr(j)+chr(k)+chr(l)+chr(m)
                    cipher = AES.new(key, AES.MODE_ECB)
                    for block in cyphered:
                        plain = cipher.decrypt(block)#decifra bloco
                        if (isBadString(plain) == 0):
                            print "Key: " +key
                            print plain
                    
                       
