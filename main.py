lista = [3, 6, 1, 5, 7, 2, 8]

def ordenar_lista(lista):
    for i in lista:
        lista.sort()
        return lista

print(ordenar_lista(lista))