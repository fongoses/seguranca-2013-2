def primes(n):
    if n<=2:
        return []
    sieve=[True]*(n+1)
    for x in range(3,int(n**0.5)+1,2):
        for y in range(3,(n//x)+1,2):
            sieve[(x*y)]=False

    return [2]+[i for i in range(3,n,2) if sieve[i]]

def primesFactor(n):
    fatores = []
    fator = 2
    while fator < n:
        resto = n % fator
        multiplicidade = 0
        while resto == 0:
            multiplicidade += 1
            fatores += [fator]
            n //= fator
            resto = n % fator
        if multiplicidade > 0:
            print (fator, multiplicidade)
        fator += 1
    return fatores