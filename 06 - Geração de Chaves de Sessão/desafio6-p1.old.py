## Universidade Federal do Rio Grande do Sul - Instituto de Informatica
## Departamento de Informatica Aplicada
## Seguranca em Sistemas de Computacao - 2013/2
## Professor: Raul Fernando Weber
## Alunos: Luiz Gustavo Frozi e  Mario Gasparoni Junior
##
## Python 3.2
##
## Desafio 6 - Parte 1
##
## Script que executa encontra a chave de sessão de um algoritmo Diffie-Hellman
## multiplicativo.
##
from Crypto.Cipher import AES
from Crypto import Random

#
# Infomacoes Interceptadas
#

# Numero Primo
n = 340282366920938463463374607431768211297

# Segundo Numero
g = 339661812359158752487805590648382723989

# Alice -> Bob : X = x * g mod n
X = 234399727922910008434346336719740475791

# Bob -> Alice : Y = y * g mod n
Y = 317353208171493985828526472609655218772

# Mensagem Cifrada
cyphered = [] #cada bloco eh um elemento da lista
cyphered.append("62876D72F63FA4416232323FCD174AA5")
cyphered.append("24D6CCC8FEA90D80BB0D760484FF250D")
cyphered.append("55E1379F1A9AEA1CCB4F78A493A52D3B")
cyphered.append("366DF3E0D8FE243C678EA5684CA93BA9")
cyphered.append("2223F0319C61F988F8458629DC40F012")
cyphered.append("D4CA5B4F9EB764280CACF7D94BB6AD72")
cyphered.append("45BF11ACEEE09B345EBB3C7FEE4DE538")
cyphered.append("A88A7581C03489671C39E3E8D7BBB583")
cyphered.append("E5AC55D051D25AC0D3037894F84448EC")
cyphered.append("FD2BA8F131FDCDE263350EDB2FF05788")
cyphered.append("406B31C60D98C82FCE5691048D941297")
cyphered.append("AEA2A59EFE1F0F302B772E3FA71ADC2B")
cyphered.append("F41F2A9366D23A6466F0189FAA64DBD2")
cyphered.append("A2886B04E44ADD5DA017750ABE3B9640")
cyphered.append("64830D476141C52ADF1A1F6CEF9B251F")
cyphered.append("0B32B0939F0D39649E922D9079D5F40D")
cyphered.append("37223AEBDA6B8A9CE90C6AF7377314CF")
cyphered.append("BB8536DA945BACF0A49806E203AF9360")
cyphered.append("AB99EE8C6B039DAFF19B98F9B022DF31")
cyphered.append("45A9BEED64D31BAC0E0D4C123CF75414")
cyphered.append("63C4E0B54D9EA3672C8A01278D76D8AB")
cyphered.append("51AF84E6AA724D88ACBDF38C5A97536B")
cyphered.append("0663A73267A1B844B6C7964EB37F5DC6")
cyphered.append("00359B2A6B2A5F84746DB2AD3C673E96")
cyphered.append("0DFE64AA45DC88551DDC719097394D81")
cyphered.append("64B85E0D31E0E0F9101E7B81CBAE9A10")
cyphered.append("87352B318B6A922F0F13C55D03ED3616")
cyphered.append("EBEC0742A7609730860BB63FED4D87AB")
cyphered.append("2A38410548B923D84E963E76434C4390")
cyphered.append("EDBB171C2CAAFE26CB15ED5397CD6072")
cyphered.append("8326D2B0688AF789977F11A2F6568F94")
cyphered.append("E97D50D3B537600C8BDAA679DA9DF008")
cyphered.append("40A369C1F8D33AC3270DE9A930E27199")
cyphered.append("2C046043401CBDF5056F072B89ACCA9E")
cyphered.append("B679E8EE601A2319D23D71DC16A069A3")
cyphered.append("BB8D80A332F807F4F530D48643234A70")
cyphered.append("17F3691B907822EC6C1D7F2291AC2840")
cyphered.append("F64640F53B639E2FBDE92AAC2D9C7001")
cyphered.append("7195DF585525B1074D055574A6BC539E")
cyphered.append("00B68BAED5E9D42944B17F276BE5C177")
cyphered.append("3D73DF93029D323C9C3727F28212A034")
cyphered.append("71EAF2195578CEC509926EB9B7F03D5B")
cyphered.append("58242C0FF430AC3EE612D4E23C260A38")
cyphered.append("5E6ADE558D68B0E6D426B653BAF1D5ED")
cyphered.append("846157BB8A7BFD37BC26546C6566A4DF")
cyphered.append("537A2B1074A990143DFED27F974FA118")
cyphered.append("E1D346FE32CB9E510802CE1AEDAC800F")
cyphered.append("F6AA7193C300A28881AC2139E900E332")
cyphered.append("1CD23686429A1B96BF08F1EAC2DA03A2")
cyphered.append("392FA0CC520732602B0908BBC6E1FAC5")
cyphered.append("B43621C47BD4B691FD23BB4C8C72C7F3")
cyphered.append("B9DCBCE039FEA805A2A3C2461D7F6D20")
cyphered.append("0EC3BA63FE34B07E64ED88B1381BA6F5")
cyphered.append("38D9D9868FA77585846604CD68004DE1")
cyphered.append("F3496484D8805A464845180A372A783A")
cyphered.append("EC7A5A18E5CB5F85C07E0DB47B3A6176")
cyphered.append("45DDB95EDF2310445952F8D8F7891919")
cyphered.append("53C2EAC56834F10C28C1C6BC0C211BBE")
cyphered.append("2923F64FCB596779BD306ADD5198C834")
cyphered.append("434B417A75DACE44170C57873B7A1017")
cyphered.append("CFF67B5091BB2E174E16E89E79EE48B8")
cyphered.append("FA02E504ED5F95282F72936076B4977A")
cyphered.append("F50BED746F702684676E83008A6BF332")
cyphered.append("A377160D0A5787573A31B2F7496CD9FE")
cyphered.append("3B7F8211933A2BA58ED49EC8E1AA1F44")
cyphered.append("0577005A5EDD846716546217F48F0D11")
cyphered.append("ADAF225B3D710D5F91DC0B644C93069B")
cyphered.append("AEF1DD06B4884B5C5E04343FB444E8B1")
cyphered.append("C4D4032FA3F1130C6FED663EB76E8F88")
cyphered.append("FDA87820B78E26CB2547EC0FEA40AB17")
cyphered.append("117B451382052780E7430D2BD6A3662D")
cyphered.append("A24A4182E5627AD9BFE5BF24D437CE96")
cyphered.append("7CE3DF19F8F87F6928C0FE25DD0E2F72")
cyphered.append("ADA79F05D18516E3FA46023DAD49690E")
cyphered.append("53FB73BC1152061613349E09D22A703B")
cyphered.append("71A1A5CAE851CE8981A72555EAC8C0CC")
cyphered.append("DBCCD65C9F156BDD8037AB7AB57C42B9")
cyphered.append("B42A2402D14A8EB94170644F37396803")
cyphered.append("C7A0ED7B3CDFB45FED182B6D1C21575A")
cyphered.append("3910150CA7C9A6623C3706DD913A9887")
cyphered.append("8164ACF4C1F60D8CB5C1F9DB846911EC")
cyphered.append("DF774ABB054F12D4433322FFDF5D122F")
cyphered.append("F98AC0A783A5DC3D3A4C5A54320C02FD")
cyphered.append("CDC4101626FE13CA1606C03EB83DCB3D")
cyphered.append("9045EABC2B8C3B608E270653076912B3")
cyphered.append("EE234B5FA10D3944B7A35E7E84FA0FEC")
cyphered.append("CB7D6A691F941A86CB715B4F03FC2202")
cyphered.append("FC8B3E0210CCB974128A92DF746B9529")
cyphered.append("FC7E72127701F6C3E264D094EC16632C")
cyphered.append("A30F49DF6DD1BC992D42082E8AD79E9A")
cyphered.append("48DA0A20817FD75A8A121AB126138E9D")
cyphered.append("F4212EC1CE368350D85FB7091D53D61E")
cyphered.append("FF2ADEE6B06319864F705A7792539931")
cyphered.append("DE6BFC90AE5118EF06A11198513466BE")
cyphered.append("D4FD68518A56D5E9BB7B1A3F48B41CEC")
cyphered.append("24972F4C1738475B8580F8AE02F6FB87")
cyphered.append("9119E1EBF6AF543C11CB3D539CFCB8C9")

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

#
# Inicio do Ataque
#
g_inv = modinverse(g, n)

K = (X * Y * g_inv) % n

print("Key:")
key = makeKey128(K)
print(key)

print("Texto:")
bkey = bytes(key)
cipher = AES.new(bkey, AES.MODE_ECB)
for block in cyphered:
    plain = cipher.decrypt(block) #decifra bloco
    print(plain)
