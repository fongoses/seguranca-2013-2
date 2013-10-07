## Universidade Federal do Rio Grande do Sul - Instituto de Informatica
## Departamento de Informatica Aplicada
## Seguranca em Sistemas de Computacao - 2013/2
## Professor: Raul Fernando Weber
## Alunos: Luiz Gustavo Frozi e  Mario Gasparoni Junior
##
## Python 2.7
##
## Desafio 6 - Parte 3
##
## Script que calcula as chaves (n,e) e (n,d), chaves publica e privada 
## indicadas no segundo arquivo.
##
from Crypto import Random
import fractions

# Primo do Primeiro Arquivo
p = 5700734181645378434561188374130529072194886064169

# Primo do Segundo Arquivo
q = 35894562752016259689151502540913447503526083244127

# Desafio a ser assinado
desafio = 79657283408167701961383242801433670716

#
# Biblioteca
#
def primoRelativo(n):
    p = int(Random.get_random_bytes(128).encode('hex'), 16)
    i = 1
    while fractions.gcd(p, n) != 1:
        p = int(Random.get_random_bytes(128).encode('hex'), 16)
        i += 1
        if i > 100000:
            return None
    return p
    
# Versao do gcd/mdc modificada entre "a" e "b"
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Calcula o inverso multiplicativo de "a" em modulo "m"
def modinverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


#
# Execucao do RSA
#

n = p * q
n_temp = (p - 1) * (q - 1)

e = primoRelativo(n_temp)
public_key = (n, e)
print "Chave Publica (n, e) = ", public_key

d = modinverse(e, n_temp)
private_key = (n, d)
print "Chave Privada (n, d) = ", private_key

assinatura = pow(desafio, d, n)
print "Desafio: ", desafio
print "Assinatura: ", assinatura

verificacao = pow(assinatura, e, n)
if verificacao == desafio:
    print "Verificacao OK"
else:
    print "Assinatura Invalida"
