def multiplos(a):
    multiplos=[]

    aux=0
    while (aux<=10):
        multiplos.append(a*aux)
        aux+=1
    return multiplos

def executa():
    n1=input("Entre o número:\n")
    try:
        int(n1)
    except:
        print("Insira um número")
        return
    print(multiplos(int(n1)))

executa()