def multiplos(a):
    multiplos=[]

    aux=0
    while (aux<=10):
        multiplos.append(a*aux)
        aux+=1
    return multiplos

def divisores(a):
    divisores=[]
    for n in range(1,11):
            if a%n==0:
                divisores.append(n)
    return divisores

def executa():
    n1=10
    print("Número será:",n1)
    print("Multiplos:",multiplos(n1))
    print("Divisores",divisores(n1))

executa()