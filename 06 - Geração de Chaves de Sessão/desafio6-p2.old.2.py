## Universidade Federal do Rio Grande do Sul - Instituto de Informatica
## Departamento de Informatica Aplicada
## Seguranca em Sistemas de Computacao - 2013/2
## Professor: Raul Fernando Weber
## Alunos: Luiz Gustavo Frozi e  Mario Gasparoni Junior
##
## Python 2.7
##
## Desafio 6 - Parte 2
##
## Script que executa encontra a chave de sessao de um algoritmo Diffie-Hellman
## multiplicativo.
##
from Crypto.Cipher import AES
#from Crypto import Random
import array
#
# Infomacoes Interceptadas
#

# Numero Primo
n = 340282366920938463463374607431768211297

# Segundo Numero
g = 2

# Bob -> Alice : Y = g^y mod n
Y = 111378665949503964756483212252284796659

# Alice -> Bob : X = g^x mod n
X = 203296100051928047072369865615321706708

# Mensagem Cifrada
cyphered = [] #cada bloco eh um elemento da lista
cyphered.append("45518D4B3B2518E31433F73774B68093".decode("hex"))
cyphered.append("1ACCBEEB4CAEA4FDF628E998FCDE1A56".decode("hex"))
cyphered.append("A9B8E8FCF8BF06397AFA1A790BF789A3".decode("hex"))
cyphered.append("55424C30DB0A7234F03269C9520D7D2A".decode("hex"))
cyphered.append("829279996DA2B361F92AF6E31BC34B22".decode("hex"))
cyphered.append("1D6607B0C78288B5F9069DA7E3FAE145".decode("hex"))
cyphered.append("6B923611B489CB04F122A7FD6AEBFA59".decode("hex"))
cyphered.append("09F4821CA9B511C05DDF335BB4246A39".decode("hex"))
cyphered.append("9DEB838A06D7A2DD6C333ADE60E3B565".decode("hex"))
cyphered.append("BCBC6053CDD2BF08299CC127C7E44E9C".decode("hex"))
cyphered.append("94DAC960741A0756D481C7A509D4189A".decode("hex"))
cyphered.append("3FB887E65A77954E6A2B3E2D7CE47736".decode("hex"))
cyphered.append("95FB155BCF74E8FD30AD45C25D5B3D08".decode("hex"))
cyphered.append("F69F5DB34906563D673585D0F3C9AA67".decode("hex"))
cyphered.append("25366AA2B236CF9FB51C2DA0D233260A".decode("hex"))
cyphered.append("7BC5FAA7C0213C4D5BBDA831409D17D1".decode("hex"))
cyphered.append("21CD990066C10E00679FFA0DC2C22871".decode("hex"))
cyphered.append("CF218773C81EA3F5A9B5E2415E9496A6".decode("hex"))
cyphered.append("BE5C0B917AF7445A4E95A64A9E3A0D67".decode("hex"))
cyphered.append("408C9D79636D87C433CAC5AB5AECDF53".decode("hex"))
cyphered.append("3BB95707E93763060A2704A818D6F8DB".decode("hex"))
cyphered.append("A89A7E9086DA497282D89BCE421ECAC3".decode("hex"))
cyphered.append("948C03159C0B8ECF98A70FE955487F3B".decode("hex"))
cyphered.append("61A79056CDD48E5DDFC97E5983E1720D".decode("hex"))
cyphered.append("D6C63810B8DE8AE970D9DCCC43CBF802".decode("hex"))
cyphered.append("4ED84B42E2FA2DB43B62446D0BACB2EB".decode("hex"))
cyphered.append("BCB3ECD2DFD3B44DF0B5C8911A9FABB1".decode("hex"))
cyphered.append("06BACC5CF9F0C0D63186CA1948C1BF42".decode("hex"))
cyphered.append("E2A32BA5B85BAB2FA14758A1D7544E7E".decode("hex"))
cyphered.append("864B1AEECF1C423CA237499241B43719".decode("hex"))
cyphered.append("A69FE964A04445BAA2087B645033FB08".decode("hex"))
cyphered.append("34A06BFAC16CB9807C35FF6E049BFEC2".decode("hex"))
cyphered.append("FF38DA78840B1738062B16E4CA7F9B3F".decode("hex"))
cyphered.append("EAF95F56E120B7DA55EA4747650A2F92".decode("hex"))
cyphered.append("4208CCB73E114B4CB5575AA569117EE7".decode("hex"))
cyphered.append("A04A9FB9A9331BD2AD6EAA2E816D8344".decode("hex"))
cyphered.append("99BE100E62C76CA8C88CFAFCAC009052".decode("hex"))
cyphered.append("3FF976DE5C55845ACECE623CC436CC33".decode("hex"))
cyphered.append("2041B5EF6E61085EA6418843D54C3C19".decode("hex"))
cyphered.append("2EFB07C387226AF2AE5EFAC30B008F0C".decode("hex"))
cyphered.append("2E5657418020327E11286A0B612E58D9".decode("hex"))
cyphered.append("5CF287063F59561CC9B2DCA92683C20E".decode("hex"))
cyphered.append("4E4E57EBC34A09BAB3F7DB6E40D7A093".decode("hex"))
cyphered.append("97FF5D0DD8944ABBADC67BB89EDACBE2".decode("hex"))
cyphered.append("7EED3188CF4D893B3635FB1993070FFB".decode("hex"))
cyphered.append("6D3763BB2760051C6B30D20FA48BA92A".decode("hex"))
cyphered.append("109D395E44EE2A0C1EA1B53B6F59F46B".decode("hex"))
cyphered.append("DAF6F729A02546A4118D8EFE941F6B29".decode("hex"))
cyphered.append("4AEC8A6153FCA42B97034F4A1FBA4E0C".decode("hex"))
cyphered.append("43248618C17BA30D612BB66F8C3FAFD5".decode("hex"))
cyphered.append("7A6743C2900845603D817CC761137E05".decode("hex"))
cyphered.append("50167F1D7104803462B5F750D3465F12".decode("hex"))
cyphered.append("FBEA95B6199BB8A169B772A494B803A9".decode("hex"))
cyphered.append("83AFC2E308A78FEA8A4AA166CDBBBF3E".decode("hex"))
cyphered.append("FD762E7BBFC2B4A0D6BE49E9C7952A84".decode("hex"))
cyphered.append("3C4B65AFA9093D176EBD15C709DD7A4E".decode("hex"))
cyphered.append("044276F3DE0E3FAFBA31A5B558C58F47".decode("hex"))
cyphered.append("8B3CA6AECDF0A309321239E0AFE5399D".decode("hex"))
cyphered.append("683F3E24449497459EDFC54E1971519D".decode("hex"))
cyphered.append("86CD3446527452847965039BD2B2D6C3".decode("hex"))
cyphered.append("CFE9B62F258945BB7826BD2A09D70671".decode("hex"))
cyphered.append("962A78815E7A06A1338CF4142B2A357B".decode("hex"))

