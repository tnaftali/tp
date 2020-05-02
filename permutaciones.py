## TP1 Algoritmos y Estructuras de Datos II
## Integrantes:
## Maria Pia Pepe
## Tobias Naftali
## Rodrigo Federico Quiroga
def permutaciones(lst):
    if (len(lst) == 0):
        ## evaluo si la lista esta vacia, en cuyo caso devuelve una lista vacia
        return []
    elif (len(lst) == 1):
        ## si la lista tiene 1 solo elemento, retorno ese elemento de la lista
        return [lst]
    else:
        ## creo una nueva lista con las nuevas permutaciones
        l=[]
        ## recorro la lista con un for
        ## me quedo con el primer elemento de la lista para luego hacer las
        ## combinaciones con todos los elementos subsiguientes
        ## realizo la recursion con los elementos subsiguientes buscando las permutaciones
        ## guardo todos los resultados en la lista final, la cual retorno
        for i in range(len(lst)):
            eInicial=lst[i]
            eSubsiguientes = lst[:i] + lst[i+1:]
            for p in permutaciones(eSubsiguientes):
                l.append([eInicial]+p)
        return l
            
            
lista = [6,2,3]
## lista de el ementos que se va a permutar
for p in permutaciones(lista):
    print(p)
