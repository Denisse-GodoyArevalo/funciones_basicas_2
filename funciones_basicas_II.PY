#1 cuenta regresiva
def Cuenta_regresiva(num):
    resultado = []
    for valor in range(num ,-1, -1):
        resultado.append(valor)
    return resultado    
print(Cuenta_regresiva(5))    

#2 imprimir y devolver 
def imprimir_devolver(lista):
    print(lista[0])
    return lista[1]

valor_devuelto = imprimir_devolver([1,2])
print(valor_devuelto)

#3 primero mas longitud
def primero_mas_longitud(lista):
    suma = lista[0] + len(lista)
    return suma
print(primero_mas_longitud([10,20,30,40]))

#4 valor mayor que el segundo
def valores_mayores(lista):
    nueva_lista = []
    for valor in lista:
        if valor > lista[1]:
            nueva_lista.append(valor)
    print(f"son {len(nueva_lista)} valores mayores que {lista[1]}")
    return nueva_lista

print(valores_mayores([5,2,3,2,1,4]))

#5 Esta longitud, ese valor
def tamaño_longitud(lista):
    lista_nueva = []
    cont = 1
    while cont <= lista[0]:
        lista_nueva.append(lista[1])
        cont += 1
    return lista_nueva
print(tamaño_longitud([4,7]))
print(tamaño_longitud([6,2]))    

