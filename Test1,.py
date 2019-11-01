Codigo = input("Digite uma sequencia de números, separando-os por espaço: ")
Codigo_em_lista = Codigo.split()
NumeroM = int(Codigo_em_lista[0])
NumeroN = int(Codigo_em_lista[1])
ListaM = Codigo_em_lista[2:NumeroM+2]
ListaN = Codigo_em_lista[NumeroM + 2 : len(Codigo_em_lista)]



if NumeroM <=5 or NumeroN <= 10:
    print("Reescreva o codigo")
    Codigo = input("Digite uma sequencia de números, separando-os por espaço: ")
    Codigo_em_lista = Codigo.split()
    NumeroM = int(Codigo_em_lista[0])
    NumeroN = int(Codigo_em_lista[1])
    ListaM = Codigo_em_lista[2:NumeroM+2]
    ListaN = Codigo_em_lista[NumeroM + 2 : len(Codigo_em_lista)]

    
        
print(ListaM)


def Soma_ListaM(Lista_a_ser_usada):
    Soma_Parte_M = 0
    for indice in range(2, NumeroM + 2):
            Soma_Parte_M += int(Codigo_em_lista[indice])
    return Soma_Parte_M


print(Soma_ListaM(Codigo_em_lista))

'''if Soma_ListaM(Codigo_em_lista) % '''

