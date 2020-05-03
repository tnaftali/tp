import sys

def permutations(list):
  if len(list) == 0:
    ## evaluo si la lista esta vacia, en cuyo caso devuelvo una lista vacia
    return []
  elif len(list) == 1:
    ## si la lista tiene 1 solo elemento, retorno ese elemento de la lista
    return [list]
  else:
    ## creo una nueva lista con las nuevas permutaciones
    perm_list = []
    ## recorro la lista con un for
    ## me quedo con el primer elemento de la lista para luego hacer las
    ## combinaciones con todos los elementos subsiguientes
    ## realizo la recursion con los elementos subsiguientes buscando las permutaciones
    ## guardo todos los resultados en la lista final, la cual retorno
    for i in range(len(list)):
      current = list[i]
      next = list[:i] + list[i+1:]
      for p in permutations(next):
        perm_list.append([current]+p)
    return perm_list


## lista de el ementos que se va a permutar
list = []
inserted_items = input("Ingresar números separados por coma\n").split(",")
for item in inserted_items:
  list.append(int(item))
for p in permutations(list):
  print(p)