#
# Funcoes de Biblioteca
#
# Algoritmo para gerar a chave citado nas mensagens
def makeKey128(key):
    bytechave = [None]*16
    for i in range(0, 16):
        bytechave[i] = key % 256
        key = key // 256
    return bytechave

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

# Calcula o numero randomico usando a regra de formacao citada na mensagem 1
def fakeRandom(x, y, w, z):
    return 2**x * 3**y * 5**w * 7**z

# Tenta encontrar o logaritmo discreto usando a regra de formacao citada
# (algoritmo trivial)
def modlog(X, g, n):
    print "modlog(", X, ", ", g, ", ", n, ")"
    for a in range(1, 161):
        for b in range(1, 161):
            for c in range(1, 161):
                for d in range(1, 161):
                    x = fakeRandom(a, b, c, d)
                    if len(str(x)) > 50:
                        break
                    else:
                        if X == pow(g, x, n):
                            return x
        print "(x, a, b, c, d) = ", (x, a, b, c, d)
    raise Exception('modular log does not exist')

# Versao mais otimizada
def modlogInverse(X, g, n):
    print "modlogInverse(", X, ", ", g, ", ", n, ")"
    for d in range(13, 161):
        for c in range(1, 161):
            for b in range(1, 161):
                for a in range(1, 161):
                    x = fakeRandom(a, b, c, d)
                    if len(str(x)) > 50:
                        break
                    else:
                        #print "(x, a, b, c, d) = ", (x, a, b, c, d)
                        if X == pow(g, x, n):
                            return x
        print "(x, a, b, c, d) = ", (x, a, b, c, d)
    raise Exception('modular log does not exist')

def modlogN(X, g, n):
    print "modlogN(", X, ", ", g, ", ", n, ")"
    x = 0
    while x < n:
        #print (X, x)
        if X == pow(g, x, n):
            return x
        x += 1
    raise Exception('modular log does not exist')

def discreteLogModP(a, b, p):  # brute force version
    '''Returns x so pow(a, x, p) is b mod p, or None if no solution.'''
    print "discreteLogModP(", a, ", ", b, ", ", p, ")"
    x = 0
    a_x = 1
    b %= p
    while x < p:
        if a_x == b: return x
        a_x = a_x * a % p
        x += 1
    return None

#
# Inicio do Ataque
#

# O ataque deve ser feito no numero do Bob que possui uma regra de formacao fraca
#y = modlogInverse(Y, g, n) # depois de (a, b, c, d) = (1, 160, 160, 14) na iteracao, depois de 28 horas, Core 2 Duo com 2,4GHz e 4GB de RAM
y = 69509746771281455987953422720000000000000000000000 # Resultado do logaritmo = randomico do Bob
print "y:", y
arquivo_random = open('desafio6-p2.random', 'w')
arquivo_random.writelines(str(y))
arquivo_random.close()


# K = pow(X, y, n)
K = 283903288088203077050299572641376932758L
print "K:", K
arquivo_k = open('desafio6-p2.k', 'w')
arquivo_k.writelines(str(K))
arquivo_k.close()

print "Key:"
key = makeKey128(K)
print key

strkey = "".join(chr(x) for x in key) #key eh uma lista de inteiros, 
#converte cada int em char e depois da um join nessa lista de string com a string ""

print "Texto:"

arquivo = open('desafio6-p2.unciphered', 'w')

cipher = AES.new(strkey, AES.MODE_ECB)
for block in cyphered:
    plain = cipher.decrypt(block) #decifra bloco
    print(plain)
    arquivo.writelines(plain)

arquivo.close()
