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
    n1=input("Entre o número:\n")
    try:
        int(n1)
    except:
        print("Insira apenas números")
        return
    print("Multiplos:",multiplos(int(n1)))
    print("Divisores",divisores(int(n1)))

executa()