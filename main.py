
def suma(n1,n2,n3):
    resultado=n1+n2+n3
    return(resultado)

lista=[]

for i in range(1,3):
    n1 = int(input("Var 1"))
    n2 = int(input("Var 2"))
    n3 = int(input("Var 3"))
    lista.append(suma(n1,n2,n3))

print(f"{lista}")
